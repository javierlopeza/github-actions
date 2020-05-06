with open("./subprogram/demo.txt", "r") as f:
    today = f.readline()

with open("./final.txt", "a") as f:
    f.write("\n--- {} ---".format(today))
