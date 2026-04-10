from logo import show_logo
from menu import show_menu
from scanner import scan_file
from analyser import analyze_file

def main():
    while True:
        show_logo()
        show_menu()

        choice = input("\nChoose an option: ")

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
            print("============================\n")

        elif choice == "2":
            print("Scan folder (coming soon)")

        elif choice == "3":
            print("View last report (coming soon)")

        elif choice == "4":
            print("URL & Email Analyzer (coming soon)")

        elif choice == "5":
            print("Help / About (coming soon)")

        elif choice == "6":
            print("Exiting HexHunter...")
        break
    else:
        print("Invalid option. Try again.")

if __name__ == "__main__":
    main()