#Defining a general function getInformation
#rankingFileName set default to "TopUni.csv"
#capitalsFileName set default to "capitals.csv"
def getInformation(selectedCountry,rankingFileName,capitalsFileName):

    #Open the file output.txt in writing mode
    outfile = open("output.txt", "w")
    #Opens file TopUni.csv in reading mode with encoding='utf-8' to read special characters too.
    infile = open(rankingFileName,"r",encoding='utf-8')
    #Opens file capitals.csv in reading mode with encoding='utf-8' to read special characters too.
    infile2 = open(capitalsFileName,"r",encoding='utf-8')

    try:

        # TEST - 1 : UNIVERSITIES COUNT

        #Opens file TopUni.csv in reading mode with encoding='utf-8' to read special characters too.
        infile = open(rankingFileName, "r",encoding='utf-8')
        # A variable named 'total' is initialized which stores the total number of universities.
        total = 0
        # A variable named 'count' is created which stores the total number of lines in the file 'TopUni.csv'.
        count = 0
        #This code reads a single top line of the file 'TopUni.csv'.
        line = infile.readline()
        #While loop is created to keep reading the lines from the TopUni.csv file.
        while line != "":
            #count gets updated by +1 every time a line is being read
            count = count + 1
            #This line of code inside while loop keeps reading the lines of text in 'TopUni.csv' file.
            line = infile.readline()
        #First line is being reduced from the count as it doesn't contain University list.
        total = count - 1
        #This code writes the desired output in output.txt
        outfile.write("Total number of universities => {}\n".format(total))



        # TEST - 2 : AVAILABLE COUNTRIES

        infile = open(rankingFileName, "r",encoding='utf-8')
        line = infile.readline()
        #Empty list 'country' created which adds individual countries into the empty list 'countries'.
        country = []
        #Empty list 'countries' created which stores all the countries.
        countries = []
        #for loop reads lines from the file 'TopUni.csv'.
        for line in infile:
            #This code strips '\n' and splits all the lines into 7 parts using ',' as the seperator for 'TopUni.csv'.
            new = line.rstrip().rsplit(",",7)
            #country name is at index position 1 in our variable named 'new'.
            country = new[1]
            #if statement is used to check if the country is added to the 'countries' list, and appends it if not added yet.
            if country.upper() not in countries:
                countries.append(country.upper())
            else:
                continue
        #This code writes the desired output in output.txt
        outfile.write("Available countries => {}\n".format(countries))



        #TEST - 3 : AVAILABLE CONTINENTS

        infile2 = open(capitalsFileName, "r",encoding='utf-8')
        line = infile2.readline()
        #Empty list 'continent' created which adds individual countries into the empty list 'continents'.
        continent = []
        # Empty list 'continents' created which stores all the countries.
        continents = []
        for line in infile2:
            # This code strips '\n' and splits all the lines into 6 parts using ',' as the seperator for 'capitals.csv'.
            new = line.rstrip().rsplit(",", 6)
            #continent name is located at 5th index in our split 'new' list.
            continent = new[5]
            # if statement is used to check if the continent is added to the 'continents' list, and appends it if not added yet.
            if continent.upper() not in continents:
                continents.append(continent.upper())
            else:
                continue
        # This code writes the desired output in output.txt
        outfile.write("Available continents => {}\n".format(continents))



        #TEST - 4 : THE UNIVERSITY WITH TOP INTERNATIONAL RANK

        infile = open(rankingFileName,"r",encoding='utf-8')
        line = infile.readline()
        #variable - Last Rank in 'TopUni.csv' file,i.e.,100.
        TopRank = 100
        #variable - Top Uni defined which is initially an empty string.
        TopUni = ""
        for line in infile:
            seperate = line.rstrip().rsplit(",",8)
            #if statement which checks if the country from the TopUni.csv file is same as the selectedCountry.
            if seperate[2].upper() == selectedCountry.upper():
                    #Rank is stored at index position 0 in our seperate list for different universities.
                    TopRank = seperate[0]
                    #TopUni is stored at index position 1 in our seperate list for different universities.
                    TopUni = seperate[1]
                    break
        # This code writes the desired output in output.txt
        outfile.write("At international rank => {} the university name is => {}\n".format(TopRank,TopUni))



        #TEST - 5 : THE UNIVERSITY WITH TOP NATIONAL RANK

        infile = open(rankingFileName,"r",encoding='utf-8')
        line = infile.readline()
        #constant TOPRANK2 is defined as the Top National Rank will always be 1.
        TOPRANK2 = 1
        #null list TopUni is created initially.
        TopUni = []
        for line in infile:
            seperate = line.rstrip().rsplit(",",8)
            if seperate[2].upper() == selectedCountry.upper():
                #index 3 in our seperate list is National Rank, which looks for 1.
                if seperate[3] == "1":
                    #when it finds the university with national rank 1, it appends the university at index 1 in seperate list to TopUni list.
                    TopUni.append(seperate[1])
                    break
        # This code writes the desired output in output.txt
        outfile.write("At national rank => {} the university name is => {}\n".format(TOPRANK2,TopUni[0]))



        #TEST - 6 : THE AVERAGE SCORE

        try:
            infile = open(rankingFileName,"r",encoding='utf-8')
            line = infile.readline()
            #variable 'sum' created which stores the sum of score. (initial sum of scores is set to 0)
            sum = 0
            #variable 'count' created to act as a counter, initialized to 0.
            count = 0
            for line in infile:
                seperate = line.rstrip().rsplit(",",8)
                if seperate[2].upper() == selectedCountry.upper():
                    #if statement which compares float score values (at index 8 in seperate list) of universities to 0.
                    if float(seperate[8]) > 0:
                        #num varibale which stores the score of one university at a time.
                        num = float(seperate[8])
                        #sum variable which keeps on adding new num values to itself as it is in a for loop.
                        sum = sum + num
                        #count being updated by 1 everytime.
                        count = count + 1
            #averageScore formula
            averageScore = sum/count
            # This code writes the desired output to output.txt.
            outfile.write("The average score => %.2f%%\n"%(averageScore))
        #exception raised if count is 0 while calculating averageScore.
        except ZeroDivisionError:
            print("No number of universities to divide with")



        #TEST - 7 : THE CONTINENT RELATIVE SCORE

        infile = open(rankingFileName,"r",encoding='utf-8')
        infile2 = open(capitalsFileName,"r",encoding='utf-8')
        line = infile.readline()
        line2 = infile2.readline()
        #empty initial 'univcontinent' string is defined.
        univcontinent = ""
        #empty initial 'countryContinent' list is created.
        countryContinent = []

        for line in infile2:
            #strips the character '\n' and splits the lines in file 'capitals.csv' into 5 parts with ',' as seperator.
            seperate2 = line.rstrip().rsplit(",",5)
            if seperate2[0].upper() == selectedCountry.upper():
                #univcontinent is provided with value from 5th index of seperate2 list from capital.csv file, if the country is equal to selectedCountry.
                univcontinent = seperate2[5]
                #breaks from the loop
                break
        infile2 = open(capitalsFileName,"r",encoding='utf-8')
        for line in infile2:
            seperate2 = line.rstrip().rsplit(",", 5)
            #if statement is used to sort out the same continents from capitals.csv as the univcontinent.
            if univcontinent.upper() == seperate2[5].upper():
                #countries from same continent are appended to countryContinent list.
                countryContinent.append(seperate2[0])
        #for loop which runs as many number of times as the length of list countryContinent converting the elements to upper case.
        for i in range(len(countryContinent)):
            countryContinent[i] = countryContinent[i].upper()
        #initial value of varibale 'i' set to 0.
        i = 0
        #initial value of 'TopScore' variable set to 0.
        TopScore = 0.0
        try:
            infile = open(rankingFileName,"r",encoding='utf-8')
            line = infile.readline()
            for line in infile:
                seperate = line.rstrip().rsplit(",",8)
                #if country from 'TopUni.csv' is in the new countryContinent list.
                if seperate[2].upper() in countryContinent:
                    #and if float value of score (at index position 8 in our seperate list (or to be clear at position 8 in 'TopUni.csv' file))
                    if float(seperate[8]) > TopScore:
                        #TopScore variable is updated to the new value
                        TopScore = float(seperate[8])
            #relativeScore formual = averageScore/TopScore)*100
            relativeScore = float(averageScore/TopScore)*100.0
            # These two lines of code writes the desired output in output.txt
            outfile.write("The relative score to the top university in %s is => (%.2f/%.2f)*100%% "%(univcontinent.upper(),averageScore,TopScore))
            outfile.write("=%.2f%%\n"%relativeScore)
        #General Exception raised
        except Exception:
            print("")



        #TEST - 8 : THE CAPITAL CITY

        infile = open(rankingFileName,"r",encoding='utf-8')
        infile2 = open(capitalsFileName, "r", encoding='utf-8')
        line = infile.readline()
        line2 = infile2.readline()
        #initial empty variable 'capital'.
        capital = ""
        #for loop which reads throughout the lines in 'capitals.csv'.
        for line2 in infile2:
            seperate2 = line2.rstrip().rsplit(",",5)
            #if selectedCountry is the same as any country in index position 0 in seperate2 list {capitals.csv}
            if seperate2[0].upper() == selectedCountry.upper():
                #capital is being assigned the value from index position 1 of seperate2 list (Capital section of 'capitals.csv' file - only to explain)
                capital = seperate2[1]
        # This code writes the desired output in the file 'output.txt'.
        outfile.write("The capital is => {}\n".format(capital))



        #TEST - 9: THE UNIVERSITIES THAT HOLD THE CAPITAL NAME

        infile = open(rankingFileName,"r",encoding='utf-8')
        infile2 = open(capitalsFileName,"r",encoding='utf-8')
        line = infile.readline()
        line2 = infile2.readline()
        #initial empty 'univcapital' list
        univcapital = []
        for line in infile:
            seperate = line.rstrip().rsplit(",",8)
            if seperate[2].upper() == selectedCountry.upper():
                #if the capital from the previous test is in the name of universities, goes through every university name as it is in a for loop.
                if capital in seperate[1]:
                    #university name is appended to the empty list 'univcapital'
                    univcapital.append(seperate[1])
        #This code writes desired output to file output.txt
        outfile.write("Universities with capital name => ")
        #formatting so as to write multiple universities in 'output.txt' according to the desired format as in instructions.
        for i in range(len(univcapital)):
            outfile.write("\n#%d%s"%((i+1),univcapital[i]))

    #exception raised if the files 'TopUni.csv' or 'capitals.csv' or 'output.txt' are not found and quits the code.
    except FileNotFoundError:
        print("Error message: File not found.")
        quit()