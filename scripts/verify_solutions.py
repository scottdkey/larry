"""Run every exercise's tests against its reference solution."""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    failed = []
    for sol in sorted((ROOT / "solutions").iterdir()):
        ex = ROOT / "exercises" / sol.name
        if not sol.is_dir() or not ex.is_dir():
            continue
        with tempfile.TemporaryDirectory() as tmp:
            for src in (*ex.glob("test_*.py"), *sol.glob("*.py")):
                shutil.copy(src, tmp)
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", tmp],
                capture_output=True,
                text=True,
            )
        status = "ok" if result.returncode == 0 else "FAIL"
        print(f"{status:4} {sol.name}")
        if result.returncode:
            failed.append(sol.name)
            print(result.stdout[-2000:])
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
