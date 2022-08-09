T = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(T):
    word = list(input())
    for vowel in vowels:
        for s in range(word.count(vowel)):
            word.remove(vowel)
    print(f'#{i+1} {"".join(word)}')    
