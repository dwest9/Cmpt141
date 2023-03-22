

payment = float(input("Enter the payment for the case: "))
staffs = float(input("Enter the number of staff: "))

each_staff = (payment*0.75)/staffs

print("Phoenix Wright's 25% share of the fee is worth: ", '$' + str(payment*0.25))
print("The staff 25% share is: ", '$' + str(payment*0.75))
print("Each staff member takes home: ", '$' + str(each_staff))

