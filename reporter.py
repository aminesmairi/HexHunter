import os
from datetime import datetime

def save_report(scan_data, folder_path):
    # Create reports folder if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/HexHunter_Report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("===== HEXHUNTER SCAN REPORT =====\n\n")
        f.write(f"Folder: {folder_path}\n")
        f.write(f"Date: {timestamp}\n\n")

        for file in scan_data["files"]:
            f.write(f"File: {file['file']}\n")
            f.write(f"Risk: {file['risk']} | Score: {file['score']}\n\n")

        summary = scan_data["summary"]

        f.write("----- SUMMARY -----\n")
        f.write(f"Total Files: {summary['total']}\n")
        f.write(f"Low Risk: {summary['low']}\n")
        f.write(f"Medium Risk: {summary['medium']}\n")
        f.write(f"High Risk: {summary['high']}\n")

    return filename