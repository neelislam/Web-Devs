char = input("Enter character: ")
histo = input("Enter histogram: ")

list_histo = list(histo)
print(list_histo)

for n in list_histo:
    output = ""
    times = int(n)
    while times > 0:
        output += char
        times -= 1
    print(output)
