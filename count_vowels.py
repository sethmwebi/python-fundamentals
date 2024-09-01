def count_vowels(text: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counts = [vowel for vowel in text if vowel in vowels]
    return len(vowel_counts)


print(count_vowels("rebeccapurple"))
