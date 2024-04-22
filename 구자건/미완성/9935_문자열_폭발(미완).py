from sys import stdin
def artful_explosion(string_Line, boomers):
    pp_range = len(boomers) - 1 
    before_string_len = len(string_Line)
    after_string_len = len(string_Line-1)
    while(before_string_len != after_string_len):
        sp = pp_range
        while sp < before_string_len :
            if boomers[pp_range] != string_line[sp]:
                if string_line[sp] in boomers:
                    sp += moving_table[string_line[sp]]
                    break
                else:
                    sp += pp_range+1
                    break
            i = 0
            while i <= pp_range:
                if string_Line[sp - 1] == boomers[pp_range - i]:
                    i -=
                else
    return

string_line = list(map(int, stdin.readline().rstrip()))
boomers = list(map(int, stdin.readline().rstrip()))
moving_table = dict()