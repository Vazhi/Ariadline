"""Synthetic evaluation dry-run generator and validator.

Structural diagnostics only. A pass is not ethics approval, permission, meaning
authority, preservation certification, preregistration, participant evidence,
or a publication decision.
"""
from __future__ import annotations
import copy, json, random, re
from collections import Counter, defaultdict
from pathlib import Path

SEED=20260728
STRATA=["PG-DESC","PG-THEORY","PG-EMP","PG-COMP","PG-EDIT"]
PUB_TASKS={"reconstruction","ambiguity","review","revision","translation","full-document"}
FORBIDDEN={"name","full_name","email","phone","address","institution","exact_location","account_id"}
PID_RE=re.compile(r"^SLE-PART-[A-Z0-9-]+$")
TID_RE=re.compile(r"^SLE-DRY-TRIAL-\d{4}$")
MASK_RE=re.compile(r"^MX\d{3}$")

def participants():
    return [{
        "participant_id":f"SLE-PART-D{i+1:03d}","study_phase":"pilot",
        "primary_stratum":STRATA[i%5],"secondary_experience":["synthetic-dry-run"],
        "career_stage_band":["advanced-student","early","mid","senior"][i%4],
        "primary_scholarly_language_band":["L1","L2","L3","protected"][i%4],
        "professional_english_use":["low","medium","high"][i%3],
        "sle_contributor":"yes" if i==0 else "no",
        "canto_span_contributor":"yes" if i in (1,11) else "no",
        "controlled_language_experience":["none","limited","regular"][i%3],
        "translation_experience":["none","limited","regular"][i%3],
        "accessibility_accommodation":"provided-synthetic" if i==7 else "none",
        "consent_state":"synthetic-not-applicable",
        "completion_state":"withdrawn" if i==19 else "complete",
        "exclusion_code":"synthetic-withdrawal" if i==19 else "none",
        "withdrawal_order_position":0 if i==19 else None,
    } for i in range(20)]

def materials():
    rows=[
      ("SLE-DRY-MAT-0001","SLE-DRY-BRIEF-0001","SYN","reconstruction","descriptive",["P","S"],["U"],"yes","no"),
      ("SLE-DRY-MAT-0002","SLE-DRY-BRIEF-0002","SYN","ambiguity","theoretical",["P","S"],[],"no","no"),
      ("SLE-DRY-MAT-0003","SLE-DRY-BRIEF-0003","SYN","review","editorial",["P","S"],[],"no","no"),
      ("SLE-DRY-MAT-0004","SLE-DRY-BRIEF-0004","SYN","revision","empirical",["P","S"],[],"no","no"),
      ("SLE-DRY-MAT-0005","SLE-DRY-BRIEF-0005","SYN","translation","multilingual",["P","S"],[],"no","no"),
      ("SLE-DRY-CS-0001","SLE-DRY-CS-BRIEF-0001","CS","reconstruction","canto-span-supplement",["P","S"],[],"no","yes"),
    ]
    return [{
      "material_id":a,"meaning_record_id":b,"material_class":c,"task_type":d,
      "domain_family":e,"required_conditions":f,"optional_conditions":g,
      "u_admissible":h,"canto_span":i,"lifecycle_state":"pilot_ready",
      "authority_state":"constructed-project-local" if i=="yes" else "constructed-brief",
      "permission_state":"synthetic-only"
    } for a,b,c,d,e,f,g,h,i in rows]

def condition_rows(mats):
    out=[]; n=1
    for m in mats:
        for c in m["required_conditions"]+m["optional_conditions"]:
            out.append({
              "condition_id":f"{m['material_id']}-{c}","material_id":m["material_id"],
              "meaning_record_id":m["meaning_record_id"],"condition":c,
              "mask_code":f"MX{n:03d}","condition_author_role":"synthetic-generator",
              "material_version":"dry-run-v0.1",
              "preservation_result":"not determined" if c=="U" else "preserved",
              "preservation_success":False if c=="U" else True,
              "independent_review_state":"synthetic-only","lifecycle_state":"pilot_ready"
            }); n+=1
    return out

