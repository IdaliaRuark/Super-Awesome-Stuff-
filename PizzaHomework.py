# thats enought SLICES 
slices_per_pizza = 8

# how hungry? 
print("How many slices does my family eat?:")

brother = int(input("Brother: "))
sister = int(input("Sister: "))
dad = int(input("Dad: "))
grandma = int(input("Grandma: "))

# slices we need
total_slices = brother + sister + dad + grandma


# pizzaaaa (Used AI to help me with these lines) 
pizzas_needed = total_slices // slices_per_pizza
if total_slices % slices_per_pizza != 0:
    pizzas_needed += 1

# leftovers
leftover_slices = (pizzas_needed * slices_per_pizza) - total_slices

print("how many pizzas to get:", pizzas_needed)
print("leftover slices:", leftover_slices)

input is the amount 
