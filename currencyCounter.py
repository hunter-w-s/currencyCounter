def main():
    moneyIn = input('How much money is it: ')

    try:
        moneyIn = float(moneyIn)
    except Exception as e:
        return("Error - Invalid Type of Input, Must be an Int or Float")

    if(moneyIn == 0):
        return("Error - Input Cannot be 0")

    originalMoney = '%.2f' % moneyIn

    moneyIn = int(float('%.2f' % moneyIn)*100)

    outString = "Amount: {}, Currencies:".format(originalMoney)

    cNames = ['$100 Bills','$50 Bills','$20 Bills','$10 Bills','$5 Bills','$1 Bills','Quarters','Dimes','Nickles','Pennies',]
    cValues = [10000,5000,2000,1000,500,100,25,10,5,1]
    cInt = 0

    for each in currencys:
        if(cValues[cInt]<=moneyIn):
            amountEach = int(moneyIn/cValues[cInt])
            moneyIn = moneyIn - (amountEach*cValues[cInt])
            print(amountEach)

            segmentString = " {}: {},".format(cNames[cInt],amountEach)
            
            outString = outString + segmentString

        cInt = cInt+1

    outString = outString[:-1]
         
    return(outString)


if __name__ == "__main__":
    repeat = 'y'
    while(repeat == 'y'):
        print(main())
        repeat = input("Would you like to go again (y/n): ")
    
