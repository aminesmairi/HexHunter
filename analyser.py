import os

# Suspicious file extensions
SUSPICIOUS_EXTENSIONS = [".exe", ".bat", ".cmd", ".ps1", ".vbs"]

# Suspicious keywords (for scripts/text files)
SUSPICIOUS_KEYWORDS = [
    "eval", "exec", "system", "subprocess",
    "powershell", "cmd.exe", "bash",
    "socket", "connect", "import os"
]

def analyze_file(file_path):
    risk_score = 0
    reasons = []

    # Check file extension
    _, ext = os.path.splitext(file_path)
    if ext.lower() in SUSPICIOUS_EXTENSIONS:
        risk_score += 1
        reasons.append(f"Suspicious file extension: {ext}")

    # Try reading file content (only for text-based files)
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read().lower()

            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in content:
                    risk_score += 1
                    reasons.append(f"Suspicious keyword found: {keyword}")

    except:
        pass  # Ignore binary files

    # Determine risk level based on score
    if risk_score == 0:
        risk_level = "LOW"
    elif risk_score <= 2:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return {
        "risk": risk_level,
        "score": risk_score,
        "reasons": reasons
    }