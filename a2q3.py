# David Emmanuel

# Doe869

# 11298443

# Jason Coutu

def fence_cost(length,width,height,cost):
    '''
    Computing the total cost fence cost to be used to paint

    :param length: inputing the length in meters
    :param width: inputing the width in meters
    :param height: inputing the height in meters
    :param cost: calculating the cost to paint
    :return: returning the total cost in dollars
    '''
    total_cost =float(((length * height)*2) + ((width * height)*4) * cost)
    return total_cost

width_paint = float(input("Enter the width of the fence area in meters: "))
length_paint = float(input("Enter the length of the fence area in meters: "))
height_paint = float(input("Enter the height of the fence in meters: "))
cost_entered = float(input("Enter the cost of paint per square meter: "))

print('The fence will cost $' + (str(fence_cost(width_paint,length_paint, height_paint,cost_entered))) +' to paint')