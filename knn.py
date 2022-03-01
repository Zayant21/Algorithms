from sklearn.neighbors import KDTree                                 # pip install scikit-learn
import random
random.seed(1)                                                       # Setting random number generator seed for repeatability

NUM_DRONES = 10000
AIRSPACE_SIZE = 128000 # 128 km
CONFLICT_RADIUS = 500  # Meters.


def count_conflicts(drones, conflict_radius):
    conflict = 0
    tree = KDTree(drones, leaf_size=2)                                # Setting a kd tree with 2 left and right leafs
    all_nearest_points = tree.query_radius(drones, r=conflict_radius) # Query to get the nearest points in the give radius from the point. 
    for points in all_nearest_points:
        if len(points) >= 2:                                          # Count if there are more than 2 drones in the same max_radius
            conflict = conflict + 1
    return conflict


def gen_coord():
    return int(random.random() * AIRSPACE_SIZE)


positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
conflicts = count_conflicts(positions, CONFLICT_RADIUS)
print("Drones in conflict: {}".format(conflicts))

