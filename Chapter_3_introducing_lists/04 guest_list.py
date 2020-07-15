# Guest List
invites = ['a', 'b', 'c']

print(invites[0] + " Come to my party!")
print(invites[1] + " Come to my  awesome party!")
print(invites[2] + " Come to my party! Please")

# Changing Guest List
declined_invite = 'b'
invites.remove(declined_invite)
print(declined_invite + " Could not make it")
invites.insert(1, 'd')
print(invites[1] + " Come to my super party!")

# More Guests
print('I have a larger table now!')
invites.insert(0, 'e')
invites.insert(1, 'f')
invites.append('g')

print(invites[0] + " Come to my party!")
print(invites[1] + " Come to my  awesome party!")
print(invites[2] + " Come to my party! Please")
print(invites[3] + " Come to my party!")
print(invites[4] + " Come to my  awesome party!")
print(invites[5] + " Come to my party! Please")

# Shrinking Guest List
print('I can only invite two people now')

removed_1 = invites.pop(0)
print(removed_1 + ' Really sorry')

removed_2 = invites.pop(1)
print(removed_2 + ' You cannot go')

removed_3 = invites.pop(3)
print(removed_3 + ' Sorry')

removed_4 = invites.pop(-1)
print(removed_4 + ' Please!')

# using del to remove the last two from list
print(invites[0] + ' You can still come')
print(invites[1] + ' You can still come too')

del invites[0]
del invites[-1]

# output to make sure that list is empty
print(invites)
