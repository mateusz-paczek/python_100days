# Program that generates randomly heads or tails

import random

heads_or_tail = random.randint(0,1)

if heads_or_tail == 0:
    print(f"Heads")
else:
    print("Tails")