def bandnamegen(city,pet):
    return f'Your band name could be {city} {pet}'

city = input('What city did you grow up in?\n')
pet = input('What is the name of your pet?\n')

print(bandnamegen(city,pet))