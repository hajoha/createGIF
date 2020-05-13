import numpy as np
import imageio
import os


def getFileName(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))
    return files


def createOutPut(path, i):
    images = []
    for filename in path:
        images.append(imageio.imread(filename))
    imageio.mimsave('output/test'+str(i)+'.gif', images, duration=0.4)


if __name__ == '__main__':
    inputPath = 'frame'
    path = getFileName(inputPath)
    pathNP = np.asarray(path)
    assert len(path) % 2 == 0
    for k, i in enumerate(range(0, len(path), 2)):
        createOutPut(pathNP[i:i+2], k)
