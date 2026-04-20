import sys
import struct

width = 100
height = 100

point1 = sys.argv[1]
point2 = sys.argv[2]
output_path = sys.argv[4]

point1_position, point1_color = point1.split("=")
point2_position, point2_color = point2.split("=")

x1, y1 = map(int, point1_position.split(","))
x2, y2 = map(int, point2_position.split(","))

red1, green1, blue1 = map(int, point1_color.split(","))
red2, green2, blue2 = map(int, point2_color.split(","))

x_direction = x2 - x1
y_direction = y2 - y1
direction_length_squared = x_direction * x_direction + y_direction * y_direction

pixels = []

for y in range(height):
    row = []
    for x in range(width):
        if direction_length_squared == 0:
            projection_ratio = 0
        else:
            projection_ratio = (
                (x - x1) * x_direction +
                (y - y1) * y_direction
            ) / direction_length_squared

        red = int(red1 + projection_ratio * (red2 - red1))
        green = int(green1 + projection_ratio * (green2 - green1))
        blue = int(blue1 + projection_ratio * (blue2 - blue1))

        red = max(0, min(255, red))
        green = max(0, min(255, green))
        blue = max(0, min(255, blue))

        row.append((blue, green, red))
    pixels.append(row)

row_size = (width * 3 + 3) & ~3
pixel_data_size = row_size * height
file_size = 54 + pixel_data_size

with open(output_path, "wb") as file:
    file.write(b"BM")
    file.write(struct.pack("<I", file_size))
    file.write(struct.pack("<HH", 0, 0))
    file.write(struct.pack("<I", 54))

    file.write(struct.pack("<I", 40))
    file.write(struct.pack("<i", width))
    file.write(struct.pack("<i", height))
    file.write(struct.pack("<H", 1))
    file.write(struct.pack("<H", 24))
    file.write(struct.pack("<I", 0))
    file.write(struct.pack("<I", pixel_data_size))
    file.write(struct.pack("<i", 0))
    file.write(struct.pack("<i", 0))
    file.write(struct.pack("<I", 0))
    file.write(struct.pack("<I", 0))

    padding = b"\x00" * (row_size - width * 3)

    for y in range(height - 1, -1, -1):
        for blue, green, red in pixels[y]:
            file.write(struct.pack("BBB", blue, green, red))
        file.write(padding)