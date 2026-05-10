filename = "dreams.txt"

def read_messages():
    try:
        with open(filename, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("\nEmpty Lagyan mo ngani.\n")
            else:
                print("\n--- Motivational Quotes---")
                print(content)
                print("--------------------------\n")
    except FileNotFoundError:
        print("\nWala di makita. A new one will be created when you add a message.\n")

def add_message():
    message = input("\nEnter a new Quotes: ")
    with open(filename, "a") as file:
        file.write(message + "\n")
    print("Message added!\n")

def rewrite_file():
    confirm = input("\nAre you sure you want to rewrite the entire file? (yes/nah): ")
    if confirm.lower() == "yes":
        with open(filename, "w") as file:
            print("Enter new quotes (type 'done' to finish):")
            while True:
                msg = input("> ")
                if msg.lower() == "done":
                    break
                file.write(msg + "\n")
        print("File rewritten!\n")
    else:
        print("Rewrite cancelled.\n")

while True:
    print("===== Dreams.txt Menu =====")
    print("1. Read motivation quotes")
    print("2. Add a new quotes")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("Choose an option(1-4): ")

    if choice == "1":
        read_messages()
    elif choice == "2":
        add_message()
    elif choice == "3":
        rewrite_file()
    elif choice == "4":
        print("Exiting program... Sayonara!")
        break
    else:
        print("Nobody's Perfect. Please select 1-4.\n")
