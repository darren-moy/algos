"""
In a country X, all the ants move in a circle. There is a circle marked with N marks with numbers from 1to N
clockwise. There are M ants on the circle. No two ants stand on the same mark initially. It is also known in which direction each ant will move.
If two ants meet during the movement, then each of them begins to move in a different direction. Your task is to determine where the ants will be after T
seconds of such movement.

Input format:
The first line contains the numbers  N, M, T.
The following M lines have the following format:
Each line contains two numbers x and y.
The first number of this line xis the position of the ant, the second number of this line yis the direction in which the ant moves. Here, y = 1
,if the ant starts to move clockwise and y = -1, if counterclockwise.
The distances between adjacent marks are the same. In one second, the ant overcomes a distance equal to the distance between adjacent marks on the circle.

Output format
In the first line, print M integers in ascending order denoting the positions where the ants will be in T seconds after such obsessive moves.

"""


def get_final_pos(mark, ants, secs, ant_position):
    final_pos = []

    for ant in ant_position:
        position, direction = ant

        displacement = (secs * direction) % mark            #to get how many marks it moves
        final_pos = (position + displacement)               #to get the final position

        if final_pos == 0:
            final_pos = mark

        final_pos.append(final_pos)

    final_pos.sort()
    return final_pos


N, M, T = map(int, input().split())
ant_pos = []
for _ in range(M):
    position, direction = map(int, input().split())
    ant_pos.append((position, direction))

res = get_final_pos(N, M, T, ant_pos)

for position in res:
    print(position, end=' ')


