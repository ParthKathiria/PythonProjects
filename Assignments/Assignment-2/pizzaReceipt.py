#generateReceipt function defined
def generateReceipt(pizzaOrder):
    #an empty list, prints 'You did not order anything if the user does not order anything.
    if pizzaOrder == []:
        print("You did not order anything")
        return
    #TAXRATE is a constant , given 13% of tax is applied to the order
    TAXRATE = 0.13
    #intializes the total price of the order at 0.0 and numberOfPizzas acts a counter in this case
    totalPrice = 0.0
    numberOfPizzas = 1
    print("Your order:")
    #for function used to indicate to every particular pizza in the whole pizzaOrder list.
    for pizza in pizzaOrder:
        #size is always at the first place in the list for a particular pizza
        size = pizza[0]
        #the list of the toppings is at the second place in the list for a particular pizza.
        toppingsList = pizza[1]
        pizzaNum = str(numberOfPizzas)

        #these lines for code from 22 to 36 define the base cost of the different pizza sizes along with the cost of adding additional toppings
        if size.upper() == "S":
            BASECOST = 7.99
            ADDITIONALTOPPINGSCOST = 0.50

        elif size.upper() == "M":
            BASECOST = 9.99
            ADDITIONALTOPPINGSCOST = 0.75

        elif size.upper() == "L":
            BASECOST = 11.99
            ADDITIONALTOPPINGSCOST = 1.00

        elif size.upper() == "XL":
            BASECOST = 13.99
            ADDITIONALTOPPINGSCOST = 1.25
        #Base Cost of the pizza selected by the user is added to the totalPrice.
        totalPrice = totalPrice + BASECOST
        #Aligns the text and the spaces between the text.
        print("Pizza",pizzaNum + ":", size, "%14.2f" %(BASECOST))
        for topping in toppingsList:
            print('-',topping)

        #if function used to add additional charges to the user if the number of toppings exceed 3.
        if len(toppingsList) > 3:
            #for function loops the code multiple times based on the number of additional toppings ordered.
            for extra in range(len(toppingsList)-3):
                if len(size) == 1:
                    print('Extra Topping', '(' + size + ')', '%7.2f' % (ADDITIONALTOPPINGSCOST))
                else:
                    print('Extra Topping', '(' + size + ')', '%6.2f' % (ADDITIONALTOPPINGSCOST))
                #Adds extra charges to the total price caused due to adding extra toppings based on the size of the pizza ordered
                totalPrice = totalPrice + ADDITIONALTOPPINGSCOST
        #counter updated
        numberOfPizzas = numberOfPizzas + 1
    #calculates tax amount
    taxAmount = totalPrice * TAXRATE
    #adds tax amount to the total price
    totalPrice = totalPrice + taxAmount
    #formats and primts the taxAmount and totalPrice
    print('Tax: %20.2f' %(taxAmount))
    print('Total: %18.2f' %(totalPrice))
    #returns the function
    return