def trial_rows(parts,mats,conds,seed=SEED):
    rng=random.Random(seed)
    mask={(r["material_id"],r["condition"]):r["mask_code"] for r in conds}
    core=[m for m in mats if m["canto_span"]=="no"]; out=[]; n=1
    active=[p for p in parts if p["completion_state"]!="withdrawn"]
    for pi,p in enumerate(active):
        chosen=core.copy(); rng.shuffle(chosen)
        for pos,m in enumerate(chosen[:4],1):
            c="U" if m["material_id"]=="SLE-DRY-MAT-0001" and pi%5==0 else ("P" if (pi+pos)%2==0 else "S")
            out.append({
              "trial_id":f"SLE-DRY-TRIAL-{n:04d}","participant_id":p["participant_id"],
              "material_id":m["material_id"],"meaning_record_id":m["meaning_record_id"],
              "material_version":"dry-run-v0.1","condition":c,
              "masked_condition":mask[(m["material_id"],c)],"task_type":m["task_type"],
              "domain_family":m["domain_family"],"pattern_ids":["SLE-PATTERN-0001"],
              "rule_ids":["SLE-RULE-0001","SLE-RULE-0004"],"order_position":pos,
              "response_started_at":None,"response_time_ms":30000+(pi*137+pos*211)%45000,
              "completion_state":"complete","device_band":["desktop","tablet","mobile"][pi%3],
              "accommodation_applied":p["accessibility_accommodation"]
            }); n+=1
    cs=next(m for m in mats if m["canto_span"]=="yes")
    for pi,c in ((1,"P"),(11,"S")):
        p=active[pi]
        out.append({
          "trial_id":f"SLE-DRY-TRIAL-{n:04d}","participant_id":p["participant_id"],
          "material_id":cs["material_id"],"meaning_record_id":cs["meaning_record_id"],
          "material_version":"dry-run-v0.1","condition":c,
          "masked_condition":mask[(cs["material_id"],c)],"task_type":cs["task_type"],
          "domain_family":cs["domain_family"],"pattern_ids":["SLE-PATTERN-0014"],
          "rule_ids":["SLE-RULE-0001"],"order_position":5,"response_started_at":None,
          "response_time_ms":42000+pi,"completion_state":"complete","device_band":"desktop",
          "accommodation_applied":p["accessibility_accommodation"]
        }); n+=1
    return out

