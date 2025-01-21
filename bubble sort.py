#########################################################################
def bubble_sort():
    swap = True
    while swap:
        swap = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = a
                swap = True
    return nums

def bubble_reverse():
    swap = True
    while swap:
        swap = False
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                a = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = a
                swap = True
    return nums

###########################################################################
lists = 0
nums = []
while lists == 0:
    nums.append (input("add to the list: "))
    yn = input("do you wish to add another value? yes or no? ")
    if yn == "n" or yn == "no":
        lists = 1
    else:
        lists = 0

print(nums)
choice = int(input("type 1 for Smallest to Biggest\ntype 2 for Biggest to smallest: "))

if choice == 1:
    bubble_sort()
    print(nums)
elif choice == 2:
    bubble_reverse()
    print(nums)
else:
    print("That's not an option dumbo")