#Class Circle
#A Circle instance accepts attribute radius (r)
#It has a method area that returns the area (A) of the circle using the formula A=πr2
#It has a method to calculate circumference (c) using the formula C=2πr
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area_circle(self):
        A = math.pi*self.radius**2
        return A
    def circumfrence(self):
        C = 2*math.pi*self.radius
        return C
#Class Square
#A Square instance accepts the attribute side (a)
#It has method area that returns the area (A) of the square using the formula A=a2
#It has a method to calculate the perimeter (P) of the square using the formula P=4a 
class Square:
    def __init__(self,a):
        self.a = a

    def area_square(self):
        areasquare = self.a*self.a
        return areasquare
    def perimeter(self):
        peri = 4*self.a
        return peri

#Class Rectangle
#A Rectangle instance accepts two sides of a rectangle (w,l)
#It has method to calculate the area (A) of the rectangle using the formula A=wl
#It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)
class Rectangle():
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area_rectangle(self):
        arearectangle = self.width*self.length
        return arearectangle

    def rectangle_perimeter(self):
        p = 2(self.width + self.length) 
        return p  

#Class Sphere
#A Sphere Instance accepts the radius of the sphere (r)
#It has a method to calculate the surface area (A) using the formula A=4πr2
#It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
class Sphere:
    def __init__(self,r):
        self.r = r

    def area_sphere(self):
        areasphere = 4*math.pi*self.r**2
        return areasphere

    def volume(self):
        v = 4/3(math.pi**3) 
        return v   



