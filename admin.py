from medicine_details import Medicare, customerMedidata, Bills
from mediMgmt import MediMgmt, customerMedidata, Bills
from datetime import date


if (__name__ == "__main__"):
    medId = MediMgmt()
    medicust = MediMgmt()
    bill = MediMgmt()
    choice = 0
    chemist = "owner"
    password = "1234"
    print(''' 
                 ___________________________________________
                           Welcome to WellNess 24/7
                 ___________________________________________
           ''')
    ans = input("Are you owner or customer(o/c): ")
    if (ans == "o"):
        admin = input("Enter admin username:: ")
        pword = input("Enter admin password:: ")
        if (admin == chemist and pword == password):
            while (choice != 9):
                print("\t\t1. Add new medicine: ")
                print("\t\t2. Display all medicines: ")
                print("\t\t3. Search medicine by Id: ")
                print("\t\t4. Delete medicine by Id: ")
                print("\t\t5. Delete medicine by Name: ")
                print("\t\t6. Update the stock: ")
                print("\t\t7. Delete medicine by Expiry Date: ")
                print("\t\t8. Exit")
                choice = int(input("Enter your choice: "))
                if (choice == 1):
                    print("-------------------------------------------")
                    mid = int(input("Enter medicine Id: "))
                    mname = input("Enter medicine name: ")
                    expiry_date = input(
                        "Enter the date of expire the medicine in yyyy-mm-dd: ")
                    price = int(input("Enter price per medicine: "))
                    quantity = int(input("Enter quantity of medicine: "))
                    print("Medicine added Successfully..!!\n Keep adding..!!")
                    print("-------------------------------------------")
                    m1 = Medicare(mid, mname, expiry_date, price, quantity)
                    medId.addMedicine(m1)

                elif (choice == 2):
                    medId.mediDetails()

                elif (choice == 3):
                    mid = int(
                        input("Enter the medicine id to be check in stock: "))
                    medId.searchMedicineById(mid)
                elif (choice == 4):
                    mid = int(
                        input("Search the medicine to delete because of expiry: "))
                    medId.deleteMedicineById(mid)
                elif (choice == 5):
                    mname = input("Enter the name of medicine to be delete: ")
                    medId.deleteMedicineByName(mname)
                elif (choice == 6):
                    mid = int(input("Enter mid which u want to update stock: "))
                    count = int(
                        input("Enter the count u want to update stock: "))
                    medId.updateMedicineById(mid, count)
                elif (choice == 7):
                    medId.deleteMedicineByDate()
                elif (choice == 8):
                    print("Thank you..!! visit again..!!")

    else:
        customer = "user"
        password = "1234"
        print(''' 
                 ___________________________________________
                           Welcome to WellNess 24/7
                 ___________________________________________
           ''')
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
