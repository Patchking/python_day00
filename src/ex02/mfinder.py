from argparse import ArgumentParser

def compare_strs(orig_strs, input_strs) -> bool:
    for i in range(3):
        for j in range(5):
            if orig_strs[i][j] == "*" and input_strs[i][j] == "*":
                continue
            if orig_strs[i][j] == "#" and input_strs[i][j] != "*":
                continue
            return False
    return True

def main():
    parser = ArgumentParser()
    args = parser.parse_args()
    orig_strs = ["*###*", 
                 "**#**",
                 "*#*#*"]
    input_strs = []
    for i in range(3):
        input_strs.append(input())

    is_equal = False
    try:
        is_equal = compare_strs(orig_strs, input_strs)
    except IndexError:
        print("Error")
        return

    if is_equal:
        print("True")
    else:
        print("False")



if __name__ == "__main__":
    main()