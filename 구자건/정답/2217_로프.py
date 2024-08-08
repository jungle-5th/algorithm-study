from sys import stdin

def rope(n_rope):
    result = 0
    rope_list = list()
    for i in range(n_rope):
        rope_list.append(int(stdin.readline()))
    rope_list.sort()
    for i in range(n_rope):
        result = max(result , rope_list[i] * (n_rope-i))
    
    return result

n_rope = int(stdin.readline())
print(rope(n_rope))