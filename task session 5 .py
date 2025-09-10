def print_title_in_frame(title):
    border="+" + "-" * (len(title) + 4) +"+"
    print(border)
    print(f"|  {title}  |")
    print(border) 
print_title_in_frame("task session 5")
print("----------------------------------------------------------------------------" \
"----------------------------------------------------------------------------------")
print ("create a contact book")
contacts={"ebram":"01207869567","david":"01256794678","tony":'01234567890'}
print(contacts.keys())
print("contacts list:")
for name in contacts:
    print(name)
search_name=input("enter a name to search:")
if search_name in contacts:
    print=("the contacts [search_name]")
else:
    print("contact not found")
print("nothing beat a jet2 holiday :)") 
boys=[{"name":"ebram", "grades":[100,100,100]} ,{"name":"david","grades":[55,60,70]},{"name":"tony","grades":[50,50,50]}]
for boy in boys:
    average=sum(boy["grades"])/len(boy["grades"])
    print=(f"{boy["name"]}:{average:.2f}")
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"
number = 13
print(f"{number} is prime? {is_prime(number)}")

# Calculator Tests
print("5 + 3 =", calculator(5, 3, "add"))
print("5 - 3 =", calculator(5, 3, "subtract"))
print("5 * 3 =", calculator(5, 3, "multiply"))
print("5 / 0 =", calculator(5, 0, "divide"))
