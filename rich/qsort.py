def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    lower = [x for x in data if x < pivot]
    higher = [x for x in data if x > pivot]
    qlower = qsort(lower)
    qhigher = qsort(higher)
    return qlower + [pivot] + qhigher

def cheatsort(data):
    counts = [0] * 100
    for i in data:
        counts[i] += 1
    result = []
    for i in range(100):
        for j in range(counts[i]):
            result.append( i)
        
    return result

if __name__ == "__main__":
    data = []
    while True:
        print("Enter positive number -1 to end")
        num = int(input())
        if num ==-1:
            break
        data.append(num)
    sorted = qsort(data)
    print(sorted)
