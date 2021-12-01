def load_array():
    """
    Loads example input
    """
    output = []
    
    with open('/Users/root1/Desktop/dev/advent-of-code/2021/day_one.txt', 'rt') as f:
        for num in f:
            num = int(num.strip().replace('\n', ''))
            output.append(num)

    return output


def main(nums):
    if len(nums) == 1:
        return 0
    output = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            output += 1
    return output

main(load_array())