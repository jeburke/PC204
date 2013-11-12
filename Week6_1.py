import sys

class Point(object):
	"""A point in 2-S space"""

class Rectangle(object):
	"""Represents a rectangle.
	atttributes: width, height, corner.
	"""

def create_rectangle(x, y, width, height):
	rect = Rectangle()
	p = Point()
	p.x = x
	p.y = y
	rect.width = width
	rect.height = height
	rect.corner = p 
	return rect

def str_rectangle(rect):
	return '(%g, %g, %g, %g)' % (rect.corner.x, rect.corner.y, rect.width, rect.height)

def shift_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

def offset_rectangle(rect, dx, dy):
	rect_new = Rectangle()
	p = Point()
	p.x = rect.corner.x + dx
	p.y = rect.corner.y + dy
	rect_new.width = rect.width
	rect_new.height = rect.height
	rect_new.corner = p
	return rect_new

def main():
	r1 = create_rectangle(10, 20, 30, 40)
	print str_rectangle(r1)
	shift_rectangle(r1, -10, -20)
	print str_rectangle(r1)
	r2 = offset_rectangle(r1, 100, 100)
	print str_rectangle(r1)
	print str_rectangle(r2)

if __name__ == "__main__":
	main ()
