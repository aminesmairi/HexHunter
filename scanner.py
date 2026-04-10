import os
import hashlib

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