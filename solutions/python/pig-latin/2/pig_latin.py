def translate(text):
    # Define vowels for easy checking
    vowels = ('a', 'e', 'i', 'o', 'u')

    # Split the input text into individual words
    words = text.split()

    # This will store the translated Pig Latin words
    result = []

    # Process each word one by one
    for word in words:

        # -------------------------------
        # RULE 1:
        # If a word starts with:
        # - a vowel (a, e, i, o, u)
        # - or "xr"
        # - or "yt"
        # Then we simply add "ay" to the end
        # Example: "apple" -> "appleay"
        # -------------------------------
        if word.startswith(vowels) or word.startswith('xr') or word.startswith('yt'):
            result.append(word + 'ay')
            continue  # Move to the next word immediately

        # -------------------------------
        # RULE 3:
        # If the word begins with consonants followed by "qu",
        # we move the whole consonant + "qu" chunk to the end.
        #
        # Example:
        # "square" -> "aresquay"
        # "quick"  -> "ickquay"
        # -------------------------------
        i = 0  # Pointer to find where the vowel sound begins

        while i < len(word):

            # Stop when we reach the first vowel
            if word[i] in vowels:
                break

            # Special case: treat "qu" as a single consonant cluster
            if word[i:i+2] == 'qu':
                i += 2  # Skip past "qu"
                break

            # Otherwise keep moving through consonants
            i += 1

        # If the consonant cluster ended in "qu",
        # apply the special "qu" transformation
        if word[i-2:i] == 'qu':
            result.append(word[i:] + word[:i] + 'ay')
            continue

        # -------------------------------
        # RULE 4:
        # If the word begins with consonants followed by "y",
        # then "y" acts like a vowel (but not if it's the first letter).
        #
        # Example:
        # "rhythm" -> "ythmrhay"
        # -------------------------------
        i = 0  # Reset pointer for scanning again

        while i < len(word):

            # Stop if we find:
            # - a vowel
            # - OR a "y" that is not at position 0
            if word[i] in vowels or (word[i] == 'y' and i != 0):
                break

            i += 1

        # If we stopped because of a "y",
        # split the word at that position
        if i < len(word) and word[i] == 'y':
            result.append(word[i:] + word[:i] + 'ay')
            continue

        # -------------------------------
        # RULE 2 (General consonant rule):
        # For normal consonant-starting words,
        # move all consonants before the first vowel to the end.
        #
        # Example:
        # "chair" -> "airchay"
        # -------------------------------
        result.append(word[i:] + word[:i] + 'ay')

    # Join all translated words back into a sentence
    return ' '.join(result)
