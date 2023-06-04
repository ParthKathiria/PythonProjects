'''
infRate represents Inflation Rate
EC represents Expenditure Categories
TPE represents Total previous year expenses
TCE represents Total current year expenses
'''
#Assignment-1

year = int(input("Please enter the year that you want to calculate the personal interest rate for: "))
EC = int(input("Please enter the number of expenditure categories: "))
TPE = 0
TCE = 0

#for function used
for a in range(EC):
    previous = int(input("Please enter expenses for previous year: "))
    current = int(input("Please enter expenses for current year: "))
    TPE = TPE + previous
    TCE = TCE + current

#Formula for finding the Inflation Rate
infRate = ((TCE-TPE)/TCE)*100
print("Personal inflation rate for {} is {}%".format(year,infRate)) #Printing Inflation Rate

#if,and,elif functions used
if infRate<3:
    print("Type of Inflation: Low")
elif infRate>=3 and infRate<5:
    print("Type of Inflation: Moderate")
elif infRate>5 and infRate<10:
    print("Type of Inflation: High")
elif infRate>=10:
    print("Type of Inflation: Hyper")







