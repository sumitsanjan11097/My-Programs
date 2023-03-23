


def bill_generator():
    real = 0

    print("Enter the price of items you bought:")
    while True:
        op = input("Enter the price or q to quit:\n")
        while True:
            if op.isdigit():
                op = int(op)
                real += op
                break
            elif op == "q":
                

                break
            else:
                continue
        
        if op == "q":
            print(f"Your total bill is {real}.")
            
            break
        else:
            print(f"The total price now is {real}.")
    print("Thank you for shopping!")
    

if __name__ == "__main__":
    bill_generator()
