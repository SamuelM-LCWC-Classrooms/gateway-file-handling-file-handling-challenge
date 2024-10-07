import json
def task_1():
    with open("task_1.txt", "r") as file:
        lines = file.readlines()
    
    total_sum = sum(int(line.strip()) for line in lines)
    return total_sum

def task_2():
    money = 0.00
    continue_order = True
    while continue_order:
        user_choice = input("What is your choice? \n").strip()
        with open("menu.csv", "r") as file:
            for record in file:
                data = record.strip().split(",")
                if data == user_choice:
                    money += float(data)
                    print("Current Price:", money)
                    break
                else:
                    print("Item not found. Please try again.")
        
        user_continue = input("Would you like to add anything to your order? (Yes or No) \n").strip().lower()
        if user_continue != "yes":
            continue_order = False
    return money

def task_3():
    name = input('Enter the name of the person you want the details of: ')
    with open('contacts.json', 'r') as file:
        data = json.load(file)
        if name in data:
            phone = data[name]['phone']
            email = data[name]['email']
            return f"Number: {phone}, Email: {email}"
        else:
            print(f"User not found.")