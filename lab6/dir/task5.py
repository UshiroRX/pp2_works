a = [1,2,3,4,5]

with open("file.txt", "w") as f:
    for i in a:
        f.write(str(i)+" ")


