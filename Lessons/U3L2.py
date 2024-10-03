# Predict
"""
Predict A:
It will print out each item in the list, in this case it would look like: ['Apples', 'Bananas', 'Cherries', 'Dosa']
Predict B:
It would print out: The number of items is 4.
Predict C:
Apples
Bananas
Cherries
Dosa
Predict D:
0 Apples
1 Bananas
2 Cherries
3 Dosa
"""

# Modify
items = []
item_amount = int(input("How many items are you entering? "))
print("Enter your items now: ")
for item in range(item_amount):
  items.append(input("Next item: "))
print("You have entered %d items." % len(items))
for item in items:
  print(item)

