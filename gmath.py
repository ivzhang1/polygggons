import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    normalize_factor = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
    vector[0] = vector[0]/normalize_factor
    vector[1] = vector[1]/normalize_factor
    vector[2] = vector[2]/normalize_factor
    #print(vector)

#Return the dot porduct of a . b
def dot_product(a, b):
    total = 0
    for i in range(0, len(a)):
        total += a[i]*b[i]
    return total

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i+1]
    p2 = polygons[i+2]

    a = [p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2]]
    b = [p2[0]-p0[0], p2[1]-p0[1], p2[2]-p0[2]]

    return [a[1]*b[2] - b[1]*a[2], a[2]*b[0] - b[2]*a[0], a[0]*b[1] - b[0]*a[1]]

#normalize([1, 5, 0]) #[0.19611613513818404, 0.9805806756909202, 0.0]
#normalize([-1, -1, 7]) #[-0.14002800840280097, -0.14002800840280097, 0.9801960588196068]
#print(dot_product([3, -2, 6], [2, 3, -5])) #-30
#print(calculate_normal([[0, 0, 0],[7, 3, -4],[1, 0, 6]], 0)) #[18, -46, -3]
