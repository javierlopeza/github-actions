import pendulum

today = pendulum.now("America/Santiago").format("YYYY-MM-DD HH:mm:ss")

with open("demo.txt", "a") as output:
    output.write("\n" + today)
