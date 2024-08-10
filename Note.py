'''In Python, when an argument passed to a function is modified inside it, whether the change is 
visible outside or not depends on whether the variable is mutable or not.
Let's understand how it works. Execute and observe the result for code given below;'''

def func(sample, res, key, val):
    if (key in sample):
        res = True
    sample.update({key: val})
    res = False

res = None
sample = {"XS": 1, "X": 0, "XL": 3, "XXL": 4}
func(sample, res, "X", 2)#res value will be none only ,it will not change to False
print(sample["X"], res)
print("----------------------------------------------------------------------------------------------------------------")

def check_in(baggage,boarding_pass):
    if(baggage>=1 and baggage<=30):
            boarding_pass="Issued"

def update_seat(seat_list):
    seat_list[1]=25

boarding_pass="Not Issued"
print("boarding_pass before function call:", boarding_pass)
check_in(25, boarding_pass)
print("boarding_pass after function call:", boarding_pass)
print("boarding_pass, a string is immutable")
print("-------------------------------------------------------")

passenger_seat=["Jack","NA"]
print("passenger_seat before function call:", passenger_seat)
update_seat(passenger_seat)
print("passenger_seat after function call:", passenger_seat)
print("passenger_seat, a list is mutable")

