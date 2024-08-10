#In cases where a global variable needs to be modified inside a function, like in function update_baggage_limit(),
#  Python allows you to do that using the global keyword.

wt_limit=30#global variable

def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    wt_limit=new_wt_limit#Local variable
    print("This airline now allows baggage limit till",wt_limit,"kgs")

print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")

print("-----------------------------------------------------------------------------------------------------")
wt_limit=30

def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    global wt_limit
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")

#def useless_function_to_prove_a_point():
    #print("Extra baggage:",extra_baggage)
    #print("Extra baggage charge:",extra_baggage_charge)

print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
#print("Extra baggage:",extra_baggage)
#print("Extra baggage charge:",extra_baggage_charge)
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
useless_function_to_prove_a_point()  