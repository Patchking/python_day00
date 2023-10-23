from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("line_count", help = "Enter strings count", type = int)
    args = parser.parse_args()
    print(f"first arg is {args.line_count}")
    strscount = args.line_count

    for i in range(strscount):
        innput = input().strip()
        if (len(innput) == 32 and innput[:5] == "00000" and innput[5] != "0"):
            print(innput)


if __name__ == "__main__":
    main()