
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(5))
items = [1]
print(len(items))
if items:
    print('full')
else:
    print('empty')

items = [1,2,3,4,5]
items.pop(0)
print(items[0])
print(items)

for i in range(5):
    pass
print(i)

def GCD(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    return x

print(GCD(12, 18))


def add_list(list1, list2):
    if len(list1) > len(list2):
        list3 = []
        val = len(list1) - len(list2)
        for i in range(val):
            list2.append(0)

    elif len(list2) > len(list1):
        val = len(list2) - len(list1)
        for i in range(val):
            list1.append(0)

    carry = 0
    list3 = []
    for i in range(len(list1)-1,-1,-1):
        value = list1[i] + list2[i] + carry
        carry = value // 10
        value = value % 10
        list3.append(value)

        if i==0 and carry > 0:
            list3.append(carry)

    list3.reverse()
    return list3


print(add_list([5,2,3],[6,4,8]))
print(add_list([1,4,3],[5,2,5]))
print(add_list([7,6,3],[5,4,9]))