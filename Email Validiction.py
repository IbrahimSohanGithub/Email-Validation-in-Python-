# You can't get the output with 6 characters. 1st condition
# You can't get the output if your email has the first character is a number. 2nd condition
# You can't get the output if your email does not have -4 or -3 is a dot(.) 3rd condition
# You can't get the output if your email has more than one dot(.) from -9 (Index) to end of string. 4th condition
# You can't get the output if your email has more than one @ character. 5th condition
# You can't get the output if your email has a space. 6th condition
# You can't get the output if your email has a capital letter. 7th condition
# you can't get the output if your email has any special character. 8th condition


email = input('Enter your email : ')
num, num1, num2 = 0, 0, 0

if len(email) >= 6:     # 1st condition for email length is greater than 6 or not
    if email[0].isalpha():  # 2nd condition give you error if email start with number
        if ('@' in email) and (email.count('@') == 1) and email[-9:].count('.') == 1:  # 3rd condition give you error if email have more than one @
            if (email[-4] == '.') ^ (email[-3] == '.') :  # 4th condition give you error if email have more than one .
                for loop in email:
                    if loop.isspace():  # 5th condition give you error if email have space
                        num = 1
                    elif loop.isalpha():
                        if loop == loop.upper():    # 5th condition give you error if email have uppercase letter
                            num1 = 1
                    elif loop.isdigit():
                        continue
                    elif loop == '_' or loop == '.' or loop == '@':
                        continue
                    else:
                        num2 = 1
                if num == 1:
                    print('You entered an invalid email because you have space in your email.')
                elif num1 == 1:
                    print('You entered an invalid email because you have uppercase letter in your email.')
                elif num2 == 1:
                    print('You entered an invalid email because you have special character in your email.')
                else:
                    print('Congratulation! You entered a right email.')
            else:
                print('You entered a invalid email because you don\'t have write position of dot(.).') # 4th condition give you error if email have more than one .
        else:
            print('You entered a invalid email because you have more than one @ or entered a two dot (.) in in list 9 letters. .') # 3rd condition give you error if email have more than one @
    else:
        print('You entered a invalid email because you have number in your email in the first character.') # 2nd condition give you error if email start with number
else:
    print('You entered an invalid email because you have less than 6 character in your email. ') # 1st condition give you error if email length is less than 6
