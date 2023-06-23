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


def calculate_final_positions(N, M, T, ant_positions):
    final_positions = []

    for ant in ant_positions:
        position, direction = ant

        # Calculate the net displacement after T seconds
        displacement = (T * direction) % N

        # Calculate the final position
        final_position = (position + displacement) % N

        # Handle the case where the final position becomes 0
        if final_position == 0:
            final_position = N

        final_positions.append(final_position)

    final_positions.sort()
    return final_positions


# Read input
N, M, T = map(int, input().split())
ant_positions = []
for _ in range(M):
    position, direction = map(int, input().split())
    ant_positions.append((position, direction))

# Get final positions
result = calculate_final_positions(N, M, T, ant_positions)

# Print final positions
for position in result:
    print(position, end=' ')

