#!/usr/bin/env python3
"""Deterministic, synthetic-only Ariadline compact kill-test rehearsal."""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

ALLOWED_DOMAINS={"theoretical_typological","descriptive_community","corpus_experimental","computational_resource"}
ALLOWED_PRESERVATION={"preserved","not_preserved","not_determined"}
EXCLUSION_CODES={"TECHNICAL_FAILURE","FROZEN_MISSINGNESS_LIMIT","DUPLICATE_PARTICIPATION","WITHDRAWAL","ASSIGNMENT_INTEGRITY_FAILURE","MISSING_RESPONSE"}
OUTPUT_FILES=("assignments.json","scoring_and_adjudication.json","analysis.json")

def canonical(v:Any)->str:return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))
def digest(v:Any)->str:return hashlib.sha256(canonical(v).encode()).hexdigest()
def unit(seed:int,*parts:str)->float:return int.from_bytes(hashlib.sha256("|".join((str(seed),*parts)).encode()).digest()[:8],"big")/2**64
def eligible(m:dict[str,Any])->bool:return m["conditions"]["P"]["preservation"]==m["conditions"]["S"]["preservation"]=="preserved" and m["comparability"]=="comparable" and m["authority_state"]=="simulated_approved"
def add(ok:bool,code:str,msg:str,out:list[dict[str,str]])->None:
    if not ok:out.append({"code":code,"message":msg})

def validate_source(d:dict[str,Any])->list[dict[str,str]]:
    f=[]; design=d.get("design",{}); mats=d.get("materials",[])
    add(d.get("synthetic_only") is True,"SYNTHETIC_FLAG","synthetic_only must be true",f)
    add(d.get("study_state")=="synthetic_rehearsal","STUDY_STATE","study_state must remain synthetic_rehearsal",f)
    add(d.get("evidence_claim")=="procedure_only","EVIDENCE_BOUNDARY","evidence_claim must be procedure_only",f)
    add(d.get("human_gates_simulated_only") is True,"SIMULATED_GATES","human gates must be simulated only",f)
    add(isinstance(design.get("seed"),int),"SEED","integer seed required",f)
    add(isinstance(design.get("participant_count"),int) and 20<=design["participant_count"]<=30,"PARTICIPANTS","20-30 participants required",f)
    add(design.get("items_per_participant")==6,"ITEMS","six items per participant required",f)
    add(design.get("primary_comparison")=="S_vs_P","COMPARISON","S versus P must be primary",f)
    add(10<=len(mats)<=12,"MATERIALS","10-12 materials required",f)
    add(len({m.get("material_id") for m in mats})==len(mats),"MATERIAL_IDS","material IDs must be unique",f)
    add(len({m.get("meaning_record_id") for m in mats})==len(mats),"MEANING_IDS","meaning IDs must be unique",f)
    add(len({m.get("domain_family") for m in mats})>=3 and {m.get("domain_family") for m in mats}<=ALLOWED_DOMAINS,"DOMAINS","registered domain coverage required",f)
    questions=set(); s_worse=inconclusive=adverse=False
    for m in mats:
        mid=m.get("material_id"); key=m.get("scoring_key",{})
        for label in ("P","S"):
            c=m.get("conditions",{}).get(label,{})
            add(c.get("preservation") in ALLOWED_PRESERVATION,"PRESERVATION",f"{mid}/{label} invalid preservation",f)
            probs=[c.get(k) for k in ("correct_probability","uncertain_probability","missing_probability")]
            add(all(isinstance(x,(int,float)) for x in probs) and 0<=sum(probs)<=1,"PROBABILITY",f"{mid}/{label} invalid probabilities",f)
        s_worse|=m["conditions"]["S"]["correct_probability"]<m["conditions"]["P"]["correct_probability"]
        inconclusive|=m.get("scenario_class")=="inconclusive"
        adverse|=any(m["conditions"][x]["preservation"]!="preserved" for x in ("P","S"))
        q=key.get("question_id"); add(bool(q) and q not in questions,"QUESTION_ID",f"{mid} question ID missing or duplicate",f); questions.add(q)
        add(key.get("material_id")==mid and key.get("meaning_record_id")==m.get("meaning_record_id"),"KEY_TRACEABILITY",f"{mid} key identity mismatch",f)
        add(str(key.get("key_hash","")).startswith("sha256:"),"KEY_HASH",f"{mid} key hash required",f)
        add(bool(m.get("candidate_rule_ids")),"RULE_IDS",f"{mid} rule IDs required",f)
    add(s_worse,"S_ADVERSE","at least one S-adverse material required",f);add(inconclusive,"INCONCLUSIVE","inconclusive material required",f);add(adverse,"ADVERSE_PRESERVATION","preservation failure/unresolved case required",f)
    seen=set()
    for x in d.get("planned_exclusions",[]):
        aid=x.get("assignment_id");add(bool(aid) and aid not in seen,"EXCLUSION_ID","planned exclusion IDs must be unique",f);seen.add(aid);add(x.get("code") in EXCLUSION_CODES,"EXCLUSION_CODE","frozen mechanical code required",f)
    add(bool(d.get("planned_exclusions")),"EXCLUSIONS","planned exclusion required",f);add(bool(d.get("planned_deviations")),"DEVIATIONS","planned deviation required",f)
    return sorted(f,key=lambda x:(x["code"],x["message"]))

