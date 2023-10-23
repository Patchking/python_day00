import sys

def main():
    strscount = 0
    if (len(sys.argv) != 2):
        print(f"""Wrong argument count!
              Excepted: 1
              Got: {len(sys.argv) - 1}""")
        return
    try:
        strscount = int(sys.argv[1])
    except ValueError:
        print("Argument not a number")
        return

    for i in range(strscount):
        innput = input()
        if (len(innput) == 32 and innput[:5] == "00000" and innput[5] != "0"):
            print(innput)


if __name__ == "__main__":
    main()