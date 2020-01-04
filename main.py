import turtle as t
import random
def turn_left():
  t.left(10)

def turn_right():
  t.right(10)

def fire():
  global target
  an = t.heading()
  while t.ycor() > 0:
    t.forward(20)
    t.right(6)
  d = t.distance(target, 0)
  t.sety(random.randint(10, 100))
  if d < 25:
    t.color("blue")
    t.write("Good!", False, "center", ("", 15))
  else:
    t.color("red")
    t.write("Bad!", False, "center", ("", 15))
  t.color("black")
  t.goto(-200, 10)
  t.setheading(an)

def left():
  global target
  t.clear()
  t.goto(-300, 0)
  t.down()
  t.goto(300, 0)

  target = random.randint(50, 150)
  t.color("green")
  t.up()
  t.goto(target - 25, 2)
  t.down()
  t.goto(target +25, 2)
  t.color("black")
  t.up()
  t.goto(-200, 10)
  t.setheading(20)

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)


t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(50, 150)
t.pensize(1)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target +25, 2)

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

t.onkeypress(left, "Left")
t.onkeypress(turn_left, "Up")
t.onkeypress(turn_right, "Down")
t.onkeypress(fire, "space")
t.listen()
t.mainloop()