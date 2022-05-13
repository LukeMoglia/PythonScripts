import pyglet
import math
from pyglet import shapes
from pyglet.window import key
from math import sin, cos, radians, atan2, degrees, pi

key = pyglet.window.key
window = pyglet.window.Window(1012, 750, 'driving game')
keyboard = key.KeyStateHandler()
window.push_handlers(keyboard)

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
startPosX = 300
startPosY = 300

# create assets
circle = shapes.Circle(startPosX, startPosY, 10, color=(50, 225, 30), batch=batch)
line0deg = shapes.Line(circle.x, circle.y, circle.x, circle.y + 200, width=2, color=(0, 230, 0), batch=batch)


@window.event
def update(dt):
    value_circ = circle.position

    if keyboard[key.UP]:
        # circle.y += dt * 100
        print('up is being pressed')
        print(value_circ)

        myRadians = math.atan2(line0deg.y2 - line0deg.y, line0deg.x2 - line0deg.x)

        angle = math.degrees(myRadians)

        print(angle)

        circle.x = circle.x + (dt*100*math.cos(myRadians))
        circle.y = circle.y + (dt*100*math.sin(myRadians))

        line0deg.x2 = line0deg.x2 + (dt*100*math.cos(myRadians))
        line0deg.y2 = line0deg.y2 + (dt*100*math.sin(myRadians))

        line0deg.x = circle.x
        line0deg.y = circle.y


    if keyboard[key.DOWN]:
        # circle.y -= dt * 100
        print('down is being pressed')
        print(value_circ)

        myRadians = math.atan2(line0deg.y2 - line0deg.y, line0deg.x2 - line0deg.x)

        angle = math.degrees(myRadians)

        print(angle)

        circle.x = circle.x - (dt*100*math.cos(myRadians))
        circle.y = circle.y - (dt*100*math.sin(myRadians))

        line0deg.x2 = line0deg.x2 - (dt*100*math.cos(myRadians))
        line0deg.y2 = line0deg.y2 - (dt*100*math.sin(myRadians))

        line0deg.x = circle.x
        line0deg.y = circle.y

    if keyboard[key.LEFT]:
        # circle.x -= dt * 100
        print('left is being pressed')
        print(value_circ)

        angle = math.radians(2)

        newX = line0deg.x + math.cos(angle) * (line0deg.x2 - line0deg.x) - math.sin(angle) * (line0deg.y2 - line0deg.y)
        newY = line0deg.y + math.sin(angle) * (line0deg.x2 - line0deg.x) + math.cos(angle) * (line0deg.y2 - line0deg.y)

        line0deg.x2 = newX
        line0deg.y2 = newY

        line0deg.x = circle.x
        line0deg.y = circle.y



    if keyboard[key.RIGHT]:
        # circle.x += dt * 100
        print('right is being pressed')
        line0deg.x = circle.x
        # line0deg.x2 = (line0deg.x + line0deg.x2 /2)
        # line0deg.y2 = line0deg.y2 / 2
        print(line0deg.y2)

        angle = math.radians(-2)

        newX = line0deg.x + math.cos(angle) * (line0deg.x2 - line0deg.x) - math.sin(angle) * (line0deg.y2 - line0deg.y)
        newY = line0deg.y + math.sin(angle) * (line0deg.x2 - line0deg.x) + math.cos(angle) * (line0deg.y2 - line0deg.y)




        line0deg.x2 = newX
        line0deg.y2 = newY




        


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.clock.schedule_interval(update, 1 / 60)

pyglet.app.run()