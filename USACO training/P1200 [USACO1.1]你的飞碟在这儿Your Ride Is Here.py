def compNameToAscii(name: str):
    cnt = 1
    for s in range(len(name)):
        cnt *= ord(name[s]) - ord('@')
    return cnt


if __name__ == "__main__":
    star_name = input()
    support_name = input()

    ans = compNameToAscii(star_name) % 47 == compNameToAscii(support_name) % 47

    if ans:
        print('GO')
    else:
        print("STAY")
