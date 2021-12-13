import re
import string


def most_common_words(file_path: str, top_words: int) -> list:
    """
    Function which returns most common words in the file.
    @param file_path: file to be read
    @param top_words: number of top words to be returned
    @return: list of top words
    """
    if not isinstance(file_path, str) or not isinstance(top_words, int):
        raise TypeError
    if top_words <= 0:
        raise ValueError
    with open(file_path) as file:
        words = []
        for line in file:
            words.extend(re.split(fr'[\s]|[{string.punctuation}]', line))
    words_statistic = list(set(filter(lambda x: x[0] != '', list(map(lambda x: (x, words.count(x)), words)))))
    words_statistic.sort(key=lambda x: x[1], reverse=True)
    if top_words < len(words_statistic):
        return list(map(lambda x: x[0], words_statistic[:top_words]))
    return list(map(lambda x: x[0], words_statistic))


print(most_common_words('words.txt', 3))
