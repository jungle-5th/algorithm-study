from sys import stdin
from heapq import heappush, heappop
def frog_mating():
    min_health_drain = 2*(10**9)
    min_frog = 0
    count = 0
    for frog in frog_coordinates:
        count += 1
        distance = abs(frog - my_location)
        jump_health_drain = 0
        
        first_max_jump = min(distance, jump_range)
        jump_health_drain += jump_range - first_max_jump
        distance -= first_max_jump
            
        second_max_jump = min(distance, jump_range)
        second_jump_drain = jump_range - second_max_jump
        jump_health_drain += second_jump_drain 
        distance -= second_max_jump
        
        jump_health_drain += distance * health_drain
            
        if jump_health_drain < min_health_drain:
            min_health_drain = jump_health_drain
            min_frog = count
    
    print(f"{min_health_drain} {min_frog}")
    return

my_location, n_frog = map(int, stdin.readline().split(' '))

frog_coordinates = list(map(int, stdin.readline().split(' ')))

jump_range, health_drain = map(int, stdin.readline().split(' '))

frog_mating()