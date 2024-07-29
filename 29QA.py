#How do you create a empty tuple on python ?
empty_tuple = tuple()
print(type(empty_tuple))


#Write a python program to unpack a tuple into several variables ?
numbers = (10,20,30,40)
number1, number2, number3, number4 = numbers
print(number1)
print(number2)
print(number3)
print(number4)

products = ("nail polish","sticker", "bangles")
product1,product2,product3 = products
print(product1)
print(product2)
print(product3)


#write a python program to add an item to the tuple ? 
numbers = (1,2,3,4)
my_list = list(numbers)
my_list.append(6)
new_numbers = tuple(my_list)
print(new_numbers)


#Write a python proram to convert tuple into a string ?

my_list = ("F","r","i","e",'n',"d")
my_string = ' '.join(my_list)
print(my_string)

#Write a python program to find most frequent element in tuple ?

grades = (10,20,40,50,60)
most_frequent = max(set(grades), key=grades.count )
print("most frequent element:",most_frequent )

