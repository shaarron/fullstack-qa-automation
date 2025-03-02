import pytest
import logging
import os
from datetime import datetime
import sys

if __name__ == "__main__":
    test_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_directory)
    print(f"🔍 Running tests from directory: {test_directory}")

    allure_results_dir = "allure-results"
    os.makedirs(allure_results_dir, exist_ok=True)

    pytest_args = [
        "-s",
        "-v",
        "--log-cli-level=INFO",
        "--tb=short",
        "--alluredir=allure-results",
        "test_cases"
    ]

    exit_code = pytest.main(pytest_args)

    if exit_code == 0:
        print("✅ All tests PASSED successfully!")
    else:
        print(f"❌ Some tests FAILED. Exit code: {exit_code}")

    print("📊 Generating Allure Report...")
    print("📌 Allure Report generated successfully! Run `allure open allure-report` to view.")
    sys.exit(exit_code)
