## https://www.acmicpc.net/problem/20922
## 겹치는건 싫어

# 문제
# 홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다.
# 도현이를 위해 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.
# 100,000 이하의 양의 정수로 이루어진 길이가 N인 수열이 주어진다.
# 이 수열에서 같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.

# 입력
# 첫째 줄에 정수 
# N(1 <= 200,000)과 K(1 <= 100)가 주어진다.

# 둘째 줄에는 {a_1, a_2, ... a_n}이 주어진다 (1 <= 100,000)

# 출력
# 조건을 만족하는 최장 연속 부분 수열의 길이를 출력한다.

# 예제 입력 1 
# 9 2
# 3 2 5 5 6 4 4 5 7

# 예제 출력 1 
# 7

first_input = input().split(" ")
n_of_nums = int(first_input[0])
k_of_limit = int(first_input[1])
original_seq = input().split(" ")
nums = [int(k) for k in original_seq]
jinri_table = [[] for _ in range(100001)]

idx = 0
last_idx = 0
best = 0
length = 0
while idx < n_of_nums:
    if len(jinri_table[nums[idx]]) < k_of_limit:
        length += 1
    else:
        best = max(best, length)
        for i in range(last_idx, jinri_table[nums[idx]][0]):
            length -=1
            jinri_table[nums[i]].pop(0)
        last_idx = jinri_table[nums[idx]].pop(0) + 1
    jinri_table[nums[idx]].append(idx)
    idx += 1
best = max(best, length)
print(best)