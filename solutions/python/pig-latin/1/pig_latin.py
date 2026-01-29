def translate(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    words = text.split()
    result = []
    for word in words:
        # rule 1
        if word.startswith(vowels) or word.startswith('xr') or word.startswith('yt'):
            result.append(word + 'ay')
            continue

        # rule 3: begins with zero/more consonants followed by 'qu'
        i = 0
        while i < len(word):
            if word[i] in vowels:
                break
            if word[i:i+2] == 'qu':
                i += 2
                break
            i += 1
            
        if word[i-2:i] == 'qu':
            result.append(word[i:] + word[:i] + 'ay')
            continue

        # rule 4: begins with one/more consonants followed by 'y'
        i = 0
        while i < len(word):
            if word[i] in vowels or (word[i] == 'y' and i != 0):
                break
            i += 1
            
        if i < len(word) and word[i] == 'y':
            result.append(word[i:] + word[:i] + 'ay')
            continue

        # rule 2: general consonant rule
        result.append(word[i:] + word[:i] + 'ay')

    return ' '.join(result)
        