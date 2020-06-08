print('Please input the required information\n')
Name = input('Please input your name: ')

#Name
print(Name, 'welcome to Sam Stores ')
# PhoneNumber
Phn_No = input('Please input your Phone number: ')
#Gender
Gender = input('Please select your gender form the following options \n 1) Male \n 2) Female \n')
if Gender == '1':
    print('Your gender is Male\n')
elif Gender == '2':
    print('Your gender is Female \n')

#Age
while True:
    Age = input('Please input your age: ')
    if Age.isdigit():
        if int(Age) <= 18:
            print('Sorry, but this store is meant for adults. Come back when you are 18')
        else:
            print('\n The availables are: \n 1) Sweat Shirt \n 2) Jean Trouser \n 3) Cardigan, \n 4) Round neck \n '
                  '5) Tuttle neck \n 6) Suit \n 7) Towel \n 8) Curtain \n 9) Table Cloth'
                  '\n 10) Slippers')
        break

#all clothes
clothBuy = []
clthDict ={'Sweat Shirt':250, 'Jean Trouser':500, 'Cardigan':800, 'Round neck':450, 'Tuttle neck':420, 'Suit':2000, 'Towel':320, 'Curtain':120, 'Table Cloth':20, 'Slippers':120}


#printprice
for price in clthDict:
    value1 = input('Sweat Shirt?: ')
    if value1 == 'y':
        print(price, 'selected \n')
        clothBuy.append(str(price))
    elif value1 == 'n':
        print(price, ' not selected \n')

for cloth in clothBuy:
    cost = str(clthDict[cloth])
    print('You are buying', cloth, 'at the price', cost)
