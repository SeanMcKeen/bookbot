def get_word_count(text):
    words = 0

    for word in text.split():
        words += 1
    return words

def get_character_count(text):
    character_counts = {}

    for c in text:
        c = c.lower()
        if c not in character_counts:
            character_counts[c] = 1
        else:
            character_counts[c] += 1
    return character_counts

def sort_on(dict):
    return dict["count"]

def get_sorted_list(dict):
    dict_list = [{"char": k, "count": v} for k, v in dict.items()]

    dict_list.sort(key=sort_on, reverse=True)
    return dict_list