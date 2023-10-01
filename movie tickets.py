money_need=1000
recived_amt=0
asking_amt=0
for i in range(5):
    money_given=int(input("enter the amount:"))
    if  money_given <=10:
        print("thank you! but this amount is too small...")
        continue
    money_given += recived_amt
    print("Thank you..!",money_given,"so far")
                     
    if recived_amt >= money_need :
           break
    print("thank you..!",asking_amt,"its time to get 1000")

