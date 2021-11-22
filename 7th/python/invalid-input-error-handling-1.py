def get_count(words=None):
    try:
        assert words, str
        clean = "".join([ c if c.isalnum() else "" for c in words.lower() ])
        vowels = sum(map(lambda letter: 1, filter(lambda letter: letter in 'aeiou', clean)))
        consonants = sum(map(lambda letter: 1, filter(lambda letter: letter not in 'aeiou', clean)))
        return {"vowels": vowels,"consonants": consonants}
    except:
        return {"vowels": 0, "consonants": 0}
