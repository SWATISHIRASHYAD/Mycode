#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    for expenditure in list_of_expenditure:
        total+=expenditure
    print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)