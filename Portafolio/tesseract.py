from mayavi import mlab
import numpy as np

def tesseract():
    points = np.array([[1, 1, 1, 1],
                       [1, 1, 1, -1],
                       [1, 1, -1, 1],
                       [1, 1, -1, -1],
                       [1, -1, 1, 1],
                       [1, -1, 1, -1],
                       [1, -1, -1, 1],
                       [1, -1, -1, -1],
                       [-1, 1, 1, 1],
                       [-1, 1, 1, -1],
                       [-1, 1, -1, 1],
                       [-1, 1, -1, -1],
                       [-1, -1, 1, 1],
                       [-1, -1, 1, -1],
                       [-1, -1, -1, 1],
                       [-1, -1, -1, -1]])

    faces = [[0, 1, 3, 2], [4, 5, 7, 6], [0, 4, 6, 2], [1, 5, 7, 3], [2, 3, 7, 6], [0, 1, 5, 4]]

    mlab.figure(bgcolor=(1, 1, 1), size=(400, 400))
    mlab.triangular_mesh([point[0] for point in points],
                         [point[1] for point in points],
                         [point[2] for point in points],
                         [point[3] for point in points],
                         faces,
                         color=(0, 0, 0))
    mlab.show()

tesseract()
