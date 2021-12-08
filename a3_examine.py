import csv

# open a file into a file variable (or use a with statement)


with open('data/coffees.csv') as coffee_file:
   coffees = csv.DictReader(coffee_file, delimiter='\t', quoting=csv.QUOTE_NONE)
print(coffees)

# use the next() built-in function to get the next item from the reader
# Print the item you got.

