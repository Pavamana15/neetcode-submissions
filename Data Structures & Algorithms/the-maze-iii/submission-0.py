class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        def dijkstra(maze, start, distance):
            dirs = {
                'r': (0, 1),
                'l': (0, -1),
                'u': (-1, 0),
                'd': (1, 0)
            }

            queue = []
            heapq.heappush(queue, (0, [], start[0], start[1]))  # FIX 1

            while queue:
                dist, inst, sx, sy = heapq.heappop(queue)

                if distance[sx][sy]['dist'] < dist:
                    continue

                for direction, (dx, dy) in dirs.items():
                    x, y = sx, sy
                    count = 0
                    hit_hole = False

                    while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                        x += dx
                        y += dy
                        count += 1
                        if [x, y] == hole:
                            hit_hole = True
                            break

                    nx, ny = (x, y) if hit_hole else (x, y)

                    new_dist = dist + count
                    new_path = inst + [direction]

                    if new_dist < distance[nx][ny]['dist'] or new_dist == distance[nx][ny]['dist'] and new_path < distance[nx][ny]['dirs']:
                        distance[nx][ny]['dist'] = new_dist
                        distance[nx][ny]['dirs'] = new_path
                        heapq.heappush(queue, (new_dist, new_path, nx, ny))  # FIX 4

        distance = [
            [{'dist': float('inf'), 'dirs': []} for _ in range(len(maze[0]))]
            for _ in range(len(maze))
        ]

        distance[ball[0]][ball[1]] = {'dist': 0, 'dirs': []}
        dijkstra(maze, ball, distance)

        return (
            'impossible'
            if distance[hole[0]][hole[1]]['dist'] == float('inf')
            else ''.join(distance[hole[0]][hole[1]]['dirs'])
        )
