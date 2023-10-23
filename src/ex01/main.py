import sys

def main():
    if (len(sys.argv) != 2):
        print(f"""Wrong argument count!
              Excepted: 1
              Got: {len(sys.argv) - 1}""")
        return
    strs = sys.argv[1].split()
    print("".join(word[0] for word in strs))

if __name__ == "__main__":
    main()