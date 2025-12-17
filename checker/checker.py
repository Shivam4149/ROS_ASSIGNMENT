
import zipfile
import os
import sys
import json
import tempfile

def main(zip_path):
    report = {
        "status": "PASS",
        "errors": [],
        "warnings": []
    }

    if not zipfile.is_zipfile(zip_path):
        report["status"] = "FAIL"
        report["errors"].append("Not a valid ZIP file")
        print(json.dumps(report))
        return

    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(tmp)

        files = os.listdir(tmp)

        # handle single root folder inside zip
        if len(files) == 1 and os.path.isdir(os.path.join(tmp, files[0])):
            root = os.path.join(tmp, files[0])
        else:
            root = tmp

        root_files = os.listdir(root)

        if "package.xml" not in root_files:
            report["warnings"].append("package.xml not found")

        if "CMakeLists.txt" not in root_files:
            report["warnings"].append("CMakeLists.txt not found")

    os.makedirs("reports", exist_ok=True)
    with open("reports/report.json", "w") as fp:
        json.dump(report, fp, indent=2)

    # IMPORTANT: only JSON on stdout
    print(json.dumps(report))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({
            "status": "ERROR",
            "errors": ["Usage: python checker.py <zip_file>"]
        }))
    else:
        main(sys.argv[1])
