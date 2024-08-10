#lex_auth_012693750719488000124
import string
def get_count(num_list):
    count=0

    # Write your logic here
    for i in range(1,len(num_list)):
        if num_list[i]==num_list[i-1]:
            count+=1

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
print("-------------------------------------------------------")
#lex_auth_012693763253788672132
import random
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[0]*no_of_passengers
    num=100
    #Write your logic here
    for i in range(0,no_of_passengers):
        num+=1
        ticket_number_list[i]=airline+':'+source[0:3]+':'+destination[0:3]+':'+str(num)
    
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))