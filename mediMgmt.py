from medicine_details import Medicare, customerMedidata, Bills
from datetime import date
from datetime import datetime


class MediMgmt:
    def addMedicine(self, m1):
        with open("mediData.txt", "a") as fp:
            fp.write(str(m1))
            fp.write("\n")

    def mediDetails(self):
        try:
            with open("mediData.txt", "r") as fp:
                data = fp.read()
                print(data)
        except FileNotFoundError:
            print("File does not found")

    def searchMedicineById(self, mid):
        try:
            with open("mediData.txt", "r") as fp:
                for x in fp:
                    x = x.split(",")
                    # print(x)
                    if (mid == int(x[0])):
                        print("Medicine is in stock..!!")
                        print(x)
                        # print(x[0])
                        # print(x[1])
                        # print(x[2])
                        break
                else:
                    print("Searched medicine is currently out of stock..!!")
        except FileNotFoundError:
            print("File does not found")

    def deleteMedicineById(self, mid):
        try:
            allMedi = []

            found = False
            with open("mediData.txt", "r") as fp:
                for medi in fp:
                    medi = medi.split(",")
                    if (mid == int(medi[0])):
                        print("Medicine is removed as it expiered\n")
                        found = True
                    else:
                        allMedi.append(medi)
                        print(allMedi)
        except FileNotFoundError:
            print("MEdicine not found")

        if (found):
            with open("mediData.txt", "w") as fp:
                for mediData in allMedi:
                    mediData = ",".join(mediData)
                    fp.write(mediData)

    def deleteMedicineByName(self, mname):
        try:
            allMedi = []

            found = False
            with open("mediData.txt", "r") as fp:
                for medi in fp:
                    medi = medi.split(",")
                    if (mname == medi[1]):
                        print("Medicine is removed as it expiered\n")
                        found = True
                    else:
                        allMedi.append(medi)
                        print(allMedi)
        except FileNotFoundError:
            print("MEdicine not found")

        if (found):
            with open("mediData.txt", "w") as fp:
                for mediData in allMedi:
                    mediData = ",".join(mediData)
                    fp.write(mediData)

    def updateMedicineById(self, mid, count):
        try:
            allMedi = []
            found = False
            with open("mediData.txt", "r") as fp:
                for medi in fp:
                    medi = medi.split(",")
                    if (mid == int(medi[0]) and int(medi[4]) <= count):
                        n = int(medi[4]) + count
                        medi[4] = str(n)
                        print(medi[4])
                        found = True
                    allMedi.append(medi)
                print("Medicine is updated successfully..!!\n")

        except FileNotFoundError:
            print("File does not found")
        if (found):
            with open("mediData.txt", "w") as fp:
                for mediData in allMedi:
                    mediData = ",".join(mediData)
                    fp.write(mediData)
                    # fp.write("\n")

    def deleteMedicineByDate(self):
        try:
            allMedi = []
            found = False
            # mid = int(input("enter id: "))

            today_date = input("Enter today date: ")
            with open("mediData.txt", "r") as fp:
                for medi in fp:
                    medi = medi.split(",")
                    # print(medi[2])
                    if (medi[2] <= today_date):
                        print("expiry date of medicines are deleted..!!\n ")
                        found = True
                else:
                    print("hello")
                    allMedi.append(medi)
                        #print(allMedi)
                    print("This medicine is not expire..!!")

        except FileNotFoundError:
            print("MEdicine not found..!! \n Please update the stock...!!")

        if (found == True):
            with open("mediData.txt", "w") as fp:
                for mediData in allMedi:
                    mediData = ",".join(mediData)
                    fp.write(mediData)

# Customer Data

    def showAllMedicines(self):
        try:
            found = False
            allMedi = []

            with open("mediData.txt", "r") as fp:
                data = fp.read()
                print(data)
                found = True

        except FileNotFoundError:
            print("File does not found")
        if (found == True):
            with open("medi_cart.txt", "w") as fp:
                for x in data:
                    x = ",".join(x)
                    fp.write(x)

    def addToCart(self):
        ans = input("Do u ish to buy medicine..?(y/n): ")
        if (ans == "y"):
            print("Please proceed with your order..")
            medi_ord = int(input("How many types of medicine u want: "))
            for ord in range(1, medi_ord+1):
                mid = int(input("Enter medicine id: "))
                cnt = int(input("Enter no of medicines u want to buy: "))

                with open("mediData.txt", "r") as mp:
                    for y in mp:
                        y = y.split(",")
                        if (mid == int(y[0]) and cnt <= int(y[4])):
                            m3 = customerMedidata(mid, cnt)
                            with open("cust_cart.txt", "a") as fpp:
                                fpp.write(str(m3))
                                fpp.write("\n")
                            print("Order confirm..!!")
                            break
                    else:
                        print("Not available")
        else:
            print("Take Care..!!\nStay Healthy..!! Stay Safe")

    def buyMediNow(self):
        allMedi = []
        with open("mediData.txt", "r") as fp:
            for i in fp:
                i = i.split(",")
                allMedi.append(i)

        with open("cust_cart.txt", "r") as fp1:
            for buy in fp1:
                buy = buy.split(",")
                for medi in allMedi:
                    if (buy[0] == medi[0]):
                        # print("found")
                        medi[4] = str(int(medi[4])-int(buy[1]))
                        medi[4] += "\n"
        print(allMedi)
        with open("mediData.txt", "w") as fp:
            for medi in allMedi:
                medi = ",".join(medi)
                fp.write(medi)

    def buyNow1(self):
        try:
            price = 0
            with open("cust_cart.txt", "r") as fp:
                for i in fp:
                    i = i.split(",")
                    mid = int(i[0])
                    # print(mid)
                    count = int(i[1])
                    # print(count)
                    with open("mediData.txt", "r") as fp:
                        for y in fp:
                            y = y.split(",")
                            # print("success")
                            if (mid == int(y[0])):
                                # print("succs1")
                                medinm = y[1]
                                total = int(y[3]) * count
                                total += price
                                # print(total)
                                with open("bill.txt", "a") as fp:
                                    m3 = Bills(mid, medinm, count, total)
                                    fp.write(str(m3))
                                    fp.write("\n")

                with open("bill.txt", "r") as ffp:
                    for M in ffp:
                        M = M.split(",")
                        price += int(M[3])
                        print("*---*Wellness 24/7*---*")
                        print("-----------------------------------------------")
                        print(
                            "|Medicine Id| Medicine Name | medicine Quantity|Medicine Price|")
                        print("|", M[0], "|", M[1],
                              "|", M[2], "|", M[3], "|")
                        print("-----------------------------------------------")

                    else:

                        print("Your final bill is: ", price)

                        print("Thank you for visiting us..!!")
            self.buyMediNow()
        except FileNotFoundError:
            print("Sorry for inconvenience..\n medicine is not available right now..")

        else:
            with open("cust_cart.txt", "w") as fpp:
                fpp.write("")
            with open("bill.txt", "r") as fp:
                data = fp.read()
            with open("billrecords.txt", "a") as fp:
                fp.write(data)
                fp.write("\n")
            with open("bill.txt", "w") as fp:
                fp.write("")
