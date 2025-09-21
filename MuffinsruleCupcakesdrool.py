# oh yeah muffins and cupcakes my fav :D 
muffins = 10
cupcakes = 10
#I think asking would be appropriate 
print("What would you like to order? Muffins or cupcakes? (Enter 0 to finish)")

while True:
    order = input().strip().lower()

    if order == "0":
        break
    elif order == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif order == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    else:
        print("Invalid input")
#nom nom nom muffins are superior 
print(f"muffins: {muffins} cupcakes: {cupcakes}")
