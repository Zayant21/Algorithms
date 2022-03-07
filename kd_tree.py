import random
from math import floor
random.seed(1)  # Setting random number generator seed for repeatability

NUM_DRONES = 10000
AIRSPACE_SIZE = 128000 # 128 km
CONFLICT_RADIUS = 500  # Meters.
k = 2 


def distance(p1,p2):                                                # Getting distance between two points

    x1,y1 = p1
    x2,y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    return (dx**2 + dy**2)


def kdtree(points, depth = 0 ):                                     # Build the kd tree and map all points starting with x axis and then y axis and going back and forth
    n = len(points)
    if n<=0:
        return None
    axis = depth % k
    sorted_points = sorted(points, key = lambda point: point[axis])
    
    if n % 2 == 0:                                                  # to get the median for next root node each time we divide the points.
        median_idx = int(n/2)
    else:
        median_idx = floor(n/2)
    return{
        'point': sorted_points[median_idx],
        'left': kdtree(sorted_points[:median_idx], depth+1),
        'right': kdtree(sorted_points[median_idx+1:], depth+1)
    }

def best_distance(pivot, point1, point2):                          # return the best distance between two distances from the pivot
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    d1 = distance(pivot,point1)
    d2 = distance(pivot,point2)

    if d1 < d2:
        return point1
    else:
        return point2


def kdtree_closest_point(root, point, depth = 0):                 # Implemtation of kd tree recursive process
    if root is None:
        return None
    axis = depth % k
    apposite_branch = None

    if point[axis] < root['point'][axis]:                        # check our pointp[axis] with root[axis] to decide to go left or right side of the tree 
        next_branch = root['left']
        opposite_branch = root['right']
    else:
        next_branch = root['right']                              
        opposite_branch = root['left']
    
    best_result = best_distance(point,kdtree_closest_point(next_branch,point,depth+1), root['point'])  # get the best result point 


    # if the distance between the search point and best distance is greator than the distance between search point and the nearest bound of the box that means
    # our point radius is overlapping into other sub trees aka (boxes) and we might need to visit those trees too to make sure we does not miss the nearest point. 

    if distance(point,best_result) > (abs(point[axis] - root['point'][axis])):                        
        best_result = best_distance(point,kdtree_closest_point(next_branch,point,depth+1), best_result)
    
    
    return best_result



def count_conflicts(drones, conflict_radius):
    drone_conflicts = 0 
    tree = kdtree(positions)
    for drone in drones:
        if distance(drone ,  kdtree_closest_point(tree, drone)) > conflict_radius**2:
            drone_conflicts = drone_conflicts+1
    return drone_conflicts

def gen_coord():
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
conflicts = count_conflicts(positions, CONFLICT_RADIUS)
print("Drones in conflict: {}".format(conflicts))
