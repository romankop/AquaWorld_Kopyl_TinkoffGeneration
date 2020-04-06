import random
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.image as mpimg


def count_animals(mas_search, x_pos, y_pos, animal_id):
    counter = 0
    horizon = (-1, 0, 1)
    vertical = (-1, 0, 1)
    for hor in horizon:
        for ver in vertical:
            try:
                if mas_search[y_pos + ver][x_pos + hor] == animal_id and (hor, ver) != (0, 0):
                    counter += 1
            except:
                pass
    return counter


zor = 2
n, m = (10, 10)
sea = [[random.randint(1, 4) for j in range(m)] for i in range(n)]
colors = {1: 'gray', 2: 'b', 3: 'b', 4: 'b'}
# 1 - скала
# 2 - пустота
# 3 - рыба
# 4 - креветка
cave = mpimg.imread('cave.png')
fish = mpimg.imread('clown-fish.png')
shrimp = mpimg.imread('shrimp.png')

aqua = plt.figure()
ax = plt.gca(xlim=(0, m), ylim=(0, n))

while True:
    for i in range(len(sea)):
        for j in range(len(sea[i])):
            ax.add_patch(Rectangle((j, i), 1, 1, color=colors[sea[i][j]], zorder=zor))
            if sea[i][j] == 1:
                plt.imshow(cave, extent=(j, j + 1, i, i + 1), zorder=zor + 1)
            if sea[i][j] == 3:
                plt.imshow(fish, extent=(j, j + 1, i, i + 1), zorder=zor + 1)
            if sea[i][j] == 4:
                plt.imshow(shrimp, extent=(j, j + 1, i, i + 1), zorder=zor + 1)
    plt.pause(1)
    zor += 1

    sea_old = sea.deepcopy()
    for i in range(len(sea_old)):
        for j in range(len(sea_old[i])):
            if sea_old[i][j] == 1:
                sea[i][j] = 1
            if sea_old[i][j] == 2:
                if count_animals(sea_old, j, i, 3) == 3:
                    sea[i][j] = 3
                elif count_animals(sea_old, j, i, 4) == 3:
                    sea[i][j] = 4
                else:
                    sea[i][j] = 2
            if sea_old[i][j] == 3:
                if count_animals(sea_old, j, i, 3) < 2 or count_animals(sea_old, j, i, 3) >= 4:
                    sea[i][j] = 2
                else:
                    sea[i][j] = 3
            if sea_old[i][j] == 4:
                if count_animals(sea_old, j, i, 4) < 2 or count_animals(sea_old, j, i, 4) >= 4:
                    sea[i][j] = 2
                else:
                    sea[i][j] = 4

plt.show()
