lines = []
print("If there was any already existing text in inputs.txt, please remove them before adding more."
      "\nI can't be bothered to learn how to clear it within the program itself."
      "\nPut BizHawk inputs here (press enter twice):")
while True:
    # User input
    userinput = input()

    # Convert specific inputs into DSM format
    if 'R' in userinput:
        right = 'R'
    else:
        right = '.'

    if 'L' in userinput:
        left = 'L'
    else:
        left = '.'

    if 'D' in userinput:
        down = 'D'
    else:
        down = '.'

    if 'U' in userinput:
        up = 'U'
    else:
        up = '.'

    if 'B' in userinput:
        b = 'B'
    else:
        b = '.'

    if 'A' in userinput:
        a = 'A'
    else:
        a = '.'

    if 'Y' in userinput:
        y = 'Y'
    else:
        y = '.'

    if 'X' in userinput:
        x = 'X'
    else:
        x = '.'

    if 'S' in userinput:
        start = 'T'
    else:
        start = '.'

    if 's' in userinput:
        sel = 'S'
    else:
        sel = '.'

    if 'l' in userinput:
        l = 'E'
    else:
        l = '.'

    if 'r' in userinput:
        r = 'W'
    else:
        r = '.'

    if userinput:
        lines.append(userinput)
    else:
        break

    output_string = "|0|" + right + left + down + up + start + sel + b + a + y + x + r + l + ".000 000 0|"

    with open('inputs.txt', 'a') as f:
        f.write(output_string + '\n')

print("Exported as inputs.txt")
