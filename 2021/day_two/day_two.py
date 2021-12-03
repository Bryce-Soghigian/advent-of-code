def load_input():
    import os
    output = []
    with open(os.path.join(os.getcwd(), '2021/day_two.txt'), 'rt') as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(" ")
            output.append((line[0],int(line[1])))
    return output


class SubmarineTraverse:

    def __call__(self, movements):
        depth = 0
        horizontal = 0
        aim = 0
        for command,unit in movements:
            
            if command == 'down':
                aim +=  unit
            elif command == 'up':
                aim -= unit
            else:
                horizontal += unit
                depth += aim * unit

        return depth * horizontal

sea_traversal = SubmarineTraverse()
print(sea_traversal(load_input()))