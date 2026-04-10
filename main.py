from logo import show_logo
from menu import show_menu

def main():
    while True:
        show_logo()
        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("Scan file (coming soon)")
        elif choice == "2":
            print("Scan folder (coming soon)")
        elif choice == "3":
            print("Exiting HexHunter...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()