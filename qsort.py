def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    lower = [x for x in data if x < pivot]
    higher = [x for x in data if x > pivot]
    # added middle for if there are multiple of the same number present
    middle = [x for x in data if x == pivot]
    qlower = qsort(lower)
    qhigher = qsort(higher)
    
    return qlower + middle + qhigher

def cheatsort(data):
    counts = [0] * 100
    for i in data:
        counts[i] += 1
    result = []
    for i in range(100):
        for j in range(counts[i]):
            result.append( i)
        
    return result

# will be set to 1 if number is negative or not -1
validation = 0

if __name__ == "__main__":
    data = []
    while True:
        # at the start of each loop, validation is set to 0 as to not let prior numbers intefere when appending new numbers
        validation = 0
        print('You will be asked for a sequence positive numbers you wish to be sorted.')
        print("Enter '-1' to sort the numbers.")
        num = int(input('Input a single number: '))

        # if validation == 1 the number won't be appended to the list
        if num <-1:
            print ("That is not a positive number, please try another number.")
            validation = 1
        if num == -1:
            break

        # if validation == 0 the number is valid and will be appended to the list
        if validation == 0:
            data.append(num)
    sorted = qsort(data)
    print(sorted)
