# EXERCISE 1
x = int(input("enter the ist integer"))
y = int(input("enter the second number"))
if (x * y  => 1000):
    return x * y
return sum

# EXERCISE 2

previous_no = 0
for i in range(1, 11):
    current_no = i
    sum_of_no = previous_no + current_no
    print(f"current_no: {current_no}), previous_no: {previous_no}, sum: {sum_of_no}")
    previous_no = current_no
# EXERCISE 3
def display_even_character(string):
    for i in range(len(string)):
        if i % 2 == 0:        
            print(string[i])
        
user_input = ("Enter the string: ")
display_even_character(user_input)

# EXERCISE 4

def remove_characters(string, n):
    if n >= len(string):
        return ""
    else:
        return string[n:]

user_input = input("enter the string: ")
n = 3
new_string = remove_characters(user_input, n)
print(new_string)

def remove_character(string, n):
    if n >= len(string):
        return ""
    else:
        return string[n:]

user_input = input("Enter the string: ")
n = 4
new_string = remove_character(user_input, n)  # Corrected function name
print(new_string)


# EXRECISE 5
def same_different_number(lst):
    if lst[0] == lst[-1]:
        print("First And Last Number Are Same")
    else:
        print("not same")
input_list = [4,5,6,7,8,4,5]
same_different_number(input_list)

# EXERCISE 6
list = [4, 5, 35, 25, 7, 8, 50]
for i in list:
    if i % 5 == 0:
        print(i)


# EXERCISE 7
for i in range(1, 6):
    print(str(i) * i)

# EXERCISE 8
def is_palindrome(num):
    num1 = str(num)
    if num1 == num1[::-1]:
        return True
    else:
        return False
num = int(input("Enter The Number"))
if is_palindrome(num):
    print("Ths Number Is Palindrome")
else:
    print("This Number Is Not Palindrome")

# EXERCISE 9

list1 = [3, 6, 5, 7, 5, 4, 8]
list2 = [4, 6, 7, 8, 10,9,12]
new_list = []
for num in list1:
    if num % 2 != 0:
        new_list.append(num)
for num1 in list2:
    if num1 % 2 == 0:
        new_list.append(num1)
print(new_list)


# EXERCISE 10

def reverse_num(number):
    number = str(number)[::-1]
    return ','.join(number)
num1 = int(input("Enter The Integer: "))
num2 = reverse_num(num1)
print(num2)



