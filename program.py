with open("./subprogram/demo.txt", "r") as f:
    today = f.readline()

with open("./final.txt", "w") as f:
    f.write("--- {} ---".format(123))
