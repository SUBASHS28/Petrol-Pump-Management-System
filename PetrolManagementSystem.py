#creating variables:
import datetime
print("____________________________________________________________________________")
print("")
print("\t     $$$$ PETROL BUNK MANAGEMENT SYSTEM $$$$")
pet=1000
die=1000
petpri=100.0
diepri=100.0
empid=["1001","1002","1003"]
empname=["DHONI","ROHIT","KL.RAHUL"]
empage=["32","28","30"]
empaddr=["Chennai","Mumbai","Punjab"]
empphno=["9908789652","8974524367","8897436280"]
vno=["TN 33 AA 1020","TN 33 BB 2030","TN 33 CC 3040"]
par=["PETROL","DIESEL","PETROL"]
vol=["4","10","6"]
amt=["400.0","1000.0","600.0"]
dte=["November 12, 2019","November 12, 2019","November 12, 2019"]

while(1):
#program:
    print("       ~~~~~~~~~~ Welcome to the  MSD's Petrol Bunk ~~~~~~~~~~")
    print("____________________________________________________________________________")
    print("\n")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  1  |  View Stocks               |")
    print("\t\t\t ----------------------------------")

    print("\t\t\t|  2  |  View Prices               |")  
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  3  |  View Sales                |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  4  |  Update Petrol Price       |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  5  |  Update Diesel Price       |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  6  |  Petrol Purchase           |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  7  |  Diesel Purchase           |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  8  |  Bill Entry                |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  9  |  Add New Employee          |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  10 |  View Employee Details     |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  11 |  Delete Employee           |")
    print("\t\t\t ----------------------------------")
    print("\t\t\t|  0  |  Exit                      |")

    print("\n")

    try:
        a=int(input("Select a choice : "))
        print("____________________________________________________________________________\n")
        if a == 0:
            print("Thank you for using MSD's Petrol bunk")
            print("************* Visit Again **************")
            break
        if a==1:

         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ VIEW STOCKS ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print("PETROL   =  "+str(pet)+" ltr")
         print("DIESEL   =  "+str(die)+" ltr")
         print("-------------------------------------------------------")

        if a==2:
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~ VIEW PRICES ~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print("PETROL   = Rs. "+str(petpri))
         print("DIESEL   = Rs. "+str(diepri))
         print("-------------------------------------------------------")

        if a==3:
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ VIEW SALES~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         f2=len(vno)
         for i in range(f2):
          y2=i+1
          y1=str(y2)
          print("S.NO        = "+y1)
          print("VEHICLE NO  = "+vno[i])
          print("PARTICULAR  = "+par[i])
          print("VOLUME      = "+vol[i]+" ltr")
          print("AMOUNT      = Rs. "+amt[i])
          print("DATE        = "+dte[i])
          print("************************************************")

        if a==4:
         print("~~~~~~~~~~~~~~~~~~~~~~~~ UPDATE PETROL PRICE~~~~~~~~~~~~~~~~~~~~~~~~")
         petpri=float(input("ENTER PETROL PRICE : "))

        if a==5:
         print("~~~~~~~~~~~~~~~~~~UPDATE DIESEL PRICE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         diepri=float(input("ENTER DIESEL PRICE : "))

        if a==6:
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ PETROL PURCHASE ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         pet=pet+(int(input("ENTER THE VOLUME OF PETROL : ")))

        if a==7:
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~DIESEL PURCHASE ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         die=die+(int(input("ENTER THE VOLUME OF DIESEL : ")))

        if a==8:
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ BILL ENTRY ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         vno.append((input("Enter The VEHICLE NUMBER  : ")))
         print("CHOOSE THE PARTICULAR :")
         print("Enter 1 FOR PETROL")
         print("Enter 2 FOR DIESEL")
         ch=int(input("Choose Any One : "))

         if(ch == 1):
          par.append("PETROL")
          p1=int(input("Enter the Petrol Volume : "))
          a1=p1*petpri
          print("Price : "+str(a1))
          pet=pet-p1
          vol.append(""+str(p1))
          amt.append(""+str(a1))
          dat=datetime.date.today().strftime("%B %d, %Y")
          dte.append(dat)

         if(ch == 2):
          par.append("DIESEL")
          p1=int(input("Enter the Diesel Volume : "))
          a1=p1*diepri
          print("Price : "+str(a1))

          die=die-p1
          vol.append(""+str(p1))
          amt.append(""+str(a1))
          dat=datetime.date.today().strftime("%B %d, %Y")
          dte.append(dat)

        if a==9:
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~ ADD NEW EMPLOYEE ~~~~~~~~~~~~~~~~~~~~~~~~~~")
         empid.append(input("Enter The Employee ID : "))
         empname.append(input("Enter The Employee Name : "))
         empage.append(input("Enter The Employee Age : "))
         empaddr.append(input("Enter The Employee Address : "))
         empphno.append(input("Enter The Employee Phone Number : "))

        if a==10:
         print("~~~~~~~~~~~~~~~~~~~~~~~~ VIEW EMPLOYEE DETAILS ~~~~~~~~~~~~~~~~~~~~~~~~")
         f2=len(empid)
         for i in range(f2):
          y2=i+1
          y1=str(y2)
          print("EMPLOYEE ID              = "+empid[i])
          print("EMPLOYEE NAME            = "+empname[i])
          print("EMPLOYEE AGE             = "+empage[i])
          print("EMPLOYEE ADDRESS         = "+empaddr[i])
          print("EMPLOYEE PHONE NUMBER    = "+empphno[i])
          print("************************************************")
        if a==11:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE STUDENT ~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f2=len(empname)
                for y in range(f2):
                    y2=y+1
                    y1=str(y2)

                    print(y1+"EMPLOYEE NAME  :   ->>  "+empname[y])
                    print("")
                r1 = int(input("Select a employee name [ 0 for back ] : "))
                if(r1 != 0):

                    temp=""+empname[r1-1]
                    empid.pop(r1-1)
                    empname.pop(r1-1)
                    empage.pop(r1-1)
                    empaddr.pop(r1-1)
                    empphno.pop(r1-1)
                    print(""+temp+" Removed Successfully!..")

        if a>11:
          print("Please enter a valid choice from 1-10 and 0")
    except ValueError:
            print("Please input as suggested.")

    r=int(input("do you want to conti 1 or 0:"))
    if r==1:
        continue
    else:
        break

