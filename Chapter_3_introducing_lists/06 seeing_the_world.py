# Make an unordered list
destination = ['New York', 'Tokyo', 'Germany', 'France', 'Spain']

# output it in its original form
print(destination)

# apply the sorted function on the list and output it
print(sorted(destination))

# output the list again to show that it was a temporary change and not a
# permanent
print(destination)

# apply the reverse method on the list to mirror the list
destination.reverse()
print(destination)

# reverse it again to bring the list back to original form
destination.reverse()
print(destination)

# apply reverse with the sorted function on list
print(sorted(destination, reverse=True))

# use sort method to sort list in alphabetical order
destination.sort()
print(destination)

# output the list to show that it has been permanently changed
print(destination)

# using program from 04 guest_list to find the number of people going to party
invites = ['a', 'b', 'c']
print('The number of people invited is: ' + str(len(invites)) +
      ' that are going to the party')
