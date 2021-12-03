import os
def load_array():
    """
    Loads example input
    """
    output = []
    
    with open(os.path.join(os.getcwd(), '2021/day_three/day_three.sample.txt'), 'rt') as f:
        for num in f:
            num = num.strip().replace('\n', '')
            output.append(num)

    return output

def invert_bit(bit):
    output = ""
    for char in bit:
        output += str(int(char) ^ 1)
    
    return output


def solve(binary_numbers):
    majority = len(binary_numbers) // 2
    most_common = {}
    for i in range(len(binary_numbers[0])):
        most_common[i] = 0

    for num in binary_numbers:
        for i,char in enumerate(num):
            if char == "1":
                most_common[i] += 1

    gamma = "" 
    for i in range(len(binary_numbers[0])):
        if most_common[i] > majority:
            gamma += "1"
        else:
            gamma += "0"
    
    epsilon = invert_bit(gamma)

    return int(gamma, 2) * int(epsilon, 2)

print(solve(load_array()))
