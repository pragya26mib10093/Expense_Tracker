# Expense Tracker Project

expenses = [] # list of expenses in form of dictionary

print(" Welcome to Expense Tracker ")

while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. view Total Spend")
    print("4. Exit")


    choice=int(input("Please Enter Your Choice : "))

    
 # Add Expense   
    if(choice ==1):
        date=input("Enter The Date : ")
        category=input("Enter The Category (food,travel,books) : ")
        discription=input("Give more Detail : ")
        amount=eval(input("Enter The Amount Spend : "))

        expense={
            "date" : date,
            "category" : category,
            "discription" : discription,
            "amount" : amount,


        }

        expenses.append(expense)
        print(" \n DONE ,Expense in added succesfully")

#2. View all Expenses
    elif(choice ==2):
        if( len(expenses)==0 ):
            print("No Expenses Added")
        else:
            print("=====This is Your Expense=====")
            count=1
            for eachspend in expenses:
                print(f"Spend number {count} -> {eachspend["date"]}, {eachspend["category"]}, {eachspend["discription"]}, {eachspend["amount"]} ")
                count= count+1

#3. View Total spending
    elif(choice ==3):
        total=0
        for eachspend in expenses:
            total = total + eachspend["amount"]

        print("\n Total spend = ", total)

#4. exit
    elif(choice ==4):
        print("Thankyou for using our system")
        break

    else:
        print("Invalid Choice. Try Again")







