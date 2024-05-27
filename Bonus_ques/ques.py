
def calToFah(c):
    return float((c * 9/5) + 32)

def fahToCal(f):
    return float((f-32)*5/9)


c = int(input("enter cel: "))
fah = calToFah(c)
f = int(input("enter fah: "))
cel = fahToCal(f)
print(f"cel is {cel} and fah is -{fah}")
print("cel is"+ str(cel) + "and fah is - "+ str(fah))

print("cel is {} and fah is - {}".format(cel, fah))


import random

def guess_number():
    rand_num = random.randint(1, 9)
    print(" chosen one is {}".format(rand_num))

    print("guess number bet 1 to 9")

    guess = None

    while guess != rand_num:
        guess = int(input('guess number again '))

        if guess < rand_num:
            print('it is greator whatever you have guessed')
        elif guess > rand_num:
            print('it is lesser whatever you have guessed')
        else:
            print('you guessed it correctly ')

guess_number()
        

def pyra(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")

        for k in range(2*i+1):
            print("a", end="")
        print()

pyra(10)

st=""
while True:
    inp = input("enter char or spaces to eliminate :-- ")
    if inp in [' ', '   ', '___', "_", "#"]:
        break
    else:
        st+=inp + ", "
print(st)


# whether the string is integer or not

str_value = "23"

if str_value.isdigit():
    print("this is numerical value (int, float)")
else:
    print('this one is string')

v = list(str_value)
print(v)

digits = [0,1,2,3, 4, 5, 6, 7,8,9]
for i  in v:
    if int(i) in digits:
        print('digits are there')
        break
    else:
        print('str')

# regex 

import re 

regex = '^[0-9]+$'
print(re.search(regex,str_value ))



value = ['1', '2', 'asasa', 4, 5]
count = 0 
for i in value:
    if str(i).isdigit():
        count +=1
print(count)
    



 
