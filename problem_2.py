'''

Input Format:
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Output Format:
For each command of type print, print the list on a new line.

Smaple input :

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''


# Solve that probems :

list_of_num = []
for _ in range(0, int(input())):
    user_input = input().split(' ')
    command = user_input.pop(0)
    if len(user_input) > 0:
        if 'insert' == command:
            eval("list_of_num.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
        else:
            eval("list_of_num.{0}({1})".format(command, user_input[0]))
    elif command == 'print':
        print(list_of_num)
    else:
        eval("list_of_num.{0}()".format(command))