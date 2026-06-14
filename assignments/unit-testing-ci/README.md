# 📘 Assignment: Unit Testing & Local CI with pytest

## 🎯 Objective

Learn how to write unit tests using `pytest`, create a simple local test runner, and understand the basics of a CI workflow for Python projects.

## 📝 Tasks

### 🛠️ Add tests for the provided `starter-code.py`

#### Description
Use `pytest` to write unit tests that validate the behavior of functions in `starter-code.py`. Provide clear assertions, test edge cases, and include a small shell script `run_tests.sh` that runs the test suite locally.

#### Requirements
Completed assignment should:

- Include a `tests/` folder with `pytest` test files covering each public function in `starter-code.py`.
- Provide a `run_tests.sh` script that installs test dependencies and runs the test suite.
- Use meaningful test names and include at least one test for an expected failure (e.g., division by zero).
- Optionally include a sample GitHub Actions workflow file (`.github/workflows/ci.yaml`) as a reference for CI.

#### Example test run

```bash
./run_tests.sh
```

You should see `pytest` output showing tests passing.

### ✨ Optional Enhancements

- Add code coverage measurement with `coverage` or `pytest-cov`.
- Add a GitHub Actions workflow (`.github/workflows/ci-python-tests.yml`) that runs the test script on push.

Starter code: `starter-code.py` — write tests in `tests/test_starter.py` and run with `run_tests.sh`.
