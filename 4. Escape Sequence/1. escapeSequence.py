print("Welcome to GeekyShows")
print("Welcome to\nGeekyShows")
print("Welcome to\tGeekyShows")
print("Welcome to \"GeekyShows\" ")
print("Welcome to \'GeekyShows\' ")

# \n --- new line
# \t --- tab
# "\whatever\"
# '\whatever\'


# strings = ["eat","tea","tan","ate","nat","bat"]

# Output:  [["bat"],["nat","tan"],["ate","eat","tea"]]

# x=" ".join(reversed(strings))
# y = " ".join(strings)
# z = " ".join(map(str, strings))
# print(y)
# print(x)
# print(z)

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}
for word in strings:
    key = tuple(sorted(word))  # Sort the word and use it as a key
    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(word)

result = list(anagrams.values())
print(result)


  


