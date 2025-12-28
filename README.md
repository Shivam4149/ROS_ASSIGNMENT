- ROS Code Checker and Simulation Preview Too

-  Overview
This project implements a ROS/ROS2 code validation tool** with a minimal web interface.  
The goal of the assignment is to design a tool, not a full robotic system.

The system allows a user to:
- Upload a ROS package as a ZIP file
- Validate its structure and basic correctness
- View a structured JSON report
- Trigger a minimal simulation preview

The focus is on **tool design, validation logic, workflow, and documentation.

- Project Structure
ROS_ASSIGNMENT/
├─ checker/
│ ├─ checker.py
│ └─ reports/
├─ web/
│ ├─ app.py
│ └─ templates/
│ ├─ upload.html
│ └─ report.html
├─ simulator/
│ └─ simulate.py
├─ test_packages/
│ ├─ test_pkg.zip
│ └─ faulty_pkg.zip
└─ README.md



 1. Code Checker
 Purpose
The code checker validates ROS/ROS2 packages provided as ZIP files and reports structural issues in a structured way.

Checks Performed
- Valid ZIP file check
- Safe extraction of ZIP contents
- Detection of single-root-folder ZIPs
- ROS structure validation:
  - `package.xml`
  - `CMakeLists.txt`
- Clear separation of **errors** and **warnings**
- JSON-based reporting

 Output
- JSON printed to standard output
- JSON report saved to `checker/reports/report.json`

 Example (Valid Package)
```json
{
  "status": "PASS",
  "errors": [],
  "warnings": []
}
{
  "status": "PASS",
  "errors": [],
  "warnings": [
    "package.xml not found",
    "CMakeLists.txt not found"
  ]
}

2. Web Interface
Purpose
The web interface provides a simple UI to interact with the checker.

- Features
Upload ROS package ZIP
Run checker internally
Display JSON report in browser
Handle malformed output safely

- Technology
Python Flask
HTML (Flask templates)

- How It Works
User uploads a ZIP file
File is saved to uploads/
Checker is executed via subprocess
JSON output is parsed and displayed


3. Simulation Module (Minimal)
Purpose
The simulation module demonstrates the post-validation workflow.
Description
Triggered after code validation
Copies existing screenshots or generates mock frames
Produces simulation_report.json
No full ROS, IK, or controller implementation
Rationale
The assignment prioritizes tool workflow over robotic complexity.
Hence, simulation is kept minimal and demonstrative.

4. Test Packages
Two test packages are included to demonstrate validation behavior.

4.1 Valid Package — test_pkg.zip
Contains:
package.xml
CMakeLists.txt
Python script

{
  "status": "PASS",
  "errors": [],
  "warnings": []
}

4.2 Faulty Package — faulty_pkg.zip
Contains:
Missing ROS metadata files
Python file with syntax error
Result:
{
  "status": "PASS",
  "errors": [],
  "warnings": [
    "package.xml not found",
    "CMakeLists.txt not found"
  ]
}


5. How to Run
5.1 Run Web Interface
cd ROS_ASSIGNMENT/web
python app.py

Open browser:
http://localhost:5000

5.2 Test Packages
Upload test_pkg.zip → PASS
Upload faulty_pkg.zip → WARNINGS / FAIL


6. Demo Video
https://drive.google.com/file/d/1OpiiPS2LJzXuyuFD9rUSPGj8Ax7fo9QY/view?usp=sharing
