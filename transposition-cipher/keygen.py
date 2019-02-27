import random


def main():
    print("---key generator for transportation cipher---")
    print("input split number")
    n = int(input())
    
    permutation = [i for i in range(n)]
    temp = permutation[:]
    while temp == permutation:
        random.shuffle(permutation)

    print(" ".join([str(p) for p in permutation]))

if __name__ == "__main__":
    main()
