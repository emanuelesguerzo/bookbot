def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_chars(file_contents):
    chars = {}
    for char in file_contents.lower():      
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted_list(chars):
    sorted_chars = []
    for key, value in chars.items():
        sorted_chars.append({"char": key, "num": value})
    sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars