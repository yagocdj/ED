vowels = ['a', 'e', 'i', 'o', 'u']

s = 'eu me chamo fulanoo'
vowels_counter = 0
for char in s:
    if char in vowels:
        vowels_counter += 1

print(vowels_counter)
