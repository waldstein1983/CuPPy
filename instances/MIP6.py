numVars = 2
numCons = 6
points = None
#points = [[2.5, 4.5], [6.5, 0.5], [0.5, 1],
#          [7, 5.7], [7.7, 5], [2, 0.25]]
#points = [[0, 0], [2.5, 4.5], [7.75, 5.75], [6.5, 0.5]]
#points = [[0, 0], [2.5, 4.5], [7.5, 5.5], [6.5, 0.5]]
rays = []
A = [[ -8,     30],
     [ -2,    -4],
     [-14,     8],
     [  2,   -36],
     [  30, -8],
     [  10,     10],
#     [  1,    -8],
     ]
b = [115,
     -5,
      1,
     -5,
     191,
     127,
#     2
    ]

#This is the integer hull
#A = [[ 0, -1],
# [-1, 1],
# [-2,  1],
# [-1,  2],
# [ 2, -1],
# [ 0,  1],
# [ 1, 0],
# ]

#b = [ -1,   
#   1,  
#  -1,   
#   5,  
#  11,   
#   5,   
#   7]

#c = [-1, 1]
c = [1, -1]
obj_val = 2 
rhs = None
cuts = None
sense = ('Max', '<=')
integerIndices = [0, 1]

obj_val1 = 1.63
A1 = A + [[1, 0]]
b1 = b + [2]

A2 = A + [[-1, 0]]
b2 = b + [-3]

obj_val2 = 1
A3 = A2 + [[0, -1]]
b3 = b2 + [-5]

A4 = A2 + [[0, 1]]
b4 = b2 + [4]