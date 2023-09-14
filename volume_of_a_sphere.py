#This program is supposed to calculate the area of a given circle

def compute_area_of_circle(radius):
	pi = 3.14
	area = (4/3) * pi * (radius ** 3)
	return area

radius1 = 30
volume1 = compute_area_of_circle(radius1)
print(f"The volume of a sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = compute_area_of_circle(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")
