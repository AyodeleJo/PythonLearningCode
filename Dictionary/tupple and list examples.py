found = False
i = 0
names = ['Elena', 'Sonia', 'Mary', 'Lopamudra', 'Anita', 'Anastasia', 'Anita', 'Tanya', 'Jessica', 'Adriana', 'Kavita']
search = input('Enter name to find in list: ')
while not found and i < len(names):
    if search.title() == names[i]:
        found = True
        print(search, 'is number', i + 1, 'on the list.')
        break
    else:
        i += 1
if not found:
    print(search, 'is not on the list')

names_list = ['Iryna', 'Yu-Hang', 'Galina', 'Lakshmi', 'Stephani', 'Khadija', 'Usha', 'Iris', 'Cecila', 'Elahe',
              'Shabnam']
search_name = input('Enter a name to find in the list: ')
search_name = search_name.title()
if search_name in names_list:
    print(search_name, 'is number', names_list.index(search_name) + 1, 'on the list')
else:
    print(search_name, 'is not on the list')

"""Create two functions that find and returns the largest and 
the smallest numbers in a given list of positive numbers"""


def find_smallest(listofnums):
    smallest = 1000
    for num in listofnums:
        if num < smallest:
            smallest = num
    return smallest


def find_largest(listofnums):
    largest = 0
    for num in listofnums:
        if num > largest:
            largest = num
    return largest


nums = [5, 78, 99, 34, 22, 32, 12, 99, 89]
print(find_smallest(nums), find_largest(nums))


def find_smallest(listnums):
    return min(listnums)


def find_largest(listnums):
    return max(listnums)


nums = [5, 78, 99, 34, 22, 32, 12, 99, 89]
print(find_smallest(nums), find_largest(nums))


from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])

print(T[1][1])


class Book:
    # Question 2
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price

    # Question 3
    def view(self):
        return ("Book Title: ", self.Title, "Book Author: ", self.Author, "Book Price: ", self.Price)


# Question 4
MyBook = Book("Python Crash Course", "Eric Matthes", "23 $")
print(MyBook.view())
# The output: ('Book Title: ', 'Python Crash Course', 'Book Author: ', 'Eric Matthes', 'Book Price: ', '23 $')
