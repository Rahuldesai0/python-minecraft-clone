transparent = 2
is_cube = False
glass = False
translucent = False

# fmt: off

colliders = [
	[
		(-0.5, -0.5000, -0.5),
		( 0.5,  0.4375,  0.5)
	]
]

vertex_positions = [
	[ 0.5,  0.4375,  0.5,   0.5, -0.5,  0.5,   0.5, -0.5, -0.5,   0.5,  0.4375, -0.5], # right
	[-0.5,  0.4375, -0.5,  -0.5, -0.5, -0.5,  -0.5, -0.5,  0.5,  -0.5,  0.4375,  0.5], # left
	[ 0.5,  0.4375,  0.5,   0.5,  0.4375, -0.5,  -0.5,  0.4375, -0.5,  -0.5,  0.4375,  0.5], # top
	[-0.5, -0.5,  0.5,  -0.5, -0.5, -0.5,   0.5, -0.5, -0.5,   0.5, -0.5,  0.5], # bottom
	[-0.5,  0.4375,  0.5,  -0.5, -0.5,  0.5,   0.5, -0.5,  0.5,   0.5,  0.4375,  0.5], # front
	[ 0.5,  0.4375, -0.5,   0.5, -0.5, -0.5,  -0.5, -0.5, -0.5,  -0.5,  0.4375, -0.5], # back
]

tex_coords = [
	[0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
	[0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
	[0.0, 0.9375, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 0.9375, 0.0],
]

shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]
