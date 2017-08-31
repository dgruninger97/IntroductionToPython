"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and David Gruninger.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
import rosegraphics as rg
window =  rg.TurtleWindow()
David = rg.SimpleTurtle('turtle')
David.speed = 12
David.pen = rg.Pen('red', 5)
for k in range(35):
    David.draw_circle(30)
    David.forward(50)
    David.backward(30)
    David.left(10)
    David.right(20)

Allison = rg.SimpleTurtle()
Allison.speed = 13
size = 300
Allison.pen = rg.Pen('blue', 10)
for k in range(10):
    Allison.draw_square(8)
    Allison.backward(30)
    Allison.right(15)
    Allison.left(50)
########################################################################
