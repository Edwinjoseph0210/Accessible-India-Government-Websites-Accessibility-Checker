import subprocess
import json

class AccessibilityAuditor:
    def __init__(self, pa11y_path='pa11y'):
        self.pa11y_path = pa11y_path

    def audit_url(self, url):
        try:
            result = subprocess.run([
                self.pa11y_path, url, '--reporter', 'json'
            ], capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                print(f"Pa11y error: {result.stderr}")
                return None
        except Exception as e:
            print(f"Error auditing {url}: {e}")
            return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        auditor = AccessibilityAuditor()
        report = auditor.audit_url(sys.argv[1])
        print(json.dumps(report, indent=2))
    else:
        print("Usage: python accessibility_audit.py <url>") 