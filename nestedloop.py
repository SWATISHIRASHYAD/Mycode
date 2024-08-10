#Loop When to use
#for loop with range:To create a sequence and iterate over it. Not preferred when collections are involved.
#for loop with in:To access the values of elements in a collection
#while loop:When number of iterations are not known
number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1): 
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
           print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
print("-------------------------------------------------------------------------------------------------------")
number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    baggage_count =1
    while (baggage_count<=number_of_baggage):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
        baggage_count+=1
print("---------------------------------------------------------------------------------------")
baggage_count=10
no_of_baggage_picked=0
while(baggage_count>0):
    no_of_baggage_picked = (int)(input ("Number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
    print("No. of baggage remaining:",baggage_count)
print("_----------------------------------------------------------------------------------------")
for passenger in "A","A", "FC", "C", "FA","SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
        print("Check the person")
        print("Check for cabin baggage")
print("-------------------------------------------------------------------------------------")
num_list = []
for num in num_list:
    print(num, end = " ")

