import random

def randomListGenerator(LIST_SIZE, MIN_VALUE, MAX_VALUE):
    # Generate random list
    random_list = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(LIST_SIZE)]
    return random_list

if __name__ == "__main__":
    random_list = randomListGenerator(10, 1, 100)
    print(random_list)