
from collections import defaultdict



def get_input():
    """
    Load all lines as tuples
    """

    line_segments = []
    smallest_x = float('inf')
    smallest_y = float('inf')
    greatest_x = float('-inf')
    greatest_y = float('-inf')
    import os
    with open(os.path.join(os.getcwd(), "2021/day_five/large_input.txt"), 'rt') as file:

        for line in file:
            coords = line.replace("\n", '').split(" ")

            origin_x, origin_y = [int(item) for item in coords[0].split(",")]
            dest_x, dest_y = [int(item) for item in coords[2].split(",")]
            line_segment = (origin_x, origin_y, dest_x, dest_y)
            smallest_x = min(smallest_x, origin_x, dest_x)
            greatest_x = max(greatest_x, origin_x, dest_x)
            smallest_y = min(smallest_y, origin_y, dest_y)
            greatest_y = max(greatest_y, origin_y, dest_y)
            line_segments.append(line_segment)
        
        return {
            'line_segments': line_segments,
            'boundary_points': ([smallest_x, smallest_y], [greatest_x, greatest_y])
        }

print(get_input())


class Solution:
    def __init__(self, line_segments, boundary_points) -> None:

        self.start = boundary_points[0]
        self.end = boundary_points[1]
        self.segments = line_segments
        self.graph = self._build_graph()

        
    def _build_graph(self):
        """
        generate all coordinates from start to end 
        """


        graph = defaultdict(int)


        for x in range(self.start[0], self.end[0]+1):

            for y in range(self.start[1], self.end[1]+1):
                graph[f'{x},{y}'] = 0
        
        return graph

    def _mark_graph(self, segment):

        x1,y1, x2,y2 = segment
        if x1 == x2:
            # mark graph in y range
            for point in range(y1, y2):
                print(point)
                self.graph[f'{x1},{point}'] += 1
            
        else:
            # mark grpah in x range
            for point in range(x1, x2):
                self.graph[f'{y1},{point}'] += 1


    def _count_intersections(self):
        count = 0
        for num in self.graph.values():
            if num >= 2:
                count += 1
        return count
    def __call__(self):
        """
        1. mark all ndoes in line segment
        2. count intersections greater than >= 2

        """
        for segment in self.segments:
            print(segment,"segment")
            self._mark_graph(segment)

        return self._count_intersections()
        
        
new_inp = get_input()
line_segments, boundarys = new_inp['line_segments'], new_inp['boundary_points']
new_solution = Solution(line_segments=line_segments, boundary_points=boundarys)
print(new_solution())
