import Dictionaries.dicts as dicts
import Lists.lists as lists
import sys

sys.path.append('Lists')
sys.path.append('Dictionaries')

def main():
    print("Choose a topic:")
    print("1. Lists")
    print("2. Dictionaries")
    print("3. Exit")
    choice = int(input("Your choice: "))
    try:
        if choice == 1:
            lists.main()
        elif choice == 2:
            dicts.main()
        elif choice == 3:
            sys.exit()
        else:
            print("Invalid choice!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        main()
        print()
        input("Press Enter to continue...")
        print()