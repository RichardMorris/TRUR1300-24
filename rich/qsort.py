def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    lower = [x for x in data if x < pivot]
    higher = [x for x in data if x > pivot]
    mid = [x for x in data if x == pivot]
    qlower = qsort(lower)
    qhigher = qsort(higher)
    return qlower + mid + qhigher

def cheatsort(data):
    counts = [0] * 100
    for i in data:
        counts[i] += 1
    result = []
    for i in range(100):
        for j in range(counts[i]):
            result.append( i)
        
    return result

data = [3, 6, 8, 10, 1, 2, 1]
print(qsort(data))
print(cheatsort(data))
