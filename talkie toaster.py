index = 0
breakfast = ["toast","muffins","baguettes","teacakes","buns","baps","bagels","croissants","pancakes","waffles","flapjacks"]
breakfastloop = 0

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

if toast == "no" or toast == "n":
    breakfastloop = 1 
while breakfastloop == 1:
    print("how about ",breakfast[index],"? ")
    index = index + 1 
    toast = input("how about it? ")
    if index == 10:
        index = 0
    if toast == "yes" or toast == "y":
        breakfastloop = 0
        print("Brilliant! heres some toast!")
        print("  __  _     __  _")
        print("(     ))  (     ))")
        print("|     ||  |     ||")
        print("|     ||  |     ||")
        print("'-----'`  '-----'`")