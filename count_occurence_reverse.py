string = "ab2"
output = ""
digit = ""
for ch in string:
    if not ch.isdigit():
        if digit != "":
            output = (int(digit) - 1) * output[-1]
        output = output + ch
        digit = ""
    else:
        digit = digit + ch

output = output + (int(digit) - 1) * output[-1]

print(output)
