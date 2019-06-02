import operator
seats = None
while seats == None:
    try:
        seats = int(input("Enter number of seats available:"))
        if seats <= 0:
            print("Number of seats can not be less than 1")
            seats = None
        elif seats > 10:
            print("Number of seats can not be more than 10")
            seats = None
    except ValueError:
        seats = None
        print("number of seats must be a valid number more than 0")
party_num = None
while party_num == None:
    try:
        party_num = int(input("Enter number of parties in the election:"))
        if party_num <= 0:
            print("number of parties can not be less than 1")
            party_num = None
        elif party_num > 10:
            print("Number of seats can not be more than 10")
            seats = None
    except ValueError:
        party_num = None
        print("number of seats must be a valid number more than 0")
parties_seats = {}
for i in range(party_num):
    party_name = None
    while party_name == None:
        party_name = input("Please enter the name of the party:")
        if party_name in parties_seats:
            print("Party already entered")
            party_name = None
        elif len(party_name) == 0:
            print("You must enter a party name")
            party_name = None
    percent = None
    while percent == None:
        try:
            percent = float(input("Please enter the percentage of votes for "+party_name+": "))
            if percent < 0 or percent > 100:
                percent = None
                print("percentage must be between 0 and 100")
        except ValueError:
            percent = None
            print("You must enter a valid number for the percentage")
    parties_seats[party_name] = [percent,0]
if sum([parties_seats[party][0] for party in parties_seats]) != 100:
    print("Ooops something went wrong, your percentages did not add to 100!")
else:
    for i in range(seats):
        index, value = max(enumerate([parties_seats[party][0]/(parties_seats[party][1]+1) for party in parties_seats]), key=operator.itemgetter(1))
        parties_seats[list(parties_seats.items())[index][0]][1] += 1
for party in parties_seats:
    print(party+" won this many seats:"+str(parties_seats[party][1]))
