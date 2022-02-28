def find_highest_frequency_character(s):
    character_counter = {}
    max_frequency_character = 'a'
    max_frequency = 0
    for character in s:
        character_counter[character] = character_counter.get(character, 0) + 1
        if max_frequency < character_counter.get(character):
            max_frequency_character = character
            max_frequency = character_counter.get(character)
    return max_frequency_character


if __name__ == '__main__':
    print(find_highest_frequency_character(input()))
