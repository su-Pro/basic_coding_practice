n = int(input())
temp = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
cnt = 0
if n == 0:
    print('zero')
    exit()
while n:
    cnt += n % 10
    n //= 10

# 15 => one five
for ch in str(cnt):
    print(temp[int(ch)],end=' ')
