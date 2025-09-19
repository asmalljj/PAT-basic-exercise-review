def compression(s):
    result = ""
    i = 0
    while i < len(s):
        count = 1
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            count += 1
            j += 1
        if count > 1:
            result += str(count) + s[i]
        else:
            result += s[i]
        i = j
    return result
def decompression(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            if i < len(s):
                count = int(num_str)
                char = s[i]
                result += char * count
                i += 1
        else:
            result += s[i]
            i += 1
    return result

way = input().strip()
content = input().strip()

if way == 'C':
    print(compression(content))
elif way == 'D':
    print(decompression(content))
else:
    print("你输入了一个错误的方式")
