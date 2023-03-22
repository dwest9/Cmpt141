# David Emmanuel

# 11298443

# doe869

# jason coutu

def pattern_num(n):
   for row in range(4,0, -1):
      for col in range(1, row+1):
         if col == row:
            print(col, end='')
         else:
            print(col, end="->"*n)
      print()
n=int(input("Enter integer value for 'n': "))
pattern_num(n)
