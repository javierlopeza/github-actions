import pendulum

today = pendulum.now("America/Santiago").format("YYYY-MM-DD HH:mm:ss")

with open("demo.txt", "w") as output:
    output.write(123)
