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
            print('\n The availables are: \n 1) Sweat Shirt \n 2) Jean Trouser \n 3) Cardigan, \n 4) Round neck \n 5) Tuttle neck \n 6) Suit \n 7) Towel \n 8) Curtain \n 9) Table Cloth'
                  '\n 10) Slippers')
        break

#all clothes
ClothList=[]
clothBy = []
clthDict ={'Sweat Shirt':250, 'Jean Trouser':500, 'Cardigan':800, 'Round neck':450, 'Tuttle neck':420, 'Suit':2000, 'Towel':320, 'Curtain':120, 'Table Cloth':20, 'Slippers':120}

# print('Please select y/n as requires \n')
# value1 = input('Sweat Shirt?: ')
# if value1 == 'y':
#     print('Sweat Shirt selected \n')
#     ClothList.append('Sweat Shirt')
# elif value1 == 'n':
#     print('Swear Shirt not selected \n')
#
#
# value2 = input('Jean?: ')
# if value2 == 'y':
#     print('Jean selected\n ')
#     ClothList.append('Jean')
# elif value2 == 'n':
#     print('Jean not selected \n')
#
#
#
# value3 = input('Cardigan?: ')
# if value3 == 'y':
#     print('Cardigan selected \n')
#     ClothList.append('Cardigan')
# elif value3 == 'n':
#     print('Cardigan not selected \n')
#
#
# value4 = input('Roundneck?: ')
# if value4 == 'y':
#     print('Roundneck selected \n')
#     ClothList.append('Round neck')
# elif value4 == 'n':
#     print('Roundneck not selected \n')
#
#
#
# value5 = input('Tuttle neck?: ')
# if value5 == 'y':
#     print('Tuttle neck selected \n')
#     ClothList.append('Tuttle neck')
# elif value5 == 'n':
#     print('Tuttle neck not selected \n')
#
#
# value6 = input('suit?: ')
# if value6 == 'y':
#     print('suit selected \n')
#     ClothList.append('Suit')
# elif value6 == 'n':
#     print('suit not selected \n')
#
#
# value7 = input('Towel?: ')
# if value7 == 'y':
#     print('Towel selected \n')
#     ClothList.append('Towel')
# elif value7 == 'n':
#     print('Towel not selected \n')
#
#
# value8 = input('Curtain?: ')
# if value8 == 'y':
#     print('Curtain selected \n')
#     ClothList.append('Curtain')
# elif value8 == 'n':
#     print('Curtain not selected \n')
#
#
# value9 = input('Table cloth?: ')
# if value9 == 'y':
#     print('Cardigan selected \n')
#     ClothList.append('Table cloth')
# elif value9 == 'n':
#     print('Cardigan not selected \n')
#
#
# value10 = input('Slippers?: ')
# if value10 == 'y':
#     print('Slippers selected \n')
#     ClothList.append('Slippers')
# elif value10 == 'n':
#     print('Slippers not selected \n')
#
# print(Name+',' + ' you selected' + str(ClothList))
#
# unavilables = ['Sweat Shirt', 'Round neck', 'Suit',   'Slippers']
# print (ClothList - unavilables)
#

# clothes = ['Sweat Shirt', 'Jean Trouser', 'Cardigan', 'Round neck', 'Tuttle neck', 'Suit', 'Towel', 'Curtain', 'Table Cloth', 'Slippers']
# for clothe in clothes:
#     print('Will you like to buy', clothe)
#     value = input()
#     if value == 'y':
#         print(str(clothe),'selected \n')
#         clothBy.append(str(clothe))
#     elif value == 'n':
#         print(str(clothe), 'not selected \n')
#
# unavailables = ['Jean Trouser', 'Cardigan']
# buy = set(clothBy) - set(unavailables)
# print('These are the clothes you wanted to buy', clothBy, 'but these are the ones we do have cureently', buy)

#printprice
for price in clthDict:
    print('The price of', clthDict[0,0])

