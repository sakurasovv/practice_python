alphabet = {
    " ": 0,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
rom = "MMCMXIX"
number = 0
skip = False
for i in range(1, len(rom)):
    if skip :
        skip = False
        continue
    else :
        if alphabet[rom[i - 1]] < alphabet[rom[i]]:
            number = number + (alphabet[rom[i]] - alphabet[rom[i - 1]]) * rom.count(rom[i - 1] + rom[i])
            rom = rom.replace(rom[i - 1] + rom[i], "  ")
            skip = True
for i in rom:
    number += alphabet[i]
print(number)