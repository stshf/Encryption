import random


def main():
    print("---key generator for simple substitution cipher---")
    
    permutation = [i for i in range(26)]
    temp = permutation[:]
    while temp == permutation:
        random.shuffle(permutation)

    print(" ".join([str(p) for p in permutation]))

if __name__ == "__main__":
    main()
