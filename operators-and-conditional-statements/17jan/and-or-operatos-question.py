# write a program to check if both the numbers are positive and atleast one of the numbers is greater than 5.
first_number = input()
first_number = int(first_number)
#first_number = int(input())
second_number = input()
second_number = int(second_number)
#second_number = int(input())
is_positive_number = (first_number > 0) and (second_number > 0)
is_greater_than_5 = (first_number > 5) or (second_number > 5) 
result = (is_positive_number) and (is_greater_than_5)
print(result)