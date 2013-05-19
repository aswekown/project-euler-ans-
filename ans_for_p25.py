a = 1
b = 1
index = 2
while True:
    a, b = b, a + b
    if len(str(a)) >= 1000:
        print index
        break
    index += 1
