from PIL import Image

# Load the generated image
image_path = "a.jpg"
image = Image.open(image_path)

# Define grid size (4 rows, 5 columns)
rows, cols = 4, 5
width, height = image.size
piece_width = width // cols
piece_height = height // rows

# Split and save the pieces
pieces = []
for row in range(rows):
    for col in range(cols):
        left = col * piece_width
        upper = row * piece_height
        right = left + piece_width
        lower = upper + piece_height
        piece = image.crop((left, upper, right, lower))
        pieces.append(piece)

# Save the pieces
piece_paths = []
for i, piece in enumerate(pieces):
    piece_path = f"{i+1}.png"
    piece.save(piece_path)
    piece_paths.append(piece_path)

piece_paths

from PIL import ImageDraw

# Load the original image again
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Draw the grid lines
for row in range(1, rows):
    y = row * piece_height
    draw.line([(0, y), (width, y)], fill="black", width=3)

for col in range(1, cols):
    x = col * piece_width
    draw.line([(x, 0), (x, height)], fill="black", width=3)

# Save the modified image with grid lines
grid_image_path = "a.png"
image.save(grid_image_path)
grid_image_path