def build_valid(seed=SEED):
    ps=participants(); ms=materials(); cs=condition_rows(ms); ts=trial_rows(ps,ms,cs,seed)
    responses=[{
      "response_id":f"SLE-DRY-RESP-{i:04d}","trial_id":t["trial_id"],
      "question_id":f"SLE-DRY-Q-{((i-1)%8)+1:03d}","response_type":"selected",
      "response_value":"synthetic-option-a" if i%3 else "synthetic-option-b",
      "confidence":i%5+1,"self_reported_clarity":(i+1)%5+1,
      "self_reported_burden":(i+2)%5+1,
      "not_determined_selected":"yes" if i%17==0 else "no",
      "participant_comment":"synthetic comment" if i%13==0 else ""
    } for i,t in enumerate(ts,1)]
    scoring=[]; si=1
    for i,t in enumerate(ts,1):
        for scorer in ("SLE-SCORER-D001","SLE-SCORER-D002"):
            score=1 if (i+(1 if scorer.endswith("2") else 0))%5 else 0
            scoring.append({
              "score_id":f"SLE-DRY-SCORE-{si:05d}","trial_id":t["trial_id"],
              "question_id":f"SLE-DRY-Q-{((i-1)%8)+1:03d}","scorer_id":scorer,
              "scoring_key_version":"dry-run-key-v0.1","score":score,
              "error_class":"none" if score else "minor",
              "adjudication_required":"yes" if i%5==0 else "no",
              "adjudicated_score":1 if i%5==0 else None,
              "adjudication_reason":"synthetic disagreement" if i%5==0 else "",
              "condition_masked":"yes"
            }); si+=1
    preservation=[]; pi=1
    for t in ts:
        if t["task_type"] in {"revision","translation"}:
            r="preserved" if t["condition"] in {"P","S"} else "not determined"
            preservation.append({
              "preservation_id":f"SLE-DRY-PRES-{pi:04d}","trial_id":t["trial_id"],
              "draft_version":"synthetic-output-v0.1","meaning_record_id":t["meaning_record_id"],
              "preservation_dimension":"scope","preservation_result":r,
              "severity":"not applicable" if r=="preserved" else "major",
              "independent_reviewer_id":"SLE-REVIEWER-D001",
              "source_author_confirmation":"not applicable","revision_time_ms":t["response_time_ms"]
            }); pi+=1
    findings=[{
      "finding_id":f"SLE-DRY-FIND-{i:03d}","participant_id":t["participant_id"],
      "material_id":t["material_id"],"rule_ids":t["rule_ids"],
      "finding_type":["helpful","burdensome","unclear"][i%3],
      "summary":"Synthetic dry-run finding; not participant evidence.","verbatim_quote":"",
      "domain_scope":t["domain_family"],"disposition":"task repair" if i%2 else "no action"
    } for i,t in enumerate(ts[::19],1)]
    deviations=[{
      "deviation_id":"SLE-DRY-DEV-001","date":"2026-07-28",
      "study_phase":"synthetic-dry-run","affected_participants":[],
      "affected_materials":["SLE-DRY-MAT-0003"],"affected_conditions":["P","S"],
      "affected_outcomes":["timing"],"reason":"Injected fictional interface pause for pipeline testing.",
      "outcome_data_visible":"no","corrective_action":"Retain as expected synthetic deviation.",
      "effect_on_confirmatory_status":"none-synthetic","responsible_role":"automation-test"
    }]
    return {"metadata":{
      "fixture_id":"SLE-EVAL-DRY-RUN-VALID-0.1","version":"0.1","seed":seed,
      "synthetic":True,"participant_evidence":False,"authentic_material":False,
      "registration_state":"not preregistered"},
      "participants":ps,"materials":ms,"conditions":cs,"trials":ts,
      "responses":responses,"scoring":scoring,"preservation":preservation,
      "qualitative_findings":findings,"protocol_deviations":deviations}

def build_invalid(valid):
    f=copy.deepcopy(valid); f["metadata"].update({"fixture_id":"SLE-EVAL-DRY-RUN-INVALID-0.1","expected_invalid":True})
    for p in f["participants"]: p["email"]=""
    f["participants"][0]["email"]="fictional@example.invalid"
    for p in f["participants"][:5]: p["canto_span_contributor"]="yes"
    x=copy.deepcopy(f["trials"][0]); x.update({"trial_id":"SLE-DRY-TRIAL-9001","participant_id":"SLE-PART-MISSING"}); f["trials"].append(x)
    x=copy.deepcopy(f["trials"][1]); x.update({"trial_id":"SLE-DRY-TRIAL-9002","condition":"S" if x["condition"]=="P" else "P"}); f["trials"].append(x)
    x=copy.deepcopy(next(t for t in f["trials"] if t["task_type"]=="revision")); x.update({"trial_id":"SLE-DRY-TRIAL-9003","condition":"U","masked_condition":"MX999"}); f["trials"].append(x)
    f["conditions"][0]["mask_code"]="S-CONDITION"; f["trials"][0]["masked_condition"]="S-CONDITION"
    f["conditions"]=[r for r in f["conditions"] if not(r["material_id"]=="SLE-DRY-MAT-0002" and r["condition"]=="P")]
    p=next(r for r in f["conditions"] if r["material_id"]=="SLE-DRY-MAT-0004" and r["condition"]=="P")
    p.update({"preservation_result":"not determined","preservation_success":True,"lifecycle_state":"confirmatory_ready"})
    wid=next(p["participant_id"] for p in f["participants"] if p["completion_state"]=="withdrawn")
    x=copy.deepcopy(f["trials"][2]); x.update({"trial_id":"SLE-DRY-TRIAL-9004","participant_id":wid,"order_position":1}); f["trials"].append(x)
    f["scoring"].append({"score_id":"SLE-DRY-SCORE-90001","trial_id":"SLE-DRY-TRIAL-NOT-FOUND",
      "question_id":"SLE-DRY-Q-001","scorer_id":"SLE-SCORER-D001",
      "scoring_key_version":"dry-run-key-v0.1","score":1,"error_class":"none",
      "adjudication_required":"no","adjudicated_score":None,"adjudication_reason":"",
      "condition_masked":"yes"})
    for t in f["trials"][:12]:
        t.update({"material_id":"SLE-DRY-CS-0001","meaning_record_id":"SLE-DRY-CS-BRIEF-0001","domain_family":"canto-span-supplement"})
    return f

