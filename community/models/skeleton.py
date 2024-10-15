
transparent = True
is_cube = False
glass = False

colliders = []

bones = [{'name':'body','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 0.75, -0.125, -0.25, 1.5, -0.125, 0.25, 1.5, -0.125, 0.25, 0.75, -0.125], [0.25, 0.75, 0.125, 0.25, 1.5, 0.125, -0.25, 1.5, 0.125, -0.25, 0.75, 0.125], [-0.25, 1.5, -0.125, -0.25, 1.5, 0.125, 0.25, 1.5, 0.125, 0.25, 1.5, -0.125], [0.25, 0.75, -0.125, 0.25, 0.75, 0.125, -0.25, 0.75, 0.125, -0.25, 0.75, -0.125], [0.25, 0.75, -0.125, 0.25, 1.5, -0.125, 0.25, 1.5, 0.125, 0.25, 0.75, 0.125], [-0.25, 0.75, 0.125, -0.25, 1.5, 0.125, -0.25, 1.5, -0.125, -0.25, 0.75, -0.125]],'tex_coords':[[0.03333333333333333, 0.0, 0.03333333333333333, 0.75, 0.1, 0.75, 0.1, 0.0], [0.13333333333333333, 0.0, 0.13333333333333333, 0.75, 0.2, 0.75, 0.2, 0.0], [0.03333333333333333, 0.75, 0.03333333333333333, 1.0, 0.1, 1.0, 0.1, 0.75], [0.1, 0.75, 0.1, 1.0, 0.16666666666666666, 1.0, 0.16666666666666666, 0.75], [0.1, 0.0, 0.1, 0.75, 0.13333333333333333, 0.75, 0.13333333333333333, 0.0], [0.0, 0.0, 0.0, 0.75, 0.03333333333333333, 0.75, 0.03333333333333333, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'head','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 1.5, -0.25, -0.25, 2.0, -0.25, 0.25, 2.0, -0.25, 0.25, 1.5, -0.25], [0.25, 1.5, 0.25, 0.25, 2.0, 0.25, -0.25, 2.0, 0.25, -0.25, 1.5, 0.25], [-0.25, 2.0, -0.25, -0.25, 2.0, 0.25, 0.25, 2.0, 0.25, 0.25, 2.0, -0.25], [0.25, 1.5, -0.25, 0.25, 1.5, 0.25, -0.25, 1.5, 0.25, -0.25, 1.5, -0.25], [0.25, 1.5, -0.25, 0.25, 2.0, -0.25, 0.25, 2.0, 0.25, 0.25, 1.5, 0.25], [-0.25, 1.5, 0.25, -0.25, 2.0, 0.25, -0.25, 2.0, -0.25, -0.25, 1.5, -0.25]],'tex_coords':[[0.26666666666666666, 0.0, 0.26666666666666666, 0.5, 0.3333333333333333, 0.5, 0.3333333333333333, 0.0], [0.4, 0.0, 0.4, 0.5, 0.4666666666666667, 0.5, 0.4666666666666667, 0.0], [0.26666666666666666, 0.5, 0.26666666666666666, 1.0, 0.3333333333333333, 1.0, 0.3333333333333333, 0.5], [0.3333333333333333, 0.5, 0.3333333333333333, 1.0, 0.4, 1.0, 0.4, 0.5], [0.3333333333333333, 0.0, 0.3333333333333333, 0.5, 0.4, 0.5, 0.4, 0.0], [0.2, 0.0, 0.2, 0.5, 0.26666666666666666, 0.5, 0.26666666666666666, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'hat','pivot':[0.0, 1.5, 0.0],'vertices':[[-0.25, 1.5, -0.25, -0.25, 2.0, -0.25, 0.25, 2.0, -0.25, 0.25, 1.5, -0.25], [0.25, 1.5, 0.25, 0.25, 2.0, 0.25, -0.25, 2.0, 0.25, -0.25, 1.5, 0.25], [-0.25, 2.0, -0.25, -0.25, 2.0, 0.25, 0.25, 2.0, 0.25, 0.25, 2.0, -0.25], [0.25, 1.5, -0.25, 0.25, 1.5, 0.25, -0.25, 1.5, 0.25, -0.25, 1.5, -0.25], [0.25, 1.5, -0.25, 0.25, 2.0, -0.25, 0.25, 2.0, 0.25, 0.25, 1.5, 0.25], [-0.25, 1.5, 0.25, -0.25, 2.0, 0.25, -0.25, 2.0, -0.25, -0.25, 1.5, -0.25]],'tex_coords':[[0.5333333333333333, 0.0, 0.5333333333333333, 0.5, 0.6, 0.5, 0.6, 0.0], [0.6666666666666666, 0.0, 0.6666666666666666, 0.5, 0.7333333333333333, 0.5, 0.7333333333333333, 0.0], [0.5333333333333333, 0.5, 0.5333333333333333, 1.0, 0.6, 1.0, 0.6, 0.5], [0.6, 0.5, 0.6, 1.0, 0.6666666666666666, 1.0, 0.6666666666666666, 0.5], [0.6, 0.0, 0.6, 0.5, 0.6666666666666666, 0.5, 0.6666666666666666, 0.0], [0.4666666666666667, 0.0, 0.4666666666666667, 0.5, 0.5333333333333333, 0.5, 0.5333333333333333, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'rightArm','pivot':[-0.3125, 1.375, 0.0],'vertices':[[-0.375, 0.75, -0.0625, -0.375, 1.5, -0.0625, -0.25, 1.5, -0.0625, -0.25, 0.75, -0.0625], [-0.25, 0.75, 0.0625, -0.25, 1.5, 0.0625, -0.375, 1.5, 0.0625, -0.375, 0.75, 0.0625], [-0.375, 1.5, -0.0625, -0.375, 1.5, 0.0625, -0.25, 1.5, 0.0625, -0.25, 1.5, -0.0625], [-0.25, 0.75, -0.0625, -0.25, 0.75, 0.0625, -0.375, 0.75, 0.0625, -0.375, 0.75, -0.0625], [-0.25, 0.75, -0.0625, -0.25, 1.5, -0.0625, -0.25, 1.5, 0.0625, -0.25, 0.75, 0.0625], [-0.375, 0.75, 0.0625, -0.375, 1.5, 0.0625, -0.375, 1.5, -0.0625, -0.375, 0.75, -0.0625]],'tex_coords':[[0.75, 0.125, 0.75, 0.875, 0.7666666666666667, 0.875, 0.7666666666666667, 0.125], [0.7833333333333333, 0.125, 0.7833333333333333, 0.875, 0.8, 0.875, 0.8, 0.125], [0.75, 0.875, 0.75, 1.0, 0.7666666666666667, 1.0, 0.7666666666666667, 0.875], [0.7666666666666667, 0.875, 0.7666666666666667, 1.0, 0.7833333333333333, 1.0, 0.7833333333333333, 0.875], [0.7666666666666667, 0.125, 0.7666666666666667, 0.875, 0.7833333333333333, 0.875, 0.7833333333333333, 0.125], [0.7333333333333333, 0.125, 0.7333333333333333, 0.875, 0.75, 0.875, 0.75, 0.125]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leftArm','pivot':[0.3125, 1.375, 0.0],'vertices':[[0.25, 0.75, -0.0625, 0.25, 1.5, -0.0625, 0.375, 1.5, -0.0625, 0.375, 0.75, -0.0625], [0.375, 0.75, 0.0625, 0.375, 1.5, 0.0625, 0.25, 1.5, 0.0625, 0.25, 0.75, 0.0625], [0.25, 1.5, -0.0625, 0.25, 1.5, 0.0625, 0.375, 1.5, 0.0625, 0.375, 1.5, -0.0625], [0.375, 0.75, -0.0625, 0.375, 0.75, 0.0625, 0.25, 0.75, 0.0625, 0.25, 0.75, -0.0625], [0.375, 0.75, -0.0625, 0.375, 1.5, -0.0625, 0.375, 1.5, 0.0625, 0.375, 0.75, 0.0625], [0.25, 0.75, 0.0625, 0.25, 1.5, 0.0625, 0.25, 1.5, -0.0625, 0.25, 0.75, -0.0625]],'tex_coords':[[0.8166666666666667, 0.125, 0.8166666666666667, 0.875, 0.8333333333333334, 0.875, 0.8333333333333334, 0.125], [0.85, 0.125, 0.85, 0.875, 0.8666666666666667, 0.875, 0.8666666666666667, 0.125], [0.8166666666666667, 0.875, 0.8166666666666667, 1.0, 0.8333333333333334, 1.0, 0.8333333333333334, 0.875], [0.8333333333333334, 0.875, 0.8333333333333334, 1.0, 0.85, 1.0, 0.85, 0.875], [0.8333333333333334, 0.125, 0.8333333333333334, 0.875, 0.85, 0.875, 0.85, 0.125], [0.8, 0.125, 0.8, 0.875, 0.8166666666666667, 0.875, 0.8166666666666667, 0.125]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'rightLeg','pivot':[-0.125, 0.75, 0.0],'vertices':[[-0.1875, 0.0, -0.0625, -0.1875, 0.75, -0.0625, -0.0625, 0.75, -0.0625, -0.0625, 0.0, -0.0625], [-0.0625, 0.0, 0.0625, -0.0625, 0.75, 0.0625, -0.1875, 0.75, 0.0625, -0.1875, 0.0, 0.0625], [-0.1875, 0.75, -0.0625, -0.1875, 0.75, 0.0625, -0.0625, 0.75, 0.0625, -0.0625, 0.75, -0.0625], [-0.0625, 0.0, -0.0625, -0.0625, 0.0, 0.0625, -0.1875, 0.0, 0.0625, -0.1875, 0.0, -0.0625], [-0.0625, 0.0, -0.0625, -0.0625, 0.75, -0.0625, -0.0625, 0.75, 0.0625, -0.0625, 0.0, 0.0625], [-0.1875, 0.0, 0.0625, -0.1875, 0.75, 0.0625, -0.1875, 0.75, -0.0625, -0.1875, 0.0, -0.0625]],'tex_coords':[[0.8833333333333333, 0.125, 0.8833333333333333, 0.875, 0.9, 0.875, 0.9, 0.125], [0.9166666666666666, 0.125, 0.9166666666666666, 0.875, 0.9333333333333333, 0.875, 0.9333333333333333, 0.125], [0.8833333333333333, 0.875, 0.8833333333333333, 1.0, 0.9, 1.0, 0.9, 0.875], [0.9, 0.875, 0.9, 1.0, 0.9166666666666666, 1.0, 0.9166666666666666, 0.875], [0.9, 0.125, 0.9, 0.875, 0.9166666666666666, 0.875, 0.9166666666666666, 0.125], [0.8666666666666667, 0.125, 0.8666666666666667, 0.875, 0.8833333333333333, 0.875, 0.8833333333333333, 0.125]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leftLeg','pivot':[0.125, 0.75, 0.0],'vertices':[[0.0625, 0.0, -0.0625, 0.0625, 0.75, -0.0625, 0.1875, 0.75, -0.0625, 0.1875, 0.0, -0.0625], [0.1875, 0.0, 0.0625, 0.1875, 0.75, 0.0625, 0.0625, 0.75, 0.0625, 0.0625, 0.0, 0.0625], [0.0625, 0.75, -0.0625, 0.0625, 0.75, 0.0625, 0.1875, 0.75, 0.0625, 0.1875, 0.75, -0.0625], [0.1875, 0.0, -0.0625, 0.1875, 0.0, 0.0625, 0.0625, 0.0, 0.0625, 0.0625, 0.0, -0.0625], [0.1875, 0.0, -0.0625, 0.1875, 0.75, -0.0625, 0.1875, 0.75, 0.0625, 0.1875, 0.0, 0.0625], [0.0625, 0.0, 0.0625, 0.0625, 0.75, 0.0625, 0.0625, 0.75, -0.0625, 0.0625, 0.0, -0.0625]],'tex_coords':[[0.95, 0.125, 0.95, 0.875, 0.9666666666666667, 0.875, 0.9666666666666667, 0.125], [0.9833333333333333, 0.125, 0.9833333333333333, 0.875, 1.0, 0.875, 1.0, 0.125], [0.95, 0.875, 0.95, 1.0, 0.9666666666666667, 1.0, 0.9666666666666667, 0.875], [0.9666666666666667, 0.875, 0.9666666666666667, 1.0, 0.9833333333333333, 1.0, 0.9833333333333333, 0.875], [0.9666666666666667, 0.125, 0.9666666666666667, 0.875, 0.9833333333333333, 0.875, 0.9833333333333333, 0.125], [0.9333333333333333, 0.125, 0.9333333333333333, 0.875, 0.95, 0.875, 0.95, 0.125]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}]
