def main():
    shopping_list = []  # Initialize an empty list to store items

    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add item to the list
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the list
            else:
                print(f"{item} is not in the list.")
        elif choice == '3':
            print("\nShopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        elif choice == '4':
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
