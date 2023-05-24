from queue import PriorityQueue


# priority queque object
pq = PriorityQueue()


def dijkstra_algo(matrix, start, end):
    # algorithm params
    NEIGHBORS_LEN = 4
    n = len(matrix)
    path = set()
    distances = [[float('inf')] * n for _ in range(n)]
    distances[start[0]][start[1]] = 0
    prev_nodes = [[None] * n for _ in range(n)]
    visited = set()

    # begin with start location
    pq.put((0, start))

    # start algorithm
    while not pq.empty():
        # retrieve element from priority queue
        dist, node = pq.get()

        # check if end node has been reached
        if node == end:
            break

        if node in visited:
            continue

        visited.add(node)


        # generate neighbors of node
        neighbors = []
        neighbors_set = [
            (node[0]+1, node[1]),
            (node[0]-1, node[1]),
            (node[0], node[1]+1),
            (node[0], node[1]-1)
        ]

        # check if neighbors of nth node are valid
        for i in range(NEIGHBORS_LEN):
            if i < len(neighbors_set):
                neighbor = neighbors_set[i]
                try:
                    if neighbor[0] == -1 or neighbor[1] == -1:
                        pass
                    else:
                        val = matrix[neighbor[0]][neighbor[1]]
                        neighbors.append(neighbor)

                except IndexError:
                    print('An out of bounce error occurred at: ', neighbor)
        
        # compare value of each neigbor
        for i in range(len(neighbors)):
            neighbor_x, neighbor_y = neighbors[i]
            neighbor_val = matrix[neighbors[i][0]][neighbors[i][1]]

            if neighbor_val == 1:   # free cell
                # make magic happen
                distance = dist + 1
                if distance < distances[neighbor_x][neighbor_y]:
                    # update new neighbor
                    distances[neighbor_x][neighbor_y] = distance
                    prev_nodes[neighbor_x][neighbor_y] = node

                    # add neighbor to priority queue
                    pq.put((distance, (neighbor_x, neighbor_y)))
                
    # Reconstruct the shortest path
    node = end
    while node != start:
        path.add(node)
        node = prev_nodes[node[0]][node[1]]
    path.add(start)

    return sorted(path)

def main():
    # path matrix
    matrix = [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ]

    # start and end goal
    start = (0, 0)
    end = (2, 2)

    # find path using dijkstra algorithm
    generated_path = dijkstra_algo(matrix, start, end)

    if len(generated_path) == 0:
        # no path generated
        print('No path found')

    else:
        # path found
        print('the generated path is: \n', generated_path)

if __name__ == "__main__":
    main()