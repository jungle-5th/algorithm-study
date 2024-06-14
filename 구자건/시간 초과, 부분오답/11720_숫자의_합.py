from sys import stdin
def sum_of_bitch():
    n_number = int(stdin.readline())
    num_list = list(map(int, stdin.readline().rstrip()))
    print(sum(num_list))
    return
sum_of_bitch()