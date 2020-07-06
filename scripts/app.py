import argparse
import random

def display(word):
    version_num = random.randint(0, 500)
    final = f"{word}-{version_num}"
    return final

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dislplay information for demo")
    parser.add_argument('--word', metavar='word', required=False, type=str,default='Jouate', help='enter a word.')
    args = parser.parse_args()
    print(display(args.word))
