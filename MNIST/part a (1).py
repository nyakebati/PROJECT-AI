import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Regions
regions = ['WA', 'NT', 'SA', 'Q', 'NSW']

# Available colours
colours = ['Blue', 'Red', 'Green']

# Adjacency list
neighbors = {
    'WA': ['NT', 'SA'],  
    'NT': ['WA', 'SA', 'Q'], 
    'SA': ['WA', 'NT', 'Q', 'NSW'], 
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q'] 
}

# Store colouring solution
solution = {}

# Check if colour assignment is valid
def is_valid(region, colour):
    for neighbor in neighbors.get(region):
        if neighbor in solution and solution[neighbor] == colour:
            return False
    return True

# Recursive backtracking function
def colour_map(index):
    
    # Base case: all regions coloured
    if index == len(regions):
        return True

    region = regions[index]

    # Try each colour
    for colour in colours:

        if is_valid(region, colour):

            # Assign colour
            solution[region] = colour

            # Recur for next region
            if colour_map(index + 1):
                return True

            # Backtrack
            del solution[region]

    return False


# Run recursive colouring starting with first region
colour_map(0)

print("Solution:")
for region, colour in solution.items():
    print(region, "=", colour)




# Coordinates for simple Australia map
map_shapes = {
    'WA': [(0,2), (2,2), (2,6), (0,6)],
    'NT': [(2,4), (4,4), (4,6), (2,6)],
    'SA': [(2,2), (4,2), (4,4), (2,4)],
    'Q': [(4,4), (6,4), (6,6), (4,6)],
    'NSW': [(4,2), (6,2), (6,4), (4,4)]
}

# Create figure
fig, ax = plt.subplots(figsize=(8,6))

# Draw regions
for region, coords in map_shapes.items():

    polygon = Polygon(
        coords,
        closed=True,
        facecolor=solution[region].lower(),
        edgecolor='black',
        linewidth=2
    )

    ax.add_patch(polygon)

    # Region label
    x = sum(p[0] for p in coords) / len(coords)
    y = sum(p[1] for p in coords) / len(coords)

    ax.text(
        x, y,
        region,
        ha='center',
        va='center',
        fontsize=14,
        color='white',
        fontweight='bold'
    )

# Plot settings
ax.set_xlim(0, 6)
ax.set_ylim(2, 6)
ax.set_aspect('equal')
ax.axis('off')

plt.title("Australia Map Colouring Using Recursive Backtracking")
plt.show()