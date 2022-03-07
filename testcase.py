with open("data.txt") as data:
    content = data.readlines()
    print("test" + content[2][25:30] + "test")