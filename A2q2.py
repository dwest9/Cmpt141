# David Emmanuel

# 11298443

# doe869

# jason coutu

def calculate_speed(Distance, Time):
    '''
    compute the speed in km/h travelled by an object

    desired distance travelled: An integer for the distance travelled
    desired time taken: An integer for the time taken
    :return: The total speed travelled by the object as float number
    '''
    average_speed = distance/time
    return average_speed
distance = int(input("Enter desired distance(km): "))
time = int(input("Enter desired time(hours): "))

speed_one = calculate_speed (0, 0)
print((f'In other to travel {distance}km in {time}hrs, you must travel {speed_one}km/h'))


# number = int(input("Enter any number: "))
#
# count = 10
# while count>=1:
#     product=number*count
#     print(number, "x", count, "=", product)
#     count=count-1

# for i in range(1,101):
#     print(i)
# sum=0
# for num in range(1,101):
#     sums=sum+num
#     print(1+sums)

number = int(input('Enter a number for sum: '))
count = 1
for count in range(1, 101):
    sum = number + count
    print(number, "+", count, "=", sum)

