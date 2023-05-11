# Imports
# ---------------------------
import numpy as np

# Functions
# ---------------------------

# Positions of the 12 notes
def star_positions():
    notes = [1,2,3,4,5,6,7,8,9,10,11,12]
    angles = [2*np.pi*(i-5)/12+np.pi/12 for i in notes]
    positions = [np.array([np.cos(ang), np.sin(ang)]) for ang in angles]
    return positions

# Normalize a vector
def normalize(v):
    v = np.array(v)
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

# Position transform
def vector_transform(x, loc, scale):
    return np.array(x)*scale + loc

# distance between objs
def distance(obj1, obj2):
    dx = (obj1.pos-obj2.pos)[0]
    dy = (obj1.pos-obj2.pos)[1]
    return np.linalg.norm(np.array([dx,dy]))

# Get the points of triangle based on position and velocity vector
def get_triangle_points(pos, direction, size, loc, scale):
    normal = np.array([direction[1],-direction[0]])
    loc = np.array(loc)
    x1 = (pos + direction * size)*scale+loc
    x2 = (pos - normal * size/4)*scale+loc
    x3 = (pos + normal * size/4)*scale+loc
    return [x1,x2,x3]

# Star positions
note_positions = star_positions()
# dictionnary of indices for notes
note_index = {i:(i+6)%12 for i in range(1,13)}

def compute_hit(pos, dir, obj_size):
    for i in range(1,13):
        x = note_positions[note_index[i]]
        if np.linalg.norm(pos+obj_size*dir-x)<=15/350:
            return i
    return -1