#lex_auth_01269441810970214471

def check_double(number):
    
    #Remove pass and write your logic here
    num=2*number
    number=str(number)
    num=str(num)
    for digit in num:
        if digit not in number:
            return False
    return True
    

#Provide different values for number and test your program
print(check_double(245))