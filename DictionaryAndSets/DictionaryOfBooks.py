books = {}

while True:
    choice = input("\n1. Add 2. Remove 3. Search 4. Display 5. Exit\nChoose: ")

    if choice == '1':
        books[input("Title: ")] = input("Author: ")
    elif choice == '2':
        books.pop(input("Title: "), print("Not found!"))
    elif choice == '3':
        title = input("Title: ")
        print(f'{title} by {books.get(title, "Not found!")}')
    elif choice == '4':
        print("\n".join(f'{t} by {a}' for t, a in books.items()) or "No books available!")
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

print(books)