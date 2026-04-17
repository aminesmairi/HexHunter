from logo import show_logo
from menu import show_menu
from scanner import scan_file, scan_folder
from analyser import analyze_file
from reporter import save_report


def main():

    # Ask once at start (Option B design)
    save_reports = input("Enable report saving? (y/n): ").lower() == "y"

    while True:
        show_logo()
        show_menu()

        choice = input("\nChoose an option: ")

        # ---------------- OPTION 1 ----------------
        if choice == "1":
            path = input("\nEnter full file path: ")
            result = scan_file(path)

            print("\n===== HEXHUNTER REPORT =====")

            if "error" in result:
                print("ERROR:", result["error"])
            else:
                print("File:", result["file_path"])
                print("Size:", result["size_bytes"], "bytes")
                print("SHA256:", result["sha256"])

                analysis = analyze_file(path)

                print("Risk Level:", analysis["risk"])
                print("Score:", analysis["score"])

                if len(analysis["reasons"]) > 0:
                    print("Reasons:")
                    for reason in analysis["reasons"]:
                        print("-", reason)
                else:
                    print("No suspicious indicators found.")

                # (Optional future: file report saving)
                if save_reports:
                    print("\nSingle file report saving not implemented yet.")

            if save_reports:
                report_file = save_report({
                    "files": [{
                        "file": result["file_path"],
                        "risk": analysis["risk"],
                        "score": analysis["score"]
                    }],
                    "summary": {
                        "total": 1,
                        "low": 1 if analysis["risk"] == "LOW" else 0,
                        "medium": 1 if analysis["risk"] == "MEDIUM" else 0,
                        "high": 1 if analysis["risk"] == "HIGH" else 0
                    }
                }, path)

                print(f"\nReport saved as: {report_file}")

            print("============================\n")

        # ---------------- OPTION 2 ----------------
        elif choice == "2":
            folder = input("\nEnter folder path: ")

            results = scan_folder(folder)

            print("\n===== HEXHUNTER FOLDER SCAN =====")

            if "error" in results:
                print("ERROR:", results["error"])
            else:
                for file in results["files"]:
                    print(f"\nFile: {file['file']}")
                    print(f"Risk: {file['risk']} | Score: {file['score']}")

                # SUMMARY
                summary = results["summary"]

                print("\n----- SCAN SUMMARY -----")
                print(f"Total Files: {summary['total']}")
                print(f"Low Risk: {summary['low']}")
                print(f"Medium Risk: {summary['medium']}")
                print(f"High Risk: {summary['high']}")

                # Save report if enabled
                if save_reports:
                    report_file = save_report(results, folder)
                    print(f"\nReport saved as: {report_file}")

            print("\n===============================\n")

        # ---------------- OPTION 3 ----------------
        elif choice == "3":
            print("\nNo saved reports found.\n")

        # ---------------- OPTION 4 ----------------
        elif choice == "4":
            print("URL & Email Analyzer (coming soon)")

        # ---------------- OPTION 5 ----------------
        elif choice == "5":
            print("Help / About (coming soon)")

        # ---------------- OPTION 6 ----------------
        elif choice == "6":
            print("Exiting HexHunter...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()