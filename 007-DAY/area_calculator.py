"""Paint Area Calculator"""

import math
def print_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll Need {round_up_cans} cans of Point")

test_h = int(input("Enter Height of Wall "))
test_w = int(input("Enter Width of Wall "))
coverage = 5
print_calc(height= test_h, width= test_w, cover= coverage)
