# def my_function(x, /):
#     print(x)

# my_function(10)


def create_order(item_name, quantity, delivery_address):
    print(item_name, quantity, delivery_address)

# create_order('Laptop', 2, 'New York')
    
# def my_function(*, x):
    # print(x)
# 
# my_function(x=10)

def calculate_bill(bill_amount, tax_rate, tip_percentage=0.15, additional_fees=0):
    total =  bill_amount + (bill_amount * tax_rate) + (bill_amount * tip_percentage) + additional_fees
    print(total)

# calculate_bill(100, 0.06, 0.10, 10)
    
def myfun (*abc):
    for arg in abc:
        print(arg)

# myfun('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
        
def printf(*args):
    for arg in args:
        print(arg, end =" ")

x=2
y=x**23
printf("hello \n", "x = ", x, "y = ", y, "z = ", y%3 , "\n")

def my_fun(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

def myFuns(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print("%s==%s"%(key,value))

myFuns(first='Neil',mid='Nitin',last='Mukesh')