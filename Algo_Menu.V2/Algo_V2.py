def menu ():
    print("1- Add \n2- Subtract \n3- Multiply \n4- Divide \n5- Exit")
    

def Add (a, b):
    return a + b 

def Subtract (a, b):
    return a - b 

def Multiply (a, b):
    return a * b 

def Divide (a, b):
    return a / b 


def calculate():

    while True:
        menu()  

        options = input("Enter any option by pressing a number(1/2/3/4/5): ")
        print("option:" + str(options))  
        
        if options == "5":
            break
        elif options in ["1", "2", "3", "4"]:
            first_num = float(input("Enter first number  : "))
            print("value 1 :" + str(first_num))    
            second_num = float(input("Enter second number  : "))
            print("Value 2 :" + str(second_num))    



            if(options == "1"):
                print(first_num, "+", second_num, "=", Add(first_num, second_num))
                
            elif(options == "2"):
                print(first_num, "-", second_num, "=", Subtract(first_num, second_num))
                
            elif(options == "3"):
                print(first_num, "*", second_num, "=", Multiply(first_num, second_num))
                
            elif(options == "4"):
                print(first_num, "/", second_num, "=", Divide(first_num, second_num))
        else:
            print("Error: Unknown option")        
                
calculate()    