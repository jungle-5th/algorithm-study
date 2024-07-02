from sys import stdin
input = stdin.readline

def editor(original_string, n_edit_cmd):

    left = original_string
    right = ''
    
    for i in range(n_edit_cmd):
        edit_cmd = input().rstrip()
        
        if(edit_cmd) == 'L':
            if 0 < len(left):
                right = left[len(left) - 1] + right
                left = left[0:len(left)-1]
        
        elif(edit_cmd) == 'D':
            if 0 < len(right):
                left = left + right[0]
                right = right[1:len(right)]
        
        elif(edit_cmd) == 'B':
            if 0 < len(left):
                left = left[0:len(left)-1]
        else:
            cmd, char = edit_cmd.split(' ')
            left = left + char
    print(left + right)
    return

original_string = input().rstrip()
n_edit_cmd = int(input())

editor(original_string, n_edit_cmd)