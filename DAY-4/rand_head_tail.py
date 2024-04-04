"""Random Head or Tail"""

import random
random_coin = random.randint(0, 1)
if random_coin == 1:
    print("Head")
else:
    print("Tail")