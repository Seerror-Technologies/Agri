# Starter issues to create

Below are 12 small, ready-to-create GitHub issues for the public demo repo. Each is intentionally scoped small so new contributors can pick them up quickly.

1) Improve README run instructions

- Clarify the "Run the demo locally" steps with exact commands for Windows, macOS, and Linux.
- Add a short troubleshooting section (common errors and fixes).

Deliverable: updated `README.md`
Labels: `good first issue`, `docs`

2) Add example curl command for /parse-practice

- Add one `curl` example showing request and expected JSON response for `/parse-practice`.
- Include examples for Linux/macOS and Windows (PowerShell).

Deliverable: README update with curl snippet
Labels: `good first issue`, `docs`

3) Add unit test for simple_parse

- Add a pytest `tests/test_parse.py` with 3 assertions validating date normalization, crop detection, and `practice_type`.
- Use only synthetic inputs from `examples/synthetic/`.

Deliverable: `tests/test_parse.py`
Labels: `good first issue`, `tests`

4) Create GitHub Actions workflow to run tests

- Add `.github/workflows/ci.yml` to run Python tests on push/PR using `python -m pytest`.
- Use Python 3.9+ matrix and cache pip.

Deliverable: CI workflow file
Labels: `help wanted`, `ci`

5) Improve mock-server logging for demo

- Add structured or clearer logging to `mock-server/app.py` (timestamped, level).
- Update README with how to view logs in Docker/container.

Deliverable: logging change + README note
Labels: `good first issue`

6) Add Dockerfile for mock server

- Create a `Dockerfile` that packages the mock server and a `docker-compose.yml` to run mock server + example.
- Include instructions to build and run in README.

Deliverable: `Dockerfile` and `docker-compose.yml`
Labels: `help wanted`, `docker`

7) Add example SDK usage in README

- Expand `sdk/python/example_run.py` to read `examples/synthetic/practice_logs.csv` and parse each line, printing results.
- Add corresponding example usage and commands in README.

Deliverable: updated `example_run.py` + README snippet
Labels: `good first issue`, `docs`

8) Add lint config & pre-commit

- Add `.pre-commit-config.yaml` with hooks: `black`, `isort`, and `detect-secrets`.
- Add minimal `pyproject.toml` or config for formatting if needed.

Deliverable: pre-commit config and setup instructions
Labels: `help wanted`, `tooling`

9) Create synthetic data README

- Document how `tools/generate_synthetic_data.py` works and how to customize the generator parameters (n, crops, farmers).
- Add examples and sample outputs path.

Deliverable: `docs/synthetic-data.md`
Labels: `good first issue`, `docs`

10) Add CONTRIBUTING quick-checklist badge to README

- Add a link/badge near top of `README.md` pointing to `CONTRIBUTING.md`.
- Add a one-line "How to start" checklist (run demo → pick issue → open PR).

Deliverable: README update
Labels: `good first issue`, `docs`

11) Add code of conduct file

- Add `CODE_OF_CONDUCT.md` with Contributor Covenant summary and contact email.

Deliverable: `CODE_OF_CONDUCT.md`
Labels: `good first issue`, `docs`

12) Create minimal TypeScript client example

- Add `sdk/js/example.ts` that calls the mock server `/parse-practice` endpoint and prints the response.
- Include build/run instructions in README.

Deliverable: `sdk/js/example.ts` + README note
Labels: `help wanted`, `enhancement`

---

How to use: open each issue in GitHub Issues and paste the corresponding title/body. Keep labels as suggested to help triage.
