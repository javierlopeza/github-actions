import pendulum

today = pendulum.now("America/Santiago").format("YYYY-MM-DD HH:mm:ss")

with open("./final.txt", "a") as f:
    f.write("123".format("123"))
