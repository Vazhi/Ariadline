# Evaluation Dry-Run Tool Instructions

These optional Python tools exercise the synthetic evaluation-operations fixture for issue #36.

They use only the standard library and require Python 3.10 or later.

## Implementation layers

- `dry_run_common.py` provides the original fixture and structural-check primitives.
- `dry_run_reviewed.py` is the reviewed controlling layer. It provides balanced assignments, exact registered-mask checks, and the complete negative-code manifest.
- `generate_dry_run.py` and `validate_dry_run.py` are the supported entry points.

Do not call the base module directly when recording a package self-test.

## Generate

```bash
python3 tools/evaluation/generate_dry_run.py
```

This writes:

- `fixtures/evaluation-dry-run/v0.1/valid_fixture.json`
- `fixtures/evaluation-dry-run/v0.1/invalid_fixture.json`
- `fixtures/evaluation-dry-run/v0.1/expected_invalid_codes.json`

The default seed is `20260728`.

## Validate the valid fixture

```bash
python3 tools/evaluation/validate_dry_run.py \
  fixtures/evaluation-dry-run/v0.1/valid_fixture.json
```

Expected: `PASS` with zero findings.

## Validate expected failures

```bash
python3 tools/evaluation/validate_dry_run.py \
  fixtures/evaluation-dry-run/v0.1/invalid_fixture.json \
  --expect-codes fixtures/evaluation-dry-run/v0.1/expected_invalid_codes.json
```

Expected:

- all 34 listed validation classes are detected;
- no listed class is missing;
- no unlisted class appears;
- the command exits with status 0 only when the actual and expected code sets match exactly.

## Reproducibility record

Record the seed, reviewed-layer commit, generated-file hashes, Python version, and command exit statuses. A seed change creates a new assignment version.

## Boundary

These tools cannot approve research, identify legitimate meaning authority, certify preservation, preregister a study, recruit participants, or support a publication disposition.
