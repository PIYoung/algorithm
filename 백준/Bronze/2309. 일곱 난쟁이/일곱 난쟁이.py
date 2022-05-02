dwarf_list = [int(input()) for _ in range(9)]

total = sum(dwarf_list)

for i in range(9):
    isBreak = 0

    for j in range(i + 1, 9):
        if total - (dwarf_list[i] + dwarf_list[j]) == 100:
            fake1 = dwarf_list[i]
            fake2 = dwarf_list[j]

            dwarf_list.remove(fake1)
            dwarf_list.remove(fake2)

            isBreak = 1
            break

    if isBreak == 1:
        break


dwarf_list.sort()
print("\n".join(map(str, dwarf_list)))