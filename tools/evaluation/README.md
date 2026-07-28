# Evaluation dry-run tools

These optional Python tools exercise the synthetic evaluation-operations fixture for issue #36.

They use only the standard library and require Python 3.10 or later.

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

Expected: all required invalid codes are detected.

## Boundary

These tools cannot approve research, identify legitimate meaning authority, certify preservation, preregister a study, recruit participants, or support a publication disposition.
