import subprocess
import sys


def run_tests():
    print("\n[] Running unit tests with pytest...\n")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--maxfail=3", "--disable-warnings", "-v"],
        text=True,
    )

    if result.returncode == 0:
        print("\n All tests passed successfully.")
    else:
        print("\n Some tests failed. Check the output above.")


if __name__ == "__main__":
    run_tests()
