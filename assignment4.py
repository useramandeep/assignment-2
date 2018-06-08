#Q.1- Write a program to create a tuple with different data types and do the following operations.
#1. Find the length of tuples

keyword=(2,5,3,'Aman','Deep')
print(len(keyword))

#Q.2-Find largest and smallest elements of a tuples.
numbers=(3,4,6,2,43,)
print(max(numbers))
print(min(numbers))

#Q.3- Write a program to find the product of all elements of a tuple.

tuple_elements=(1*3*7,5*8*5)
print(tuple_elements)

#Q.1- Create two set using user defined values.

#1. Calculate difference between two sets.
set_a=set([1,2,4,5,])
set_b=set([4,5,])
set_final=set_a-set_b
print(set_final)

#2. Compare two sets.
set_a=set((1,2,3,4,5,6,7,8,9))
set_b=set((2,3,4,5))
set_c=set_a>=set_b
set_d=set_a<=set_b
print(set_c)
print(set_d)

#3. Print the result of intersection of two sets.
set_e=set_a&set_b
print(set_e)

#Q.1- Create a dictionary to store name and marks of 10 students by user input.
user_name=input("Enter Your Name")
user_age=input("Enter Your Age")
user_data={'Name':user_name,'Age':user_age}
print(user_data)

#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.


keyword=("MISSISSIPPI")
check_m=keyword.count("M")
check_i=keyword.count("I")
check_s=keyword.count("S")
check_p=keyword.count("P")
keyword_result={'Numbers Of M':check_m,'Numbers Of I':check_i,'Numbers Of S':check_s, 'Numbers Of p':check_p,}
print(keyword_result)

