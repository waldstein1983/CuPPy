numVars = 2
numCons = 4
points = None
rays = []
A = [[-9, 5],
     [1, -13],
     [5, -1],
     [-1, 5]]
#b = [0, 0, 32, 20]
b = [0, 0, 16, 10]
c = [1, 1]

sense = ('Max', '<=')
integerIndices = [0, 1]

cuts = [
        [4, .00000000008],
        [.0000000008, 4], 
        [3, 1],
        [1, 3],
        [2, .0000000004],
        [.0000000004, 2]
        ]

rhs = [
        14,
        10, 
        12,
        10,
        6,
        4
        ]