def write_fixtures(output_dir,seed=SEED):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    valid=build_valid(seed); invalid=build_invalid(valid)
    (out/"valid_fixture.json").write_text(json.dumps(valid,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (out/"invalid_fixture.json").write_text(json.dumps(invalid,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return valid,invalid

class Finding:
    def __init__(self,code,msg,record=""): self.code,self.message,self.record=code,msg,record
    def as_dict(self): return {"code":self.code,"message":self.message,"record":self.record}

def validate(f):
    out=[]; add=lambda c,m,r="":out.append(Finding(c,m,r)); meta=f.get("metadata",{})
    if meta.get("synthetic") is not True:add("NOT_SYNTHETIC","Fixture must declare synthetic=true.")
    if meta.get("participant_evidence") is not False:add("EVIDENCE_BOUNDARY","participant_evidence must be false.")
    if meta.get("authentic_material") is not False:add("AUTHENTICITY_BOUNDARY","authentic_material must be false.")
    rows=lambda k:[r for r in f.get(k,[]) if isinstance(r,dict)]
    ps,ms,cs,ts,rs,ss,prs,qfs,ds=[rows(k) for k in ("participants","materials","conditions","trials","responses","scoring","preservation","qualitative_findings","protocol_deviations")]
    for k,v in zip(("participants","materials","conditions","trials","responses","scoring","preservation","qualitative_findings","protocol_deviations"),(ps,ms,cs,ts,rs,ss,prs,qfs,ds)):
        if not v:add("MISSING_TABLE_ROWS",f"{k} has no records.")
    pids=set()
    for p in ps:
        pid=str(p.get("participant_id",""))
        if not PID_RE.fullmatch(pid):add("INVALID_PARTICIPANT_ID","Invalid participant ID.",pid)
        if pid in pids:add("DUPLICATE_PARTICIPANT_ID","Duplicate participant ID.",pid)
        pids.add(pid)
        bad=sorted(FORBIDDEN&set(p))
        if bad:add("FORBIDDEN_IDENTIFIER_FIELD",f"Forbidden field(s): {', '.join(bad)}.",pid)
    mb={str(m.get("material_id")):m for m in ms}; meaning={k:str(v.get("meaning_record_id")) for k,v in mb.items()}
    for mid,m in mb.items():
        req=set(m.get("required_conditions",[])); opt=set(m.get("optional_conditions",[]))
        if "U" in req:add("UNIVERSAL_U_REQUIREMENT","U must not be required.",mid)
        if m.get("task_type") in PUB_TASKS and not {"P","S"}<=req:add("TASK_CONDITION_REGISTRATION","Publication task must require P and S.",mid)
        if m.get("u_admissible")!="yes" and "U" in opt:add("PROHIBITED_U_REGISTRATION","U optional only when admissible.",mid)
    bymat=defaultdict(set); masks=set()
    for c in cs:
        mid=str(c.get("material_id","")); cond=str(c.get("condition","")); bymat[mid].add(cond)
        if mid not in mb:add("BROKEN_MATERIAL_FK","Condition references missing material.",mid)
        mask=str(c.get("mask_code",""))
        if not MASK_RE.fullmatch(mask):add("MASK_LEAK","Non-opaque condition mask.",f"{mid}:{mask}")
        if mask in masks:add("DUPLICATE_MASK_CODE","Duplicate mask.",mask)
        masks.add(mask)
        if cond in {"P","S"} and c.get("lifecycle_state")=="confirmatory_ready" and c.get("preservation_result")!="preserved":
            add("PRESERVATION_NOT_CONFIRMED","Confirmatory P/S lacks preserved result.",str(c.get("condition_id","")))
        if c.get("preservation_result")=="not determined" and c.get("preservation_success") is True:
            add("NOT_DETERMINED_AS_SUCCESS","not determined cannot be success.",str(c.get("condition_id","")))
    for mid,m in mb.items():
        miss=set(m.get("required_conditions",[]))-bymat.get(mid,set())
        if miss:add("REQUIRED_CONDITION_MISSING",f"Missing: {', '.join(sorted(miss))}.",mid)
    tids=set(); seen=set(); byp=defaultdict(list); canto=0
    for t in ts:
        tid=str(t.get("trial_id","")); pid=str(t.get("participant_id","")); mid=str(t.get("material_id","")); cond=str(t.get("condition","")); mn=str(t.get("meaning_record_id",""))
        if not TID_RE.fullmatch(tid):add("INVALID_TRIAL_ID","Invalid trial ID.",tid)
        if tid in tids:add("DUPLICATE_TRIAL_ID","Duplicate trial ID.",tid)
        tids.add(tid)
        if pid not in pids:add("BROKEN_PARTICIPANT_FK","Trial references missing participant.",tid)
        if mid not in mb:add("BROKEN_MATERIAL_FK","Trial references missing material.",tid);continue
        if mn!=meaning[mid]:add("MEANING_RECORD_MISMATCH","Trial meaning does not match material.",tid)
        key=(pid,mn)
        if key in seen:add("DUPLICATE_MEANING_EXPOSURE","Multiple conditions from one meaning record.",tid)
        seen.add(key);byp[pid].append(t)
        if cond not in bymat.get(mid,set()):add("UNREGISTERED_TRIAL_CONDITION","Condition absent from register.",tid)
        if cond=="U" and mb[mid].get("u_admissible")!="yes":add("PROHIBITED_U_CONDITION","U not admissible.",tid)
        if not MASK_RE.fullmatch(str(t.get("masked_condition",""))):add("MASK_LEAK","Non-opaque trial mask.",tid)
        if mb[mid].get("canto_span")=="yes":canto+=1
    pb={str(p.get("participant_id")):p for p in ps}
    for pid,trs in byp.items():
        p=pb.get(pid)
        if p and p.get("completion_state")=="withdrawn":
            w=p.get("withdrawal_order_position")
            for t in trs:
                if w is None or (isinstance(w,int) and isinstance(t.get("order_position"),int) and t["order_position"]>w):
                    add("POST_WITHDRAWAL_TRIAL","Post-withdrawal trial.",str(t.get("trial_id","")))
    cc=sum(p.get("canto_span_contributor")=="yes" for p in ps)
    if ps and cc/len(ps)>.10:add("CANTO_PARTICIPANT_CAP",f"{cc}/{len(ps)} above 10%.")
    if ts and canto/len(ts)>.10:add("CANTO_TRIAL_CAP",f"{canto}/{len(ts)} above 10%.")
    for r in rs:
        if str(r.get("trial_id","")) not in tids:add("BROKEN_TRIAL_FK","Response references missing trial.",str(r.get("trial_id","")))
    for s in ss:
        tid=str(s.get("trial_id",""))
        if tid not in tids:add("BROKEN_TRIAL_FK","Scoring references missing trial.",tid)
        if s.get("condition_masked")!="yes":add("SCORING_UNMASKED","Score not masked.",tid)
    for p in prs:
        tid=str(p.get("trial_id",""))
        if tid not in tids:add("BROKEN_TRIAL_FK","Preservation references missing trial.",tid)
        if p.get("preservation_result")=="not determined" and p.get("severity") in {"not applicable","editorial"}:
            add("NOT_DETERMINED_DOWNGRADED","not determined paired with non-material severity.",str(p.get("preservation_id","")))
    for q in qfs:
        pid=str(q.get("participant_id",""))
        if pid and pid not in pids:add("BROKEN_PARTICIPANT_FK","Finding references missing participant.",pid)
    for did,n in Counter(str(d.get("deviation_id","")) for d in ds).items():
        if n>1:add("DUPLICATE_DEVIATION_ID","Duplicate deviation ID.",did)
    return out
