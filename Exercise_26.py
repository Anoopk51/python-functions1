'''
# Question- Yov have to calculate area of circle & circumferece of circle .that you will use aproch oop.

'''
'''
My attempt--------->
# '''
# class circle:
#     def __init__(self,radius):
#         # pass
#         self.radius_1=radius
#         # self.val_of_pi=3.141
#         self.area=3.141*(radius**2)
#         self.circumference=2*3.131*radius
#     def display(self):
#         # area=val_of_pi*(radius_1**2)
#         print(f"Area of the circle is {circle_info.area}")
#         print(f"Circumference of circle is {circle_info.circumference}")
   
# radius1=float(input('Enter the radius of circle in cm.'))
# circle_info=circle(radius1)
# # print(circle_info.radius_1)
# # print(circle_info.val_of_pi)
# circle_info.display()

'''
<-------------x------------------x----------------------x-----------x--------------------------x------------------------>
Ma'am Solution in below.
'''
'''Methode-1'''
# class Circle:
#     pi=3.14 #Class object Attribute
#     def __init__(self,radius):
#         self.radius=radius
#     def get_circumference(self):
#         # circum=2*pi*self.radius
#         # return circum
#         return 2*self.pi *self.radius
#     '''My assingment for area of circle---->'''
#     def get_area(self):
#         return self.pi*(self.radius**2)
    
# circle_1=Circle(4)
# print(circle_1.get_circumference())
# print(circle_1.get_area())
# Circle_2=Circle(14)
# print(Circle_2.get_circumference())
# print(Circle_2.get_area())

'''Methode-2'''
class Circle:
    pi=3.14 #Class object Attribute
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    def get_circumference(self):
        return 2*Circle.pi*self.radius
circle_1=Circle(4)
# print(circle_1.get_circumference())
# print(circle_1.area)
print(f'The circumference of Circle 1 is: {circle_1.get_circumference()}')
print(f'The area of circle 1 is:{circle_1.area}')
circle_2=Circle(14)
print(f"The circumference of Circle 2 is: {circle_2.get_circumference()}")
print(f"The area of circle 1 is:{circle_2.area}")


'''Assingment-1 To find the area of rectangle and circumference of rectangle.'''
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def get_circumference(self):
        return 2*(self.length+self.width)
    
    def get_area(self):
        return (self.length)*(self.width)
rectangle_1=Rectangle(float(input('Enter the length of rectangle.')),float(input('Enter the width of rectagle.')))
print(f'The circumference of rectangle is {rectangle_1.get_circumference()}')
print(f'The are of rectangle is {rectangle_1.get_area()}')