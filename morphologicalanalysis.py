
add_delete_table = [
    ("", "ing", 1),  # remove 'ing' suffix
    ("", "ed", 1),   # remove 'ed' suffix
    ("", "s", 1),    # remove 's' suffix
    ("e", "ing", 1), # replace 'ing' with 'e'
]

def apply_rule(word, add, delete, position):
    # Check if the word ends with the suffix to be deleted
    if position == 1 and word.endswith(delete):
        return word[:-len(delete)] + add
    return None

def morphological_analysis(word):
    results = set()

    for add, delete, position in add_delete_table:
        modified_word = apply_rule(word, add, delete, position)
        if modified_word:
            results.add(modified_word)
    return results if results else {word}


word = input("Enter a word: ")
analyzed_forms = morphological_analysis(word)

print(f"Analyzed forms of '{word}':")
for form in analyzed_forms:
  print(form)
