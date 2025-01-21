index = 0
# This list contains  different baked goods that will be displayed later
breakfast = ["toast","muffins","baguettes","teacakes","buns","baps","bagels","croissants","pancakes","waffles","flapjacks"]
breakfastloop = 0

# This is Talkie Toaster's introduction from Red Dwarf
print("Howdy Doodily Doo!")
print("How's it going?")
print("I'm Talkie, Talkie Toaster")
print("Your chirpy breakfast companion!")
print("Talkie's the name, toasting's the game!")

toast = input("Anyone like any toast? ")
if toast == "yes" or toast == "y":
        print("Brilliant! heres some toast!")
        print("  __  _     __  _")
        print("(     ))  (     ))")
        print("|     ||  |     ||")
        print("|     ||  |     ||")
        print("'-----'`  '-----'`")

# If the user types no or n, the 'breakfastloop' variable will be set to 1. 
# while the variable is set to 1 the program will loop and increase the index variable so it will print the next item from the 'breakfast' list
if toast == "no" or toast == "n":
    breakfastloop = 1 
while breakfastloop == 1:
    print("how about ",breakfast[index],"? ")
    index = index + 1 
    toast = input("how about it? ")
    if index == 10:
        index = 0
    # The loop will not end unless the user says yes to an item.
    if toast == "yes" or toast == "y":
        breakfastloop = 0
        # No matter what item you want, you're getting toast.
        # It's a toaster, not a miracle worker...
        print("Brilliant! heres some toast!")
        print("  __  _     __  _")
        print("(     ))  (     ))")
        print("|     ||  |     ||")
        print("|     ||  |     ||")
        print("'-----'`  '-----'`")