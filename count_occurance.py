string = "aab"
output = string[0]
count = 0

for ch, idx in string:
    if string[idx] != string[idx - 1]:
        output = output + str(count)
        output = output + ch
        count = 1

    else:
        count += 1

output = output + str(count)

print(output)
