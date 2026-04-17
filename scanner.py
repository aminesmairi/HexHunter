import os
import hashlib
from analyser import analyze_file

def scan_file(file_path):
    try:
        if not os.path.exists(file_path):
            return {"error": "File not found"}

        if not os.path.isfile(file_path):
            return {"error": "This is not a file"}

        file_size = os.path.getsize(file_path)

        sha256 = hashlib.sha256()

        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return {
            "file_path": file_path,
            "size_bytes": file_size,
            "sha256": sha256.hexdigest()
        }

    except Exception as e:
        return {"error": str(e)}
    
from analyser import analyze_file
import os

def scan_folder(folder_path):
    results = []

    if not os.path.exists(folder_path):
        return {"error": "Folder not found"}

    if not os.path.isdir(folder_path):
        return {"error": "This is not a folder"}

    total_files = 0
    low = 0
    medium = 0
    high = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            total_files += 1

            scan_result = scan_file(full_path)

            if "error" not in scan_result:
                analysis = analyze_file(full_path)

                risk = analysis["risk"]

                if risk == "LOW":
                    low += 1
                elif risk == "MEDIUM":
                    medium += 1
                elif risk == "HIGH":
                    high += 1

                results.append({
                    "file": full_path,
                    "risk": risk,
                    "score": analysis["score"]
                })

    return {
        "files": results,
        "summary": {
            "total": total_files,
            "low": low,
            "medium": medium,
            "high": high
        }
    }