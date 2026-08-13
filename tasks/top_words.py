from collections import Counter
import re


def top_words(text, n):
    normalized_words = re.findall(r"[a-zA-Z]+", text.lower())

    temp_dict = {}

    # check if we've seen the word before
    for word in normalized_words:
        if temp_dict.get(word) is not None:
            temp_dict[word] = temp_dict[word] + 1
        else:
            temp_dict[word] = 1

    # Convert dictionary to a list of tuples
    sorted_temp = list(temp_dict.items())

    # Sort by the count (second element of each tuple)
    sorted_temp.sort(key=lambda item: item[1], reverse=True)

    return sorted_temp[:n]


def top_words2(text, n):
    normalized_words = re.findall(r"[a-zA-Z]+", text.lower())

    temp_dict = {}

    # check if we've seen the word before
    for word in normalized_words:
        temp_dict[word] = temp_dict.get(word, 0) + 1

    # Convert dictionary to a list of tuples
    sorted_temp = list(temp_dict.items())

    # Sort by the count (second element of each tuple)
    sorted_temp.sort(key=lambda item: item[1], reverse=True)

    return sorted_temp[:n]


def top_words3(text, n):
    return Counter(re.findall(r"[a-zA-Z]+", text.lower())).most_common(n)

print(top_words3(",tHe, boY iS Going to the market", 2))