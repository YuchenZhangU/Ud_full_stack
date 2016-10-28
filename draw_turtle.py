import turtle
import math
# ---------------- branch tree ---------------
# def branch(tur, edge, angel, scale):
#     if edge<10:
#         return
#     tur.forward(edge)
#     tur.left(angel)
#     branch(tur, edge*scale, angel, scale)
#     tur.right(2*angel)
#     branch(tur, edge*scale, angel, scale)
#     tur.right(180-angel)
#     tur.forward(edge)
#     tur.left(180)

# window = turtle.Screen()
# tur = turtle.Turtle()
# tur.speed(0)
# branch(tur, 50, 25, 0.8)
# window.exitonclick()

# import math
# # -------------draw squares -------------
# # def draw_single_square(brad, angle):
# #     brad.right(angle)
# #     for i in range(4):
# #         brad.forward(100)
# #         brad.right(90)


# # def draw_squares():
# #     brad = turtle.Turtle()
# #     brad.shape('turtle')
# #     brad.color('blue')
# #     brad.speed(0)


# #     draw_single_square(brad, 0)
# #     angle = 10
# #     for i in range(360/angle - 1):
# #         draw_single_square(brad, angle)  


# # def draw_art():
# #     window = turtle.Screen()
# #     window.bgcolor('red')
# #     # draw squares
# #     draw_squares()
# #     # draw circle
# #     angie = turtle.Turtle()
# #     angie.shape('arrow')
# #     angie.color('yellow')
# #     angie.circle(100)

# #     window.exitonclick()

# # draw_art()

# # --- mini project: draw triangles
# # step1: 
# # step2: generate three start points of triangles given one star point
# # step3: generate three triangles

# def draw_down_triangle(tur, edge):
#     tur.color('white')
#     tur.begin_fill()
#     for i in range(3):
#         tur.forward(edge)
#         tur.right(120)
#     tur.begin_fill()


def draw_tri_with_fill(tur, edge, st_pos, pencolor='black', fillcolor='green'):
    tur.pencolor(pencolor)
    tur.fillcolor(fillcolor)
    tur.up()
    tur.setpos(st_pos[0], st_pos[1])
    tur.down()
    tur.begin_fill()
    for i in range(3):
        tur.forward(edge)
        tur.left(120)
    tur.end_fill()

def draw_nest_tri(tur, edge, st_pos, n):
    if(n > 0):
        st_pos1 = st_pos
        st_pos2 = (st_pos[0] + edge/2, st_pos[1])
        st_pos3 = (st_pos[0] + edge/4, st_pos[1] + edge*math.sqrt(3)/4)
        draw_nest_tri(tur, edge/2, st_pos1, n-1)
        draw_nest_tri(tur, edge/2, st_pos2, n-1)
        draw_nest_tri(tur, edge/2, st_pos3, n-1)
    else:
        draw_tri_with_fill(tur, edge, st_pos)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')
    tur = turtle.Turtle()
    tur.shape('arrow')
    tur.speed(0)
    draw_nest_tri(tur, 400, (-200,-150),5)

    window.exitonclick()

draw_art()

# def generate_3_point(pos, edge):
#     pos_list = []
#     pos_list.append((pos[0], pos[1]))
#     pos_list.append((pos[0]+float(edge), pos[1]))
#     pos_list.append((pos[0]+float(edge)/2, pos[1]+edge*math.sqrt(3)/2))
#     return pos_list

# def draw_list_of_triangles(tur, edge, pos_list, func):
#     for pos in pos_list:
#         func(tur, edge, pos)


# def draw_nest_triangle(tur, edge, st_pos):
#     draw_list_of_triangles(tur, edge/2, generate_3_point(st_pos, edge/2), draw_up_triangle_with_fill)





# def draw_triangle():
#     window = turtle.Screen()

#     tur = turtle.Turtle()   
#     tur.pencolor('black')
#     tur.shape('turtle')
#     tur.speed(2)

#     tur2 = turtle.Turtle()

#     draw_up_triangle_with_fill(tur, 100, (0,0))
#     draw_up_triangle_with_fill(tur2, 100, (100,5))

#     # edge = 100
#     # pos_list = generate_3_point((0,0), edge)

#     # draw_list_of_triangles(tur, edge, pos_list, draw_nest_triangle)

#     #draw_nest_triangle2(tur, 100)
#     #draw_up_triangle_row(tur, 20, 8)

#     window.exitonclick()

# draw_triangle()


# ---------------- other's solution -----------------
# import turtle
# #Haha TTpro
# def draw_triangle(the_turtle,length,ori,recursion):
#     recursion=recursion+1
#     meow= the_turtle

#     for i in range(0,3):
#         if(recursion<4):
#         #if (0):
#             meow.forward(length/2)
#             meow.left(120)
#             draw_triangle(meow,length/2,0,recursion)
#             meow.right(120)
#             meow.forward(length/2)
#         else:
#             meow.forward(length)
#         if (ori==1):
#             meow.left(120)
#         else:
#             meow.right(120)

# meow = turtle.Turtle() # init
# meow.speed(10) # speed = 1 to slow turtle down
# meow.color("yellow","green") # set color5
# meow.shape("turtle") # set shape to a turtle
# background = turtle.Screen()  # create background
# background.bgcolor("red")     # set background color to red


# draw_triangle(meow,200,1,0)

#meow.forward(100)
#meow.left(120)
#draw_triangle(meow,100,0,0)
#meow.right(120)

# background.exitonclick()      # click anywhere to close background
