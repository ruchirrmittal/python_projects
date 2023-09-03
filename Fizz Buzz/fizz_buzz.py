def fizz_buzz(number):
    if number%15==0:
        return "fizz buzz"
    elif number%3==0:
        return "fizz"
    elif number%5==0:
        return "buzz"
    else:
        return str(number)
    
input("Press enter to start")
print()

next=0

while next<99:
    next+=1
    print(fizz_buzz(next))
    next+=1
    correct_answer=fizz_buzz(next)
    p1=input("Your move: \n")
    if p1 != correct_answer:
        print("{}".format(correct_answer))
        break
else:
    print("well done {}".format(next))   