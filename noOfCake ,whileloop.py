noOfCake = 0
noOfChoc = 0
# Get budget from the user
money = float(input("Enter your budget: Rs "))
while money >= 150:
    if money >= 200:
        # Buy a chocolate
        noOfChoc += 1
        money -= 200
    else:
        # If there's not enough money for a chocolate, buy a cake
        noOfCake += 1
        money -= 150
# Print the number of cakes and chocolates bought
print("You can buy", noOfCake, "cakes and", noOfChoc, "chocolates.")#With this code, the program will ask the user for their budget and then calculate how many cakes and chocolates they can buy with that budget.





