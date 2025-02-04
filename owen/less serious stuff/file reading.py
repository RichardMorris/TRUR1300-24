f = open("films.txt", "r")

for line in f:
    fields = line.split(",")
    title = fields[1]
    duration = int(fields[4])
    genre = fields[5].strip()
    if duration <= 100:
        print(title, genre, duration, "minutes")
f.close()  

#    O           O
#   /Y\    -  ¬_/Y\
#    ^           ^ 
#   / \         / \