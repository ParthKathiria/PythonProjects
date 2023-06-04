from pizzaReceipt import generateReceipt

#TUPLE is immutable, here we have all the toppings inside a tuple as they wont change further in the program.
TOPPINGS = ("ONION","TOMATO","GREEN PEPPER","MUSHROOM","OLIVE","SPINACH","BROCCOLI","PINEAPPLE","HOT PEPPER","PEPPERONI","HAM","BACON","GROUND BEEF","CHICKEN","SAUSAGE")

#pizzaOrder is an initialized as an empty list, elements would be added to this list as we move on with the program.
#pizzaOrder is our main list which would store the pizzas along with their sizes and toppings.
pizzaOrder = []

#yourToppings is also an empty list at first, to which the toppings that the user selects would be added.
yourToppings = []

#Asks user for input wheather they would like to order a pizza or not
eatPizza = input("Do you want to order a pizza? ")

#If the user would not like to order a pizza and enters NO or Q, "You did not order anything" prints out.
if eatPizza.upper() == "NO" or eatPizza.upper() == "Q":
    print("You did not order anything")

#while function
while True:
    #current Topping is intialized as an empty list, where the toppings for a particular pizza would be added.
    currentTopping = []
    if eatPizza.upper() != "Q" or eatPizza.upper() != "NO":
        #yourSize is a variable that stores the pizza size entered by the user.
        yourSize = (input("Choose a size: S, M, L, XL: "))
        #sizes available are small, medium , large and extra large.
        size = ("S", "M", "L", "XL")
        #while loop used to keep asking the user for a valid pizza size from the sizes available.
        while yourSize.upper() not in size:
            yourSize = (input("Choose a size: S, M, L, XL: "))
        #uppercases the size
        yourSize = yourSize.upper()
        yourToppings = []
        #while loop used to keep asking user for the topping, typing X indicates that user is done selecting the toppings for a particular pizza.
        while currentTopping != "X":
            currentTopping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter \"X\"\n('")
            currentTopping = currentTopping.upper()
            if currentTopping in TOPPINGS:
                print("Added {} to your pizza.".format(currentTopping))
                #Adds toppings selected by the user for the particular pizza to the list - yourToppings.
                yourToppings.append(currentTopping)
            #if user types LIST, the TOPPINGS TUPLE is printed for the user to select the topping from.
            elif currentTopping == "LIST":
                print(TOPPINGS)
            #If the user inputs X, it breaks the while loop
            elif currentTopping == "X":
                break
            #If the user types any other unmentioned topping from TUPLE or not X , 'Invalid Topping' is printed.
            else:
                print("Invalid topping")
        #pizzaOrder list is formatted in the given manner
        pizzaOrder.append((yourSize,yourToppings))
        while yourToppings == "X":
            break
        #additionalPizza is a variable that stores the input from the user if they want to order another pizza
        additionalPizza = (input("Do you want to continue ordering?"))
        #If user would not like to order another pizza, the loop breaks
        if additionalPizza.upper() == "NO" or additionalPizza.upper() == "Q":
            break
        #if the user would like to order another pizza, the loop continues
        else:
            continue

#generates a receipt based on the customer's order
print(generateReceipt(pizzaOrder))