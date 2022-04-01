if __name__ == "__main__":
    a, b = list(map(int, input()))[::-1], int(input())
    i, payload, ans = 0, 0, []

    while i < len(a) or payload > 0:
        if i < len(a):
            payload += a[i] * b
            i += 1
        ans.append(payload % 10)
        payload //= 10

    while len(ans) > 1 and ans[-1] == 0: ans.pop()
    ans = ans[::-1]
    print(''.join(map(str,ans)))