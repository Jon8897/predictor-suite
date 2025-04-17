# Security Policy

## Supported Versions
The following versions of this project are currently being supported with security updates:

| Version | Supported          |
|---------|--------------------|
| 1.0.0.0 | :white_check_mark: |

## Reporting a Vulnerability
If you discover a security vulnerability in this project, we encourage you to report it responsibly using the **Bug Report** template in the **[GitHub Issues tab](../../issues/new?template=bug_report.md)**.

### How to Report via GitHub Issues
1. Go to the **Issues** tab in this repository.
2. Click on **New Issue**.
3. Select the **Bug Report** option.
4. Fill out the required information in the template.
5. Submit the issue.

### How to Report via the Terminal
You can also create an issue using the terminal with the following steps:
1. Clone the repository (if not already cloned):
   ```bash
   git clone https://github.com/<username>/<repository>.git
   cd <repository>

1. Open the `bug_report.md` template file located in `.github/ISSUE_TEMPLATE/`:
    
    ```bash
    nano .github/ISSUE_TEMPLATE/bug_report.md
    ```
    
2. Fill out the template with the details of the vulnerability, such as:
    - Description of the issue.
    - Steps to reproduce.
    - Impact of the vulnerability.
3. Commit and push the issue file to a new branch:
    
    ```bash
    git checkout -b report/vulnerability-<short-description>
    git add .github/ISSUE_TEMPLATE/bug_report.md
    git commit -m "Reported vulnerability: <short-description>"
    git push origin report/vulnerability-<short-description>
    ```
    
4. Create a pull request from the newly pushed branch via the GitHub interface and include "Bug Report" in the PR title.

## Response Time

- **Acknowledgment**: Within 2 business days.
- **Investigation and Fix**: Depending on the complexity, an update or fix will typically be released within 7-14 business days.

## Guidelines

- Avoid testing vulnerabilities in a production environment.
- Do not exploit vulnerabilities beyond what is necessary for your report.

Thank you for helping us keep this project secure!

---

### **Explanation**
- **Via GitHub Issues**: Instructions for users to use the GitHub UI and select the `bug_report.md` template.
- **Via Terminal**: Step-by-step instructions for users to fill out the `bug_report.md` file and submit it as a pull request from the terminal.

### **Steps to Implement**
1. Add this updated `SECURITY.md` file to your project.
2. Ensure the `bug_report.md` file exists in `.github/ISSUE_TEMPLATE/`.
3. Commit the changes:
   ```bash
   git add SECURITY.md
   git commit -m "Added terminal-based reporting to SECURITY.md"
   git push