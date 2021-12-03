import os
def load_array():
    """
    Loads example input
    """
    output = []
    
    with open(os.path.join(os.getcwd(), '2021/day_three/day_three.txt'), 'rt') as f:
        for num in f:
            num = num.strip().replace('\n', '')
            output.append(num)

    return output


def most_frequent_bit(bits,position, most_common):

    matching_one_bits = set()
    matching_zero_bits = set()
    mc = None
    lc = None

    for bit in bits:
        if bit[position] == "1":
            matching_one_bits.add(bit)
        else:
            matching_zero_bits.add(bit)


    if len(matching_one_bits) >= len(matching_zero_bits):
        mc = (matching_one_bits, position, 1)
        lc = (matching_zero_bits, position, 0)
    else:

        mc = (matching_zero_bits, position, 0)
        lc = (matching_one_bits, position, 1)

    if most_common:
        return mc
    return lc

def bfs(binary_numbers, most_common=True):

    from collections import deque
    boundary = len(binary_numbers[0]) -1

    queue = deque([most_frequent_bit(binary_numbers, 0, most_common)])

    while queue:

        bit_grouping, position, most_common_bit = queue.popleft()
        if position == boundary:
            position = -1

        if len(bit_grouping) == 1:
            return list(bit_grouping)[0]
        
        new_groupings = most_frequent_bit(bit_grouping, position+1, most_common)
        queue.append(new_groupings)


def solve(binary_numbers):

    oxygen_rating = bfs(binary_numbers)
    carbon_rating = bfs(binary_numbers,most_common=False)

    return int(oxygen_rating,2) * int(carbon_rating, 2)

print(solve(load_array()))