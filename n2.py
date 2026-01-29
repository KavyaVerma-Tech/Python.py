'''import n1
account1 = n1.Bank("M101", 5000)
account1.deposit(500)
account1.withdraw(1000)
account1.balance_check()
import n1
name = input("Enter the name: ")
id = input("Enter the id:")
m = []
n = int(input("enter the number of subjects:"))
for i in range(0,n):
    a = int(input("Enter the element: "))
    m.append(a)
Student1 = n1.Result(name, id, m)
Student1.show_details()
import n1
user1 = n1.Online_Shopping("Abhilasha", "Laptop", "M10-34", 66000, 1, 8)
user2 = n1.Online_Shopping("Kirti", "Tablet", "B6-98", 40000, 1, 5)
user1.add_on()
user2.add_on()
user1.generate_bill()
user2.generate_bill()'''
import n1
bill1 = n1.Electricity_Bill("Abhilasha", "E1023", 250)
bill1.display_bill()