def make_assignments(d:dict[str,Any])->dict[str,Any]:
    seed=d["design"]["seed"]; people=[f"SYN-PART-{i:02d}" for i in range(1,d["design"]["participant_count"]+1)]; mats=sorted((m for m in d["materials"] if eligible(m)),key=lambda m:m["material_id"])
    if len(mats)!=9 or len(people)%3:raise ValueError("cyclic-balanced-v2 requires 9 eligible materials and participant count divisible by 3")
    groups=((0,1,2,3,4,5),(3,4,5,6,7,8),(6,7,8,0,1,2));conds=({0:"P",1:"P",2:"P",3:"S",4:"S",5:"S"},{3:"P",4:"P",5:"P",6:"S",7:"S",8:"S"},{6:"P",7:"P",8:"P",0:"S",1:"S",2:"S"})
    public=[];restricted=[]
    for pi,pid in enumerate(people):
        g=(pi+seed%3)%3; idx=list(groups[g]);r=(pi//3+seed%6)%6;idx=idx[r:]+idx[:r]
        for order,mi in enumerate(idx,1):
            m=mats[mi];c=conds[g][mi];aid=f"SYN-ASG-{pi+1:02d}-{order:02d}";mask=f"SYN-TXT-{digest([aid,m['material_id'],c,seed])[:12]}"
            public.append({"assignment_id":aid,"participant_id":pid,"masked_text_code":mask,"order_position":order,"domain_family":m["domain_family"],"schedule_version":"SYN-SCHEDULE-0.2","schedule_hash":"pending"})
            restricted.append({"assignment_id":aid,"material_id":m["material_id"],"meaning_record_id":m["meaning_record_id"],"condition":c,"condition_output_hash":m["conditions"][c]["output_hash"]})
    h="sha256:"+digest({"seed":seed,"algorithm":"cyclic-balanced-v2","assignments":[{k:x[k] for k in ("assignment_id","participant_id","masked_text_code","order_position","domain_family")} for x in public],"restricted_condition_mapping":restricted})
    for x in public:x["schedule_hash"]=h
    return {"fixture_id":d["fixture_id"],"synthetic_only":True,"seed":seed,"algorithm":"cyclic-balanced-v2","participant_count":len(people),"eligible_material_count":len(mats),"assignments":public,"restricted_condition_mapping":restricted,"schedule_hash":h}

def response_class(seed:int,aid:str,c:dict[str,Any])->str:
    u=unit(seed,"response",aid);m=c["missing_probability"];q=c["uncertain_probability"];p=c["correct_probability"]
    return "missing" if u<m else "uncertain" if u<m+q else "correct" if u<m+q+p else "incorrect"

def make_scoring(d:dict[str,Any],a:dict[str,Any])->dict[str,Any]:
    seed=d["design"]["seed"]; mats={m["material_id"]:m for m in d["materials"]}; mp={x["assignment_id"]:x for x in a["restricted_condition_mapping"]}; planned={x["assignment_id"]:x for x in d["planned_exclusions"]}
    responses=[];scores=[];adjs=[];excluded=[]
    for pub in a["assignments"]:
        aid=pub["assignment_id"];r=mp[aid];m=mats[r["material_id"]];c=m["conditions"][r["condition"]];plan=planned.get(aid);ans=response_class(seed,aid,c)
        if plan and plan["code"] in {"TECHNICAL_FAILURE","FROZEN_MISSINGNESS_LIMIT"}:ans="missing";code=plan["code"]
        else:code="MISSING_RESPONSE" if ans=="missing" else plan["code"] if plan else None
        rid=aid.replace("SYN-ASG","SYN-RESP");state="technical_failure" if code=="TECHNICAL_FAILURE" else "missing" if ans=="missing" else "excluded" if code else "complete"
        responses.append({"response_id":rid,"assignment_id":aid,"masked_text_code":pub["masked_text_code"],"material_id":m["material_id"],"meaning_record_id":m["meaning_record_id"],"question_id":m["scoring_key"]["question_id"],"answer_class":ans,"response_value":None if ans=="missing" else f"synthetic-{ans}","condition_identity_absent":True,"rule_metadata_absent":True,"completion_state":state,"mechanical_exclusion_code":code})
        if code:
            excluded.append({"response_id":rid,"assignment_id":aid,"code":code,"frozen_mechanical_rule":True,"reason":plan["reason"] if plan else "synthetic missing response"});continue
        base={"correct":1.0,"uncertain":0.5,"incorrect":0.0}[ans];b=(0.5 if base in {0.0,1.0} else 1.0) if unit(seed,"disagreement",aid)<.12 else base;critical=ans=="incorrect" and unit(seed,"critical",aid)<c["critical_error_probability"]
        for sid,val,ind in (("SYN-SCORER-A",base,False),("SYN-SCORER-I",b,True)):
            scores.append({"score_id":f"{rid}-{sid.rsplit('-',1)[1]}","response_id":rid,"question_id":m["scoring_key"]["question_id"],"scorer_id":sid,"independent_of_ariadline":ind,"condition_identity_absent":True,"editor_metadata_absent":True,"scoring_key_hash":m["scoring_key"]["key_hash"],"score":val,"critical_error":critical})
        if base!=b:adjs.append({"response_id":rid,"question_id":m["scoring_key"]["question_id"],"adjudicator_id":"SYN-ADJ-I","independent_of_ariadline":True,"condition_identity_absent":True,"initial_scores":[base,b],"final_score":base,"reason":"synthetic deterministic adjudication"})
    return {"fixture_id":d["fixture_id"],"synthetic_only":True,"responses":responses,"scores":scores,"adjudications":adjs,"planned_exclusions":d["planned_exclusions"],"applied_exclusions":excluded,"planned_deviations":d["planned_deviations"]}

def disposition(s:dict[str,Any])->str:
    if s.get("s_preservation_failures",0)>s.get("p_preservation_failures",0) or (s.get("critical_preservation_failures",0)>0 and s.get("s_critical_failures",0)>s.get("p_critical_failures",0)):return "stop"
    if s.get("eligible_pairs",0)<6 or s.get("analyzable_responses",0)<80:return "insufficient_evidence"
    return "continue" if s.get("mean_score_S",0)-s.get("mean_score_P",0)>=.08 and s.get("mean_burden_S",0)-s.get("mean_burden_P",0)<=1 and s.get("mean_naturalness_S",0)-s.get("mean_naturalness_P",0)>=-.25 and s.get("unresolved_bias_flags",0)==0 else "revise"

def make_analysis(d:dict[str,Any],a:dict[str,Any],sc:dict[str,Any])->dict[str,Any]:
    mats={m["material_id"]:m for m in d["materials"]};mp={x["assignment_id"]:x for x in a["restricted_condition_mapping"]};sg=defaultdict(list)
    for x in sc["scores"]:sg[x["response_id"]].append(x)
    adj={x["response_id"]:x["final_score"] for x in sc["adjudications"]};final={rid:adj.get(rid,mean(x["score"] for x in rows)) for rid,rows in sg.items()};by=defaultdict(list);crit=Counter();exp=Counter();miss=Counter();exc=Counter();classes=Counter()
    for x in sc["responses"]:
        r=mp[x["assignment_id"]];c=r["condition"];exp[(r["material_id"],c)]+=1;classes[x["answer_class"]]+=1;miss[c]+=x["answer_class"]=="missing"
        if x["mechanical_exclusion_code"]:exc[c]+=1;continue
        by[c].append(final[x["response_id"]]);crit[c]+=any(y["critical_error"] for y in sg[x["response_id"]])
    em=[m for m in d["materials"] if eligible(m)];adv=[{"material_id":m["material_id"],"meaning_record_id":m["meaning_record_id"],"scenario_class":m["scenario_class"],"P_preservation":m["conditions"]["P"]["preservation"],"S_preservation":m["conditions"]["S"]["preservation"],"S_worse_probability":m["conditions"]["S"]["correct_probability"]<m["conditions"]["P"]["correct_probability"],"bias_flags":m.get("bias_flags",[]),"rule_ids":m["candidate_rule_ids"],"applicability_agreement":m["applicability_agreement"],"adverse_record_retained":m["adverse_record_retained"]} for m in d["materials"] if m["scenario_class"]!="neutral" or m.get("bias_flags") or not m["applicability_agreement"]]
    s={"participant_count":d["design"]["participant_count"],"assignment_count":len(a["assignments"]),"raw_response_count":len(sc["responses"]),"analyzable_responses":len(final),"initial_score_count":len(sc["scores"]),"adjudication_count":len(sc["adjudications"]),"applied_exclusion_count":len(sc["applied_exclusions"]),"eligible_pairs":len(em),"mean_score_P":round(mean(by["P"]),4),"mean_score_S":round(mean(by["S"]),4),"mean_burden_P":round(mean(m["conditions"]["P"]["burden_minutes"] for m in em),3),"mean_burden_S":round(mean(m["conditions"]["S"]["burden_minutes"] for m in em),3),"mean_naturalness_P":round(mean(m["conditions"]["P"]["naturalness"] for m in em),3),"mean_naturalness_S":round(mean(m["conditions"]["S"]["naturalness"] for m in em),3),"missing_P":miss["P"],"missing_S":miss["S"],"excluded_P":exc["P"],"excluded_S":exc["S"],"p_critical_failures":crit["P"],"s_critical_failures":crit["S"],"p_preservation_failures":sum(m["conditions"]["P"]["preservation"]=="not_preserved" for m in d["materials"]),"s_preservation_failures":sum(m["conditions"]["S"]["preservation"]=="not_preserved" for m in d["materials"]),"critical_preservation_failures":sum(any(m["conditions"][x]["preservation"]=="not_preserved" for x in ("P","S")) for m in d["materials"]),"unresolved_bias_flags":sum(len(m.get("bias_flags",[])) for m in d["materials"]),"applicability_agreement_rate":round(sum(m["applicability_agreement"] for m in em)/len(em),4),"response_class_counts":dict(sorted(classes.items()))}
    routes=[{"scenario":"continue","expected":"continue","derived":disposition({"eligible_pairs":9,"analyzable_responses":120,"mean_score_P":.6,"mean_score_S":.72,"mean_burden_P":8,"mean_burden_S":8.4,"mean_naturalness_P":4,"mean_naturalness_S":3.9,"unresolved_bias_flags":0})},{"scenario":"revise","expected":"revise","derived":disposition({"eligible_pairs":9,"analyzable_responses":120,"mean_score_P":.7,"mean_score_S":.72,"mean_burden_P":7,"mean_burden_S":9.5,"mean_naturalness_P":4.2,"mean_naturalness_S":3.4,"unresolved_bias_flags":1})},{"scenario":"stop","expected":"stop","derived":disposition({"eligible_pairs":9,"analyzable_responses":120,"p_preservation_failures":0,"s_preservation_failures":1})},{"scenario":"insufficient_evidence","expected":"insufficient_evidence","derived":disposition({"eligible_pairs":4,"analyzable_responses":40})}]
    val=validate_outputs(d,a,sc,s,adv,routes)
    return {"fixture_id":d["fixture_id"],"synthetic_only":True,"evidence_claim":"procedure_only","summary":s,"mock_disposition":disposition(s),"adverse_and_inconclusive_items":adv,"exposure_by_material_condition":[{"material_id":m,"condition":c,"count":n} for (m,c),n in sorted(exp.items())],"disposition_scenarios":routes,"validation":val,"non_generalization":"Synthetic operational output only; not evidence of Ariadline effectiveness, safety, or representativeness."}

def validate_outputs(d,a,sc,s,adv,routes):
    f=[];src=validate_source(d);mp={x["assignment_id"]:x for x in a["restricted_condition_mapping"]};mats={m["material_id"]:m for m in d["materials"]};by_p=defaultdict(list)
    for x in a["assignments"]:by_p[x["participant_id"]].append(x)
    no_dup=all(len({mp[x["assignment_id"]]["meaning_record_id"] for x in rows})==len(rows) for rows in by_p.values());dom=all(max(Counter(x["domain_family"] for x in rows).values())-min(Counter(x["domain_family"] for x in rows).values())<=1 for rows in by_p.values());ex=Counter((mp[x["assignment_id"]]["material_id"],mp[x["assignment_id"]]["condition"]) for x in a["assignments"]);bal=all(ex[(m["material_id"],c)]==8 for m in d["materials"] if eligible(m) for c in ("P","S"))
    sg=defaultdict(list);ag=defaultdict(list)
    for x in sc["scores"]:sg[x["response_id"]].append(x)
    for x in sc["adjudications"]:ag[x["response_id"]].append(x)
    masked=all(x["condition_identity_absent"] and x["editor_metadata_absent"] for x in sc["scores"]);trace=all(x["material_id"] in mats and x["meaning_record_id"]==mats[x["material_id"]]["meaning_record_id"] and x["question_id"]==mats[x["material_id"]]["scoring_key"]["question_id"] and all(y["scoring_key_hash"]==mats[x["material_id"]]["scoring_key"]["key_hash"] for y in sg[x["response_id"]]) for x in sc["responses"])
    unscored=routes_ok=True
    for x in sc["responses"]:
        rows=sg[x["response_id"]];ads=ag[x["response_id"]]
        if x["mechanical_exclusion_code"]:unscored&=not rows and not ads
        else:
            routes_ok&=len(rows)==2 and len({r["scorer_id"] for r in rows})==2 and any(r["independent_of_ariadline"] for r in rows)
            routes_ok&=(len(ads)==1 and ads[0]["independent_of_ariadline"] if len({r["score"] for r in rows})>1 else not ads)
    qg=defaultdict(list)
    for x in sc["scores"]:qg[x["question_id"]].append(x)
    qs={m["scoring_key"]["question_id"] for m in d["materials"] if eligible(m)};indq=all(qg[q] and any(x["independent_of_ariadline"] for x in qg[q]) for q in qs);mech=all(x["code"] in EXCLUSION_CODES and x["frozen_mechanical_rule"] for x in sc["applied_exclusions"]) and {x["assignment_id"] for x in sc["applied_exclusions"]}>={x["assignment_id"] for x in d["planned_exclusions"]}
    checks={"source_valid":not src,"no_duplicate_meaning_exposure":no_dup,"condition_balance":bal,"domain_balance":dom,"scoring_masked":masked,"answer_key_traceability":trace,"excluded_responses_unscored":unscored,"per_response_scoring_routes":routes_ok,"independent_scoring_route_per_question":indq,"mechanical_exclusions":mech,"preservation_failures_retained":all(x["adverse_record_retained"] and x["rule_ids"] for x in adv),"all_disposition_routes":all(x["derived"]==x["expected"] for x in routes),"small_pilot_boundary":d["synthetic_only"] and d["evidence_claim"]=="procedure_only" and d["study_state"]=="synthetic_rehearsal","ordinary_editing_can_outperform":any(x["S_worse_probability"] for x in adv),"inconclusive_case_retained":any(x["scenario_class"]=="inconclusive" for x in adv),"deviation_case_retained":bool(sc["planned_deviations"]) and all(x.get("affected_record_id") for x in sc["planned_deviations"])}
    for k,v in checks.items():add(v,k.upper(),f"operational check failed: {k}",f)
    add(s["analyzable_responses"]*2==s["initial_score_count"],"SCORE_COUNT","two scores required per analyzable response",f);add(s["raw_response_count"]-s["analyzable_responses"]==s["applied_exclusion_count"],"EXCLUSION_COUNT","raw minus analyzable must equal exclusions",f)
    return {"status":"pass" if not f else "fail","check_count":len(checks),"checks":checks,"findings":sorted(f,key=lambda x:(x["code"],x["message"]))}

def build(d):
    f=validate_source(d)
    if f:raise ValueError(f"invalid source fixture: {f}")
    a=make_assignments(d);sc=make_scoring(d,a);an=make_analysis(d,a,sc);return {"assignments.json":a,"scoring_and_adjudication.json":sc,"analysis.json":an}
def main():
    p=argparse.ArgumentParser();p.add_argument("source",type=Path);p.add_argument("--output-dir",type=Path);x=p.parse_args();d=json.loads(x.source.read_text());o=build(d)
    if x.output_dir:
        x.output_dir.mkdir(parents=True,exist_ok=True)
        for n,v in o.items():(x.output_dir/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
    r={"status":o["analysis.json"]["validation"]["status"],"fixture_id":d["fixture_id"],"output_hashes":{n:"sha256:"+digest(v) for n,v in o.items()},"summary":o["analysis.json"]["summary"],"mock_disposition":o["analysis.json"]["mock_disposition"],"synthetic_only":True,"evidence_claim":"procedure_only"};print(json.dumps(r,indent=2,sort_keys=True));return 0 if r["status"]=="pass" else 2
if __name__=="__main__":raise SystemExit(main())
