#tuple
numbers = (20,30,40,50,-10)
print(type(numbers))
print(numbers)

#real time example for tuple
product1 = (23465,"ear buds", 10.999)
product2 = (412378,"ear phones",3.999)
print(product1)
print(product2[1])

#sring methodin tuple
Books = ("novels book","friction book","General knowledge","Drawing book")
print(Books[1])
Book = list(Books)
Book[3] = "colouring book"
print(Book)
Books = tuple(Book)
print(Books)
print(type(Books))

#count

count = 0
for Book in Books:
    count = count + 1
    print(count)



for Book in Books:
 if "novels book" == Book:
  print(True)


numbers = (1,2,3,4)
number = numbers.index(3)
print(number)


numbers = (1,2,3,4)
numbers1 = (5,6,7,8)
print(numbers+numbers1)
print(numbers*4)

#delete
numbers = (1,2,3,4)
numbers.delete
print(numbers)