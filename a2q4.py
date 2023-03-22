# David Emmanuel

# 11298443

# doe869

# jason coutu


def baseboard(width, length):
    '''
    computing the total cost of baseboard with the given parameters

    :param width: An integer/float for the width of the room in foot(ft)
    :param length: An integer/float for the length of the room in foot(ft)
    obtaining the cost of baseboard from input given
    :return: the total cost of baseboard
    '''
    cost_of_baseboard = int(input("input the cost of a linear foot of baseboard ($): "))
    perimeter = 2*(width + length)
    total_cost1 = cost_of_baseboard * perimeter
    return total_cost1

width = float(input("What is the width of the room(ft): "))
length = float(input("What s the length of the room(ft): "))



def carpet(width, length):
    '''
    computing the total cost of carpet with the given parameters

    :param width: An float/integer for the width of the room in foot(ft)
    :param length: An integer/float for the length of the room in foot(ft)
    obtaining the cost of carpet from input given
    :return: the total cost of carpet
    '''
    cost_of_carpet = int(input("input the cost of a square foot carpet ($): "))
    area = width * length
    total_cost2 = cost_of_carpet * area
    return total_cost2


def cost(cost1, cost2):
    '''
    Computing the total cost of both baseboard cost and carpet cost
    :param cost1: calling the function of baseboard
    :param cost2: calling the function of carpet
    :return: returning the overall total cost of the renovation
    '''
    cost1 = baseboard(width,length)
    cost2 = carpet(width,length)
    Total_Cost = cost1 + cost2 + 500
    return Total_Cost
Cost = cost(0,0)
print(f'For room of {width} and {length} the cost of renovation is $ {Cost}')

