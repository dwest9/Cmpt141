# David Emmanuel

# Doe869

# 11298443

# Jason Coutu



# str1 = input("Enter a verb ending in 'ing':  ")
# str2 = input("Enter a noun e.g 'A domestic animal':  ")
# str3 = input("Enter a verb (past tense):  ")
#
# print(f'As James was {str1} video game in his room, suddenly\n'
#       f'he heard a cracking noise as if someone was sneaking in into his room.\n'
#       f'As he looked who or what it was, immediately his {str2} "jack"\n'
#       f'started to bark at him which scared him a bit. To the essence that his gamepad immediately dropped off his hands and {str3} working.')

url = "www.cs.usask.ca"
# find the location of the first period in the url
url.find(".")
# count the number of periods in the url
# (function not covered in readings)
url.count(".")
# count the number of characters in the url after removing "www."
# (gotta be careful - don’t just assume a function does what you think!)
print(len(url.lstrip("cs")))