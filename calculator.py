try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("what kind of operation do you want to perform.Press + for addition\nPress - for subtraction\nPress / for didvision\nPress * for multiplication")
    o = input("Enter Operation: ")
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a + b}")
        case "*":
            print(f"The result is: {a * b}") 
        case "/":
            print(f"The result is: {a / b}")   
except Exception as e:
    print("Enter a valid value of a and b")