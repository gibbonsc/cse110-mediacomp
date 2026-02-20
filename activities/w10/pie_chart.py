from PIL import Image, ImageDraw
img=Image.new('RGB', (200,200))
chart=ImageDraw.Draw(img)

# parallel lists of colors and percentages
colors = [
    (128,0,0),  # red
    (0,128,0),  # green
    (0,0,128),  # blue
    (128,128,0),  # yellow
    (0,128,128)  # cyan
]
percentages = [45, 27, 16, 10, 2] # [45, 35, 10, 7, 3]
assert sum(percentages)==100

# convert percentages to degree angles,
#   then use those angles to draw pie slices
start_angle = 0
for i in range(len(percentages)):
    end_angle = start_angle + percentages[i] * 360 / 100
    chart.pieslice([0,0,199,199],start_angle,end_angle,colors[i])
    start_angle = end_angle

img.show()
img.save("pie_chart.png")
