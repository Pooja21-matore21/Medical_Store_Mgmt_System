from medicine_details import Medicare, customerMedidata, Bills
from mediMgmt import MediMgmt, customerMedidata, Bills
from datetime import date
if (__name__ == "__main__"):
    medicust = MediMgmt()
    bill = MediMgmt()
    choice = 0
    customer = "user"
    password = "1234"
    print(''' 
                 ___________________________________________
                           Welcome to WellNess 24/7
                 ___________________________________________
           ''')
    ans = input("Are you owner or customer(o/c): ")
    if (ans == "c"):
        user = input("Enter customer username:: ")
        pword = input("Enter customer password:: ")
        if (user == customer and pword == password):
            while (choice != 4):
                print("\t\t1. Show all medicines")
                print("\t\t2. Add To Cart")
                print("\t\t3. Buy Now")
                print("\t\t4. Exit")
                choice = int(input("Enter your choice: "))

                if (choice == 1):
                    medicust.showAllMedicines()

                elif (choice == 2):
                    medicust.addToCart()
                elif (choice == 3):
                    bill.buyNow1()
                elif (choice == 4):
                    print("Thank you for visiting us..!!")
