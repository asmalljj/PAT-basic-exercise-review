N = int(input())
password = []
for i in range(N):
    line = input().strip()
    parts = line.split()
    for part in parts:
        if '-' in part:
            option, answer = part.split('-')
            if answer == 'T':
                if option == 'A':
                    password.append('1')
                elif option == 'B':
                    password.append('2')
                elif option == 'C':
                    password.append('3')
                elif option == 'D':
                    password.append('4')
                break
print(''.join(password))