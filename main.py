def main():
    file_path = "books/frankenstein.txt"
    file_text = get_file_text(file_path)
    print(f"--- Begin report of {file_path} ---")

    word_count = get_word_count(file_text)
    print(f"{word_count} words found in the document")

    print_counts_sorted(file_text)

    


def get_file_text(path: str):
    with open(path) as f:
        text = f.read()
        return text


def get_word_count(text: str):
    words = text.split()
    return len(words)


def get_char_count_dict(text: str):
    count_dict = {}
    for c in text.lower():
        if not c.isalpha():
            continue
        if not c in count_dict:
            count_dict[c] = 0
        count_dict[c] += 1
    return count_dict


def get_sorted_char_count_list(count_dict: dict):
    count_list = []
    for c in count_dict:
        count_list.append({
            "char": c,
            "count": count_dict[c]
        })
    count_list.sort(key=sort_by_count, reverse=True)
    return count_list


def sort_by_count(e):
    return e["count"]


def print_counts_sorted(text: str):
    count_dict = get_char_count_dict(text)
    count_list = get_sorted_char_count_list(count_dict)

    for e in count_list:
        print(f"The '{e["char"]}' character was found {e["count"]} times")


main()