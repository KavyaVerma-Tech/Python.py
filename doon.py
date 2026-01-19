'''a=5
b=2.345
c='anshika'
d=True
e=None
print(a,type(a),'\n',b,type(b),'\n',c,type(c),'\n',d,type(d),'\n',e,type(e))
name=input('enter name:')
age=int(input('enter age:'))
print("name of the user is :",name,'\nage of the user is:',age)
a=[1,23,45,67,89]
b=('as','df',3,4,5)
c={'ka',23,45}
d={'a':"apple",'b':"ball",'c':"cat"}
print(a,type(a),'\n',b,type(b),'\n',d,type(d))
a=12
b=12.34
print("int" ,a,"in float is: ", float(a),"float",b,"in int is: ", int(b))
a=input("enter number: ")
b=float(a)
c=int(a)
print(b,c)
a=[1,23,45]
b=(12,34,56)
print(tuple(a),list(b)) 
a=23
print(a,type(a),isinstance(a,float))
a=99
print(int(a),float(a),str(a),list[a])
a=[12,45,67]
b=a
print(id(a),id(b))
a=[12,23,34]   
b=(78,34,56)
c="wanna"
a[2]=67
print(a,b,c)
print("list is mutable while string and tuple is immutable")
sentence=input("enter a sentence")
wc=0
sp=0
cc=0
for i in sentence:
    cc+=1
    if i == " ":
     sp+=1
if sentence.strip() != "":
 wc= sp+1
print("characters: ",cc,'\n',"space: ",sp,'\n',"words: ",wc)
a=[]
sumnum=0
n=int(input("no of elements:"))
for i in range(0,n):
    b=int(input("enter any number:"))
    a.append(b)
print(a)
max=a[0]
min=a[0]
for i in a:
    if max<i:
        max=i
    if min>i:
        min=i
    sumnum+=i
    avg=sumnum/n
print("maximum:",max,"minimum:",min,"average:",avg)    
heisenberg_quote = "it ceases to exist without me"
words_by_walter = heisenberg_quote.split(' ')
first_letters = [word[0] for word in words_by_walter]
print(first_letters)
def extract_first_lrtter(sentence):
    word = sentence.split(" ")
    first_letters = [i[0] for i in word]
    return first_letters

sentence=input("enter any string:")
print(extract_first_lrtter(sentence))
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num = int(input("enter any no"))
print(factorial(num))
def assignQuarter(user_date):
    date_year = user_date[:4]
    date_month = user_date[5:7]
    if (date_month >= '01') & (date_month <= '03'):
        quarter = date_year + '-Q1'
    elif (date_month >= '04') & (date_month <= '06'):
        quarter = date_year + '-Q2'
    elif (date_month >= '07') & (date_month <= '09'):
        quarter = date_year + '-Q3'
    else :
        quarter = date_year + '-Q4'
    return quarter
sample = input("enter year month date")
s = assignQuarter(sample)
print(s)
def sum(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s
n = int(input("enter a no"))
print(sum(n))
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
n = int(input("enter a no: "))
print(fact(n))
def power(a,b):
    p = a ** b
    return p
a = int(input("enter a no: "))
b = int(input("enter the power: "))
print(power(a,b))
def length(string):
    l = 0
    for i in string:
        l += 1
    return l
string = input("enter any string: ")
print(length(string))
def count(string):
    v = 0
    c = 0
    for i in string:
        if (i=='a') | (i=='e') | (i=='i') | (i=='o') | (i=='u'):
            v += 1
        else:
            c +=1
    return v,c
string = input("enter any srting: ")
print(count(string))
def reverse(string):
    return string[::-1]
string = input("enter any string: ")
print(reverse(string))
def palindrome(string):
    temp = string
    rev=string[::-1]
    if ( rev== temp):
        return "palindrome"
    else:
        return "not palindrome"
    
print(palindrome("racecar"))
def digits(num):
    l = 0
    while num!=0:
        m = num%10
        l+=1
        num = num//10
    return l
num = int(input("enter any number: "))
print("no of digits in the number is: ")
print(digits(num))
def decimal_to_binary_manual(n):
    if n == 0:
        return "0"
    binary_num = ""
    while n > 0:
        remainder = n % 2
        binary_num = str(remainder) + binary_num 
        n = n // 2 
    return binary_num
decimal_num = 13
print(f"Manual conversion of {decimal_num}: {decimal_to_binary_manual(decimal_num)}")
def decimal_to_octal_manual(n):
    if n==0:
        return "0"
    while n>0:
        remainder = n % 8
        octal_num.append(str(remainder))
        n = n // 8
        return "".join(octal_num[::-1])
decimal_num = int(input("enter any no: "))
print(decimal_to_octal_manual(decimal_num))
def sum(list):
    s = 0 
    for i in list:
        s += i
    return s
n= int(input("no. of elements:"))
l=[]
for i in range(0,n):
    a= int(input("enter elements: "))
    l.append(a)
print(sum(l))
def average(list,n):
    s = 0
    for i in list:
        s += i
    avg=s/n
    return avg
l = []
n = int(input("enter no of elements: "))
for i in range(0,n):
    a = int(input("enter the elements: "))
    l.append(a)
print("average of the elements in list is : " , average(l,n))
def find(list):
    return max(list),min(list)
l= []
n = int(input("no of elements: "))
for i in range(0,n):
    a = int(input("enter the elements: "))
    l.append(a)
print(find(l))
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")
s1 = Student("Deepak", 101)
s1.display()
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(2000)
acc.deposit(200)
print(acc.get_balance())
class Person:
    def __init__(self,name):
        self.name = name
    def speak(Self):
        print("I'm a person")
class Teacher(Person):
    def speak(self):
        print(f"I'm a teacher. My name is {self.name}")
t = Teacher("Anil")
t.speak()
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
animals = [Dog(),Cat()]
for a in animals:
    a.sound()
class Demo:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
d = Demo()
class MathOps:
    def add(self,a,b=0,c=0):
        return a+b+c
m = MathOps()
print(m.add(2))
print(m.add(2,3))
print(m.add(2,3,4))
class Parent:
    def show(self):
        print("This is parent")
class Child(Parent):
    def show(self):
        print("This is chlid")
obj = Child()
obj.show()
class Base:
    def show(self):
        print("Base class show")
class Derived(Base):
    def show(self):
        super().show()
        print("Derived class show")
d = Derived()
d.show()
class Employee:
    company = "ABC Ltd"
    def __init__(self,name):
        self.name = name
e1 = Employee("Ravi")
e2 = Employee("Amit")
print(e1.company, e1.name)
print(e2.company, e2.name)
class Student:
    name = "Deepak"
    roll = 101
s = Student()
print(s.name)
print(s.roll)
class Student:
    def display(self):
        print("Welcome to Python OOP")
s = Student()
s.display()
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def show(self):
        print(self.name, self.roll)
s1 = Student("Deepak", 101)
s2 = Student("Amit", 102)
s1.show()
s2.show()
class Employee:
    def __init__(self, name):
        self.name = name
e1 = Employee("Keshav")
e2 = Employee("Anitesh")
print(e1.name)
print(e2.name)
class College:
    college_name = "NIT"
    def __init__(self, student):
        self.student = student
s1 = College("Deepak")
s2 = College("Amit")
print(s1.college_name, s1.student)
print(s2.college_name, s2.student)
class Calculator:
    def add(self, a, b):
        return a + b
c = Calculator()
print(c.add(5,10))
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Deepak")
print(s.name)
s.name = "Rahul"
print(s.name)
class Student:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)
s = Student("Deepak")
s.show()
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self, amt):
        self.balance += amt
    def show(self):
        print("Balance:",self.balance)
acc = BankAccount(5000)
acc.deposit(2000)
acc.show()
class Student:
    def __init__(self, name):
        self.name = name
std = [Student("A"), Student("B"), Student("C")]
for s in std:
    print(s.name)
class Demo:
    def __int__(self):
        print("Object Created")
    def __del__(self):
        print("Object Deleted")
d = Demo()
del d
class Demo:
    def __init__(self):
        print("Constructor called")
obj = Demo()
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
num = int(input("enter any number: "))
print(factorial(num))
def prime(num):
    for i in range(2,num+2):
        num = num % i
    if num == 0:
            return "Prime"
    else:
            return "Not Prime"
num = int(input("enter any number: "))
print(prime(num))
def GCD(a,b):
    if a > b:
        s = b
    else:
        s = a
    for i in range(1,s+1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    return gcd        
a = int(input("enter a: "))
b = int(input("enter b: "))
print(GCD(a,b))
def power(num,exp):
    for i in range(1,exp+1):
        p = num ** i
    return p
num = int(input("enter any number: "))
exp = int(input("enter the exponent: "))
print(power(num,exp))
def power_recursion(base,expo):
    if expo == 0:
        return 1
    else:
        return base * power_recursion(base,expo-1)
base = int(input("enter any number: "))
expo = int(input("enter the exponent: "))
print(power_recursion(base,expo))
def reverse(string):
        return string[::-1]
string = input("enter any string: ")
print(reverse(string))
def palindrome(string):
    rev = string[::-1]
    if rev == string:
        return "Palindrome"
    else:
        return "Not Palindrome"
string = input("enter any string: ")
print(palindrome(string))
def fibo(n):
    print(0)
    print(1)
    a = 0
    b = 1
    f = 0
    for i in range(1,n+1):
        f = a + b
        print(f)
        a = b
        b = f
n = int(input("enter the no of terms: "))
print(fibo(n))
def count(string):
    v = 0
    for i in string:
        if (i == 'a') | (i == 'e') | (i == 'i') | (i == 'o') | (i == 'u'):
            v += 1
    return v
string = input("enter any string: ")
print(count(string))
def maximum(list):
    return max(list)
l = []
n = int(input("enter the number of terms: "))
for i in range(1,n+1):
    a = int(input("enter the element: "))
    l.append(a)
print(maximum(l))
def sum(list):
    s = 0
    for i in list:
        s += i
    return s
l = []
n = int(input("enter the number of elements:"))
for i in range(1,n+1):
    a = int(input("enter the element: "))
    l.append(a)
print(sum(l))
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("enter any number: "))
print(even_odd(num))
def convert(degree):
    f = degree * (9/5) + 32
    return f
degree = int(input("enter the degree in celsius: "))
print("degree in fahrenheit is :")
print(convert(degree))
def length(list):
    l = 0
    for i in list:
        l += 1
    return l
list = []
n = int(input("enter the no of elements: "))
for i in range(1,n+1):
    a = int(input("enter the elment: "))
    list.append(a)
print(length(list))
def square(list):
    sq_list = []
    for i in list:
        sq_list.append(i**2)
    return sq_list
list = []
n = int(input("enter the no of elements: "))
for i in range(1,n+1):
    a = int(input("enter the elment: "))
    list.append(a)
print(square(list))
def sum_natural_numbers(n):
    s = 0
    for i in n:
        s += i
    return s
n = int(input("enter the no of natural numbers: "))
l = []
for i in range(1,n+1):
    a = int(input("enter the number: "))
    l.append(a)
print(sum_natural_numbers(l))
def merge(a,b):
    m = {**a , **b}
    return m
a = {"apple":'a',"ball":'b'}
b = {"cat":'c',"dog":'d'}
print(merge(a,b))
def unique_elements(list):
    unique_set = set(list)
    unique_list = list(unique_set)
    return unique_list
n = int(input("enter the no of elements: "))
l = []
for i in range(1,n+1):
    a = int(input("enter the elements: ")) 
    l.append(a)
print(f"Unique elements: {unique_elements(l)}")
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        def display(self):
            print(f"Name: {self.name}")
            print(f"id: {self.id}")
            print(f"Salary: Rs. {self.salary}, .2f")
class Manager(Employee):
    def __init__(self, name, id, salary,department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.department)
class Developer(Employee):
    def __init__(self, name, id, salary, programming_language):
        self.name = name
        self.id = id
        self.salary = salary
        self.programming_language = programming_language
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.programming_language)
class Intern(Employee):
    def __init__(self, name, id, salary, duration):
        self.name = name
        self.id = id
        self.salary = salary
        self.duration = duration
    def display(self):
        make, model, year
a = Manager("Ayesha", "CE-3401", 40000, "Computer Science")
b = Developer("Arpit", "CE-1278", 12000, "Python")
c = Intern("Akhil", "CE-4567", 5000, "1 Month")
print("Manager Details: ")
a.display()
print("Developer Details: ")
b.display()
print("Intern Details: ")
c.display()
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print(f"{self.make}, {self.model}, engine is running")
    def start(self):
        print(f"{self.make}, {self.model}, engine is running")
class Car(Vehicle):
    def __init__(self, make, model, year,num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.num_doors = num_doors
    def str(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.num_doors)
class Bike(Vehicle):
    def __init__(self, make, model, year, type):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
    def str(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.type)
class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.capacity = capacity
    def str(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.capacity)
a = Car("Toyota", "Camry", "2025", 4)
b = Bike("Trek", "Marlin", "2024", "Mountain")
c = Truck("Ford", "F-150", "2023", "1.5 Tons")
print("Cars Details: ")
a.str()
print("Bike Details: ")
b.str()
print("Truck Details: ")
c.str()
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
    def display_products(self):
        print(self.name)
        print(self.price)
        print(self.sku)
class Electronics(Product):
    def __init__(self, name, price, sku, warranty):
        self.name = name
        self.price = price
        self.sku = sku
        self.warranty = warranty
    def display_products(self):
        print(self.name)
        print(self.price)
        print(self.sku)
        print(self.warranty)
class Clothing(Product):
    def __init__(self, name, price, sku, size):
        self.name = name
        self.price = price
        self.sku = sku
        self.size = size
    def display_products(self):
        print(self.name)
        print(self.price)
        print(self.sku)
        print(self.size)
class Grocery(Product):
    def __init__(self, name, price, sku, expiry_date):
        self.name = name
        self.price = price
        self.sku = sku
        self.expiry_date = expiry_date
    def display_products(self):
        print(self.name)
        print(self.price)
        print(self.sku)
        print(self.expiry_date)
a = Electronics("Television", "Rs. 5000", "A123", "1 Year")
b = Clothing("Shirt", "Rs. 500", "B456", "Medium" )
c = Grocery("Chips", "Rs. 20", "C9", "1-12-2026")
print("Electronics Details:")
a.display_products()
print("Clothing Details:")
b.display_products()
print("Grocery Details:")
c.display_products()
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount: Rs. {amount}, New Balance: Rs. {self.balance}")
            return True
        return False
    def withdraw(self,amount):
        if (amount > 0) and (self.balance >= amount):
            self.balance -= amount
            print(f"Withdraw amount: Rs. {amount}, New Balance: Rs. {self.balance}")
            return True
        print("Insufficient Balance")
        return False
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest Applied. Balance is now Rs. {self.balance}")
class CurrentAccount(Account):
    def  __init__(self, account_number, balance, overdraft_limit):
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if (amount > 0) and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdraw amount: Rs. {amount}, New Balance: Rs. {self.balance}")
            return True
        print("Failed")
        return False
class LoanAccount(Account):
    def  __init__(self, account_number, balance, loan_amount):
        self.account_number = account_number
        self.balance = balance
        self.loan_amount = loan_amount
    def make_repayment(self, amount):
        self.deposit(amount)
        if self.balance == 0:
            print("Loan has been successfully repaid!")
        elif self.balnce > 0:
            print("Loan overpaid")
savings = SavingsAccount("S123", "Rs. 20000", 2.5)
current = CurrentAccount("A456", "Rs. 40000", 1000)
loan = LoanAccount("C789", "60000", "Rs. 20000")
print("-" * 30)

savings.apply_interest()
print("-" * 30)
current.withdraw(300)
print("-" * 30)
loan.make_repayment(1000)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Doctor(Person):
    def __init__(self, name, age, gender, specialisation):
        self.name = name
        self.age = age 
        self.gender = gender
        self.specialisation = specialisation
    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.specialisation)
class Patient(Person):
    def __init__(self, name, age, gender, ailment):
        self.name = name
        self.age = age 
        self.gender = gender
        self.ailment = ailment
    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.ailment)
class Nurse(Person):
    def __init__(self, name, age, gender, shift):
        self.name = name
        self.age = age 
        self.gender = gender
        self.shift = shift
    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.shift)
a = Doctor("Ansh", 40, "Male", "ENT")
b = Patient("Ankul", 8, "Male", "Ear Infection")
c = Nurse("Anshika", 31, "Female", "1st Shift")
print("Doctor Details:")
a.show_info()
print("Patient Details:")
b.show_info()
print("Nurse Details:")
c.show_info()
class Person:
    def __init__(self, name, id, contact):
        self.name = name
        self.id = id 
        self.contact = contact
    def get_details(self):
        print(self.name)
        print(self.id)
        print(self.contact)
class Student(Person):
    def __init__(self, name, id, contact, course):
        self.name = name
        self.id = id 
        self.contact = contact
        self.course = course
    def get_details(self):
        print(self.name)
        print(self.id)
        print(self.contact)
        print(self.course)
class Faculty(Person):
    def __init__(self, name, id, contact, department):
        self.name = name
        self.id = id 
        self.contact = contact
        self.department = department
    def get_details(self):
        print(self.name)
        print(self.id)
        print(self.contact)
        print(self.department)
class Staff(Person):
    def __init__(self, name, id, contact, role):
        self.name = name
        self.id = id 
        self.contact = contact
        self.role = role
    def get_details(self):
        print(self.name)
        print(self.id)
        print(self.contact)
        print(self.role)
a = Student("Ansh", "CE-40", 1234556678, "Computer Science")
b = Faculty("Ankul", "MS-8", 1998765233, "Technology")
c = Staff("Anshika", "NS-31", 7886540900, "Watchman")
print("Student Details:")
a.get_details()
print("Faculty Details:")
b.get_details()
print("Staff Details:")
c.get_details()
class Menultem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_price(self):
        print(self.price)
class Beverage(Menultem):
    def __init__(self,name,price, volume):
        self.name = name
        self.price = price
        self.volume = volume
    def get_price(self):
        print(self.price)
        print(self.volume)
class Fooditem(Menultem):
    def __init__(self,name,price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
    def get_price(self):
        print(self.price)
        print(self.ingredients)
class Dessert(Menultem):
    def __init__(self,name,price, calories):
        self.name = name
        self.price = price
        self.calories = calories
    def get_price(self):
        print(self.price)
        print(self.calories)
a = Beverage("Sprit", "Rs. 30", "750ml")
b = Fooditem("Salad", "Rs. 100", "Carrot,Cucumber,Beetroot,Black pepper")
c = Dessert("Ice-cream", "Rs. 30", "3.5g")
print("Beverage Details:")
a.get_price()
print("Fooditem Details:")
b.get_price()
print("Dessert Details:")
c.get_price()
class Payment:
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        pass
class UPI(Payment):
    def __init__(self, amount, account_id):
        self.amount = amount
        self.account_id = account_id
    def pay(self):
        print("Payment via UPI")
        print(f"Payment of amount: {self.amount} is successful through UPI id: {self.account_id}")
class Card(Payment):
    def __init__(self, amount, card_no, expiry, cvv):
        self.amount = amount
        self.card_no = card_no
        self.expiry = expiry
        self.cvv = cvv
    def pay(self):
        print("Payment via card")
        print(f"Payment of amount: {self.amount} is successful through card ending in: {self.card_no[-4:]}")
class NetBanking(Payment):
    def __init__(self, amount, bank_name, account_id):
        self.amount = amount
        self.bank_name = bank_name
        self.account_id = account_id
    def pay(self):
        print("Payment via netbanking")
        print(f"Payment of amount: {self.amount} is successful through netbanking ({self.bank_name}) through user id: {self.account_id}")
payments = [ UPI(150.00, "QWE345677"), Card(1000.00, "ASD6776401234567", "04-12-2028", 123), NetBanking(500.00, "SBI", "MN000766J") ]
for p in payments:
    p.pay()
class circle:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour
    def draw(self):
        print(f"Drawing a circle of Colour: {self.colour} and Radius: {self.radius}")
class rectangle:
    def __init__(self, length, breath, colour):
        self.length = length
        self.breath = breath
        self.colour = colour
    def draw(self):
        print(f"Drawing a rectangle of Colour: {self.colour} and Length: {self.length}, Breath: {self.breath}")
class triangle:
    def __init__(self, a, b, c, colour):
        self.a = a
        self.b = b
        self.c = c
        self.colour = colour
    def draw(self):
        print(f"Drawing a triangle of Colour: {self.colour} and Sides: 1st: {self.a}, 2nd: {self.a}, 3rd: {self.c}")
drawing = [ circle(3.0, "Blue"), rectangle(4, 9, "Yellow"), triangle(4, 8, 10, "Green")]
for z in drawing:
    z.draw()
class Email:
    def __init__(self, message):
        self.message = message
    def notification(self):
        print(f"Message recieved via email: {self.message}")
class SMS:
    def __init__(self, message):
        self.message = message
    def notification(self):
        print(f"Message recieved via sms: {self.message}")
System = [ Email("HELLO!!"), SMS("BYE!!")]
for s in System:
    s.notification()
class audio:
    def __init__(self, filename):
        self.filename = filename
    def play(self):
        print(f"Playing audio file: {self.filename}")
class video:
    def __init__(self, filename):
        self.filename = filename
    def play(self):
        print(f"Playing video file: {self.filename}")
multimedia_player = [ audio("Fav_Song.mp3"), video("Animal.mp4")]
for m in multimedia_player:
    m.play()
class car:
    def __init__(self,  name, speed, distance):
        self.name = name 
        self.speed = speed 
        self.distance = distance
    def move(self):
        print(f"{self.name} covered {self.distance} distance with speed {self.speed}")
class bike:
    def __init__(self,  name, speed, distance):
        self.name = name 
        self.speed = speed 
        self.distance = distance
    def move(self):
        print(f"{self.name} covered {self.distance} distance with speed {self.speed}")
class bus:
    def __init__(self,  name, speed, distance):
        self.name = name 
        self.speed = speed 
        self.distance = distance
    def move(self):
        print(f"{self.name} covered {self.distance} distance with speed {self.speed}")
Transport = [ car("Honda", "30 km/h", "20 km"), bike("Enfield", "50 km/h", "20 km"), bus("Volvo", "70 km/h", "20 km")]
for t in Transport:
    t.move()
class retail:
    def __init__(self, name, item_purchased, date, purchase_amount):
        self.name = name
        self.item_purchased = item_purchased
        self.date = date
        self.purchase_amount = purchase_amount
    def billing(self):
        print("Details of the Retailer:")
        print(f"Name of the purchaser: {self.name} \nIteam purchased: {self.item_purchased} on {self.date} \nPurchase amount is: {self.purchase_amount}")
class wholesale:
    def __init__(self, name, item_purchased, date, purchase_amount):
        self.name = name
        self.item_purchased = item_purchased
        self.date = date
        self.purchase_amount = purchase_amount
    def billing(self):
        print("Details of the Wholesaler:")
        print(f"Name of the purchaser: {self.name} \nIteam purchased: {self.item_purchased} on {self.date} \nPurchase amount is: {self.purchase_amount}")
class online:
    def __init__(self, name, item_purchased, date, purchase_amount):
        self.name = name
        self.item_purchased = item_purchased
        self.date = date
        self.purchase_amount = purchase_amount
    def billing(self):
        print("Details of the Online:")
        print(f"Name of the purchaser: {self.name} \nIteam purchased: {self.item_purchased} on {self.date} \nPurchase amount is: {self.purchase_amount}")
system = [ retail("Pankaj", "Cold Drinks", "02-01-2026", 600.00), wholesale("Ishap", "Notebooks", "14-01-2026", 500.00), online("Esha", "Shoes", "05-01-2026", 700.00)]
for s in system:
    s.billing()
class Post:
    def __init__(self, user, time, content):
        self.user = user
        self.time = time
        self.content = content
    def display(self):
        print(f"Posted by {self.user} at {self.time}")
class Image(Post):
    def __init__(self, user, time, content):
        self.user = user
        self.time = time
        self.content = content
    def display(self):
        super().display()
        print(f"Content posted: {self.content}")
class Video(Post):
    def __init__(self, user, time, content):
        self.user = user
        self.time = time
        self.content = content
    def display(self):
        super().display()
        print(f"Content posted: {self.content}")
class Text(Post):
    def __init__(self, user, time, content):
        self.user = user
        self.time = time
        self.content = content
    def display(self):
        super().display()
        print(f"Content posted: {self.content}")
media = [ Image( "Mishty", "7:08 a.m.", "scenery.mp3"), Video( "Harleen", "12:01 a.m.", "birthday_party.mp4"), Text( "Ishap", "11:14 p.m.", "Maintain Your Peace")]
for m in media:
    m.display()
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def cook(self):
        print(f"Cooking {self.name} of price {self.price} baked in oven")
class Burger:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def cook(self):
        print(f"Cooking {self.name} of price {self.price} grilled")
class Salad:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def cook(self):
        print(f"Cooking {self.name} of price {self.price} chopped")
menu = [ Pizza("Margherita Pizza", "Rs. 500.00"), Burger("Classic Cheese Burger", "Rs. 250.00"), Salad("Veggie Supreme", "Rs. 400")]
for m in menu:
    m.cook()
class Bike:
    def __init__(self, name, fuel, maintainance, security):
        self.name = name
        self.fuel = fuel
        self.maintainance = maintainance
        self.security = security
    def calculate_rent(self):
        price = self.fuel + self.maintainance + self.security
        print(f"Rent of {self.name} bike is Rs. {price}")
class Car:
    def __init__(self, name, capacity, fuel, maintainance, security):
        self.name = name
        self.capacity = capacity
        self.fuel = fuel
        self.maintainance = maintainance
        self.security = security
    def calculate_rent(self):
        price = self.fuel + self.maintainance + self.security
        print(f"Rent of {self.name} car is Rs. {price}")
class Bus:
    def __init__(self, name, capacity, fuel, maintainance, security):
        self.name = name
        self.capacity = capacity
        self.fuel = fuel
        self.maintainance = maintainance
        self.security = security
    def calculate_rent(self):
        price = self.fuel + self.maintainance + self.security
        print(f"Rent of {self.name} bus is Rs. {price}")
bike = Bike("Enfield", 500.00, 2000.00, 5000.00)
car = Car("i20", "5 Seater", 1000.00, 5000.00, 10000.00)
bus = Bus("Volvo", "32 Seater", 2000.00, 5000.00, 10000.00)
vehicles = [bike, car, bus]
for v in vehicles:
    v.calculate_rent()
class DHL:
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
    def ship(self):
        print("Shipping via DHL")
        print(f"Contacting DHl API to ship Parcel {self.tracking_id}")
        print("Shipment successful. Status: Processed, URL: https://dhl.com")
class FedEx:
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
    def ship(self):
        print("Shipping via FedEx")
        print(f"Contacting FedEx API to ship Parcel {self.tracking_id}")
        print("Shipment successful. Status: Label Created, URL: https://FedEx.com")
class UPS:
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
    def ship(self):
        print("Shipping via UPS")
        print(f"Contacting UPS API to ship Parcel {self.tracking_id}")
        print("Shipment successful. Status: Label Created, URL: https://FedEx.com")
carriers = [ DHL("ORDER12345"), FedEx("ORDER12345"), UPS("ORDER12345")]
for c in carriers:
    c.ship()
class Bot:
    def reply(self):
        pass
class WeatherBot(Bot):
    def reply(self): 
        print("It's a sunny day!")
class NewsBot:
    def reply(self):
        print("AI is the future")
class JokeBot:
    def reply(self):
        print("What do you call a pasta? Im-pasta!")
chatbot = [ WeatherBot(), NewsBot(), JokeBot()]
for c in chatbot:
    c.reply() 
import math
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            print("Error! Denominator cannot be zero")
        common = math.gcd(numerator,denominator)
        self.numerator = numerator
        self.denominator = denominator
        if denominator < 0:
            self.numerator = -numerator
            self.denominator = -denominator
    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)
    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)
    def __truediv__(self,other):
        if other.numerator == 0:
            print(("Error! Cannot divide by zero"))
        numerator = (self.numerator * self.denominator) 
        denominator = (other.numerator * other.denominator )
        return Fraction(numerator,denominator)
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
f1 = Fraction(1,2)
f2 = Fraction(3,4)
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")
class Score:
    def __init__(self):
        self.new_score = 0
    def add(self, points):
        self.points = points
        self.new_score += points
        return self.new_score
    def high(self, a, b):
        self.a = a
        self.b = b
        a = self.new_score
        if a > b:
            return "a is Highest"
        return "b is Highest" 
s = Score()
print(s.add(5))
print(s.add(134))
print(s.high(123,443))
class Temperature:
    def __init__(self, value):
        self.value = value
    def __sub__(self, other):
        return self.value - other.value
    def __gt__(self, other):
        if self.value > other.value:
            return "True" 
        return "False"
T1 = Temperature(50)
T2 = Temperature(87)
print(T1 - T2)
print(T1 > T2)'''
class Playlist:
    def __init__(self):
        self.songs = []
    def add_on(self, song):
        self.songs.append(song)
        return self.songs
    def length(self):
        return len(self.songs)
p = Playlist()
p.add_on("Fakira")
p.add_on("Excuses")
print(p.songs)
print(p.length())