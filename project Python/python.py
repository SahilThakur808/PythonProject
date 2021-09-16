print('number guessing game')
print('guess a number between 1 to 9')
number=int(input('enter the number'))
if(number<9):
    print('this number is too small,enter a number greater than',number)
    number=int(input('enter the5 number'))

elif(number==9):
    print('yay!,you guessed the right number')
