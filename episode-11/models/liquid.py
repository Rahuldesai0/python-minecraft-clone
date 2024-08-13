# fmt: off

# in the end, it'd be nice to have it so that liquids fill up the whole block when they have a block above them
# this would avoid the problems this solution has

transparent = True
is_cube = True
glass = True

vertex_positions = [
	[ 0.500,  0.375,  0.500,   0.500, -0.625,  0.500,   0.500, -0.625, -0.500,   0.500,  0.375, -0.500], # right
	[-0.500,  0.375, -0.500,  -0.500, -0.625, -0.500,  -0.500, -0.625,  0.500,  -0.500,  0.375,  0.500], # left
	[ 0.500,  0.375,  0.500,   0.500,  0.375, -0.500,  -0.500,  0.375, -0.500,  -0.500,  0.375,  0.500], # top
	[-0.500, -0.625,  0.500,  -0.500, -0.625, -0.500,   0.500, -0.625, -0.500,   0.500, -0.625,  0.500], # bottom
	[-0.500,  0.375,  0.500,  -0.500, -0.625,  0.500,   0.500, -0.625,  0.500,   0.500,  0.375,  0.500], # front
	[ 0.500,  0.375, -0.500,   0.500, -0.625, -0.500,  -0.500, -0.625, -0.500,  -0.500,  0.375, -0.500], # back
]

tex_coords = [
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]
