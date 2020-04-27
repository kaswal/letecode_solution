def valid_anagram(s, t):
    if sorted(t) != sorted(s):
        return "false"
    else:
        return "true"

print(valid_anagram('anagram', 'nagaram'))
