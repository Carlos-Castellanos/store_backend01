from unittest.util import _count_diff_all_purpose


def start_test():
    print("-------------list test----------------")
    nums = [1, 2, 3, 4, 5, 6]

    # reads elements for la list
    print("-------------complete ----------------")
    for num in nums:
        print(num)
    print("------------- range 3-6----------------")
    for number in range(3, 6):
        print(number)

    # add elements to a list
    nums.append(7)
    print(nums)

    nums.pop(1)
    print(nums)

    nums.append(5)
    print(nums)

    nums.sort()
    print(nums)


def test1():
    print("Test 1 ")

    prices = [123, 454, 233, 7578, 1234, 456, 33, 90,
              678, 44, 2454, 324, 575, 0, -45, -20, 10]

    # 1 print numbers lower 50
    # 2 coun how many numbers are lower 50
    # 3 sum fo all numbers
    # 4the sum of the all numbers greaters than zera
    # 5 count how many zeros there are

    c = 0
    sum = 0
    sumPositives = 0
    countPositives = 0
    for num in prices:
        sum += num
        if num < 50:
            # print(num)
            c += 1
        if num > 0:
            countPositives += 1
            sumPositives += num

    print(f"There are {c} lower than 50")
    print(f"The sum of all is {sum} ")
    print(f"The sum of positives is {sumPositives}")
    print(f"There are {countPositives} lower than 0")

    menor = min(prices)
    print(menor)

    menor = max(prices)
    print(menor)


def test2():
    print("Testing2")
    users = [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green",
            "age": 24
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray",
            "age": 12
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink",
            "age": 42
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink",
            "age": 45
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple",
            "age": 32
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink",
            "age": 28
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black",
            "age": 27
        },
    ]
    # 1 - print all names
    # 2 - how many users there arein the list
    # print the names of the user who likes the color pink case insensitive

    count = 0
    for use in users:
        print(use["name"])
        count += 1
    print(f"there are {count} user in the list")
    print(f"there are {len(users)} users in the list")

    print("----------pinks---------------")
    for use in users:
        if use["color"].upper() == "PINK":
            print(use["name"])



def test3():
    print("----- Test 3 -----")
    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]
    
    # find the mos expensive product
    maxPrice=max(prices)
    print("function max " + str(maxPrice))
    
    maxPrice=prices[0]
    for i in prices:
        if i>maxPrice:
            maxPrice=i
            
    print("for loop " + str(maxPrice))
    return True





# start_test()
# test1()
#test2()
test3()
