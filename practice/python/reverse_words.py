def reverse_words(words_in_list):
    total_len = len(words_in_list)
    half_len = total_len//2
    i = 0
    while i < half_len:
        tmp = words_in_list[i]
        words_in_list[i] = words_in_list[total_len - (i+1)]
        words_in_list[total_len - (i + 1)] = tmp
        i += 1
    return words_in_list

def split_by_space_and_reverse(words_in_list):
    print(words_in_list)
    total_len = len(words_in_list)
    reversed_words = []
    cur_word = []
    for i, c in enumerate(words_in_list):
        if c == ' ':
            print(i, cur_word)
            reversed_words += reverse_words(cur_word) + [' ']
            cur_word = []
        elif i == (total_len-1):
            print(i, c)
            cur_word.append(c)
            reversed_words += reverse_words(cur_word)
        else:
            print(i, c)
            cur_word.append(c)
    return reversed_words

if __name__ == '__main__':
    words = ['c', 'a', 'k', 'e', ' ',
             'p', 'o', 'u', 'n', 'd', ' ',
             's', 't', 'e', 'a', 'l' ]

    print(words)
    rv = reverse_words(words)
    print(rv)
    print(split_by_space_and_reverse(rv))
    # print(split_by_space_and_reverse(reverse_words(words))) does not work as expected because of the way Python pass variables as references
