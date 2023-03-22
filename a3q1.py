# # David Emmanuel
#
# # 11298443
#
# # doe869
#
# # jason coutu
#
#
# email = input("Enter your email: ")
# length = len(email)
# sign = int(email.find("@"))
# username = email[0:sign]
# dot = int(email.find("."))
# TLD = email[dot:]
# print("username: " + username)
# print("TLD: " + TLD)
#
# import turtle as turtle
# def drawCircles(n):
# circlesDrawn = 0 # number of circles drawn so far
# while circlesDrawn < n: # while we haven’t drawn n circles
# turtle.goto(circlesDrawn *50, 0) # move the turtle
# turtle.down() # put the turtle ’s pen down
# turtle.circle (20) # draw a circle of radius 20 pixels
# turtle.up() # pick up the turtle ’s pen
# # add 1 to the number of circles drawn
# circlesDrawn = circlesDrawn + 1

# defines the function only:
# def introductions(greeting ):
#     print(greeting)
#     x = input("Please enter your name: ")
#     print("Hello ,", x)
# # this function call actually calls the function ,
# # which executes its code.
# introductions("Welcome to my Python program!")

# defines the function only:
# def introductions(greeting ):
#     print(greeting)
#     x = input("Please enter your name: ")
#     print("Hello , " + x)
#     return x
# # this function call actually calls the function ,
# # which executes its code.
# introductions("Welcome to my Python program!")

# t="this is where we were before we left for the market"
# r="94809438939"
# print(t.isupper())
# print(r.isdigit())

a=["1", "Two", "Three"]
a.append("Four")
print(a)