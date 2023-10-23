from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("string", help = "Input string that contains ciphered message", type = str)
    args = parser.parse_args()
    strs = args.string.split()
    print("".join(word[0] for word in strs))

if __name__ == "__main__":
    main()