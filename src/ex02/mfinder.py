from argparse import ArgumentParser

def is_input_correct(input_strs, orig_size):
    for i in range(orig_size[1]):
        if len(input_strs[i]) != orig_size[0]:
            return False
    return True

def compare_strs(orig_strs, input_strs, orig_size) -> bool:
    if not is_input_correct(input_strs, orig_size):
        raise IndexError
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
    orig_size = (len(orig_strs[0]), len(orig_strs))
    for i in range(3):
        input_strs.append(input())

    is_equal = False
    try:
        is_equal = compare_strs(orig_strs, input_strs, orig_size)
    except IndexError:
        print("Error")
        return

    if is_equal:
        print("True")
    else:
        print("False")



if __name__ == "__main__":
    main()