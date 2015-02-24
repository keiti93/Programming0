from math import sqrt

def is_triangle(a, b, c):
    return a + b > c and a + c > b and c + b > a

def area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

def is_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def max_area(triangles):
    current_max = triangles[0]
    a = current_max[0]
    b = current_max[1]
    c = current_max[2]
    max_area = area(a, b, c)
    
    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]
        current_area = area(a, b, c)
        
        if current_area > max_area:
            current_max = triangle
            max_area = current_area
            
    return current_max
