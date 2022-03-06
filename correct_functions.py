import string
import pandas as pd


def check_word(word):

    def generate_transposes(p):

        result = []

        for i in range(0, len(p) - 1):
            l = p[:i]
            c1 = p[i]
            c2 = p[i + 1]
            r = p[i + 2:]
            n = l + c2 + c1 + r
            result.append(n)

        return result

    def generate_missing_letter(p):

        result = []

        for i in range(0, len(p) + 1):
            l = p[:i]
            r = p[i:]

            alphabets = list(string.ascii_lowercase)

            for j in range(0, len(alphabets)):
                c = alphabets[j]
                n = l + c + r
                result.append(n)

        return result

    def generate_letter_removal(p):

        result = []

        for i in range(0, len(p)):
            l = p[:i]
            r = p[i + 1:]
            n = l + r
            result.append(n)

        return result

    def generate_different_letter(p):
        result = []

        for i in range(0, len(p)):
            l = p[:i]
            r = p[i + 1:]

            alphabets = list(string.ascii_lowercase)

            for j in range(0, len(alphabets)):
                c = alphabets[j]
                n = l + c + r
                result.append(n)

        return result

    def generate_split_words(p):

        result = []

        for i in range(1, len(p)):
            l = p[:i]
            r = p[i:]
            result.append((l, r))

        return result

    word = word.lower().strip()

    url = 'https://raw.githubusercontent.com/mohammadfahimtajwar/spelling-correction-suggester/main/dictionary.csv'

    df = pd.read_csv(url)
    words_in_dictionary = df['Word'].tolist()

    def check_both_words_in_dictionary(lst):

        for i in range(0, len(lst)):
            if lst[i][0] in words_in_dictionary and lst[i][1] in words_in_dictionary:
                return lst[i][0] + ' ' + lst[i][1]

    list1 = list(generate_transposes(word))
    list2 = list(generate_missing_letter(word))
    list3 = list(generate_letter_removal(word))
    list4 = list(generate_different_letter(word))
    list5 = list(generate_split_words(word))

    a = [i for i in list1 if i in words_in_dictionary]
    b = [i for i in list2 if i in words_in_dictionary]
    c = [i for i in list3 if i in words_in_dictionary]
    d = [i for i in list4 if i in words_in_dictionary]

    e = [check_both_words_in_dictionary(list5)]
    e = filter(None, e)

    suggested_corrections = list(set().union(a, b, c, d, e))

    if word in words_in_dictionary:
        return True
    else:
        return suggested_corrections
