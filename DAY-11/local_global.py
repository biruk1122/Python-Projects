enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies Inside Function: {enemies}")

increase_enemies()
print(f"Enemies Outside Function: {enemies}")
