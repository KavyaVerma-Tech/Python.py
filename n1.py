'''class Bank:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
    def deposit(self, amount):
        self.amount = amount
        if self.amount > 0:
            self.balance += amount
            print(f"Amount deposited Rs. {self.balance}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        self.amount = amount
        if amount > 0:
            self.balance -= amount
            print(f"Amount withdrawn Rs. {self.balance}")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            print("Invalid Withdrawn amount")
    def balance_check(self):
        print(f"Current Balance: Rs. {self.balance}")
class Result:
    def __init__(self, std_name, std_id, std_marks):
        self.std_name = std_name
        self.std_id = std_id
        self.std_marks = std_marks
        self.total_marks = sum(std_marks)
        self.avg = self.total_marks / len(std_marks)
    def grade(self):
        if self.avg >= 90:
            return "+A"
        elif (self.avg < 90) and (self.avg <= 80):
            return "A"
        elif (self.avg < 80) and (self.avg <= 70):
            return "+B"
        elif (self.avg < 70) and (self.avg <= 60):
            return "B"
        elif (self.avg < 60) and (self.avg <= 50):
            return "C"
        elif (self.avg < 50) and (self.avg <= 40):
            return "D"
        else:
            return "E"
    def show_details(self):
        print("Students Result:")
        print(f"Student Name: {self.std_name}")
        print(f"Student ID: {self.std_id}")
        print(f"Student Marks: {self.std_marks}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Average: {self.avg}")
        print(f"Grade: {self.grade()}")
class Online_Shopping:
    def __init__(self, name, product_name, product_id, quantity, price, discount):
        self.name = name
        self.product_name = product_name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.items = []
    def add_on(self):
            total_price = self.price * self.quantity
            discount_amount = total_price * self.discount / 100
            final_price = total_price - discount_amount
            self.items.append({"product_name": self.product_name, "quantity": self.quantity, "final_price": final_price})
    def generate_bill(self):
        print(f"Name of the customer: {self.name}")
        grand_total = 0
        for item in self.items:
            print(f"{item['product_name']} x {item['quantity']} = ₹{item['final_price']}")
            grand_total += item["final_price"]
        print(f"Total Amount: ₹{grand_total}")'''
class Electricity_Bill:
    def __init__(self, name, id,  units):
        self.name = name 
        self.id = id
        self.units = units
    def calculate_bill(self):
        if self.units <= 100:
            amount = self.units * 5
        elif self.units <= 200:
            amount = (100 * 5) + (self.units - 100) * 7
        else:
            amount = (100 * 5) + (100 * 7) + (self.units - 200) * 10
        return amount
    def display_bill(self):
        total_amount = self.calculate_bill()
        print("----- Electricity Bill -----")
        print(f"Consumer Name   : {self.name}")
        print(f"Consumer ID     : {self.consumer_id}")
        print(f"Units Consumed  : {self.units}")
        print(f"Total Amount    : ₹{total_amount}")