#work experience challenge.py

DATA = """
100
200
300

400
250

100

600
700
900

300
"""

def find_value_of_largest_order():
    # Your code here
    highest_Current_Value = 0
    current_Total = 0
    my_Array = DATA.split("\n")
    for i in my_Array:
        if i != '':
            i = int(i)
            current_Total = current_Total + i
        else:
            if highest_Current_Value < current_Total:
                highest_Current_Value = current_Total
            current_Total = 0
    print(highest_Current_Value)

if __name__ == "__main__":
    find_value_of_largest_order()
