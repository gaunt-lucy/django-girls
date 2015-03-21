def discount(age):
    if age <=22 or age >=65:
        print('Because you are ' + str(age) + ', you can get money off your travel.')
        if age <=21:
            print('You qualify for a youth discount.')
        if age >=65:
            print('You qualify for a senior discount.')
    else:
        print('No discount for you!')
age = input('How old are you?')
age = int(age)
discount(age)
