phone_book = {'Amal': '1111111111',
              'Mohamed': '2222222222',
              'Khadijah':'3333333333',
              'Abdullah':'4444444444',
              'Rawan':'5555555555',
              'Faisal':'6666666666',
              'Layla':'7777777777'}

def find_by_name(name):
    if name in phone_book:
        return phone_book[name]
    else:
        return "Sorry, the number is not found"

def find_by_number(number):
    for name,num in phone_book.items():
        if num == number:
            return name
    return "Sorry, the number is not found"

def main():
    while True:
        choice = input("Enter '1' to search by name, '2' to search by number, or '3' to add a new contact: ")
        
        if choice == '1':
            name = input("Enter the name: ")
            result = find_by_name(name)
            print(result)
        elif choice == '2':
            number = input("Enter the number: ")
            result = find_by_number(number)
            print(result)
        elif choice == '3':
            name = input("Enter the name: ")
            number = input("Enter the number: ")
            phone_book[name] = number
            print("Contact added successfully!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()