import time
from BST import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# The runtime for the above ^^ was: 6.062531232833862 seconds
# New Solution: using BST, runtime is: 0.11680889129638672 seconds


# Making our root node the first name in names_1
tree = BSTNode(names_1[0])


# Inserting each name discluding the first name in names_1 into our BST
for name in names_1[1:]:
    tree.insert(name)


# Going over names_2, checking if a name in names_2 is contained in our names_1 BST
for name in names_2:
    if tree.contains(name):
        # placing the matching ones in duplicates list
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
