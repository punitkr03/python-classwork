import string
from collections import Counter

def analyze_text(text):
    total_characters = len(text)
    words = text.split()
    total_words = len(words)
    total_sentences = text.count('.') + text.count('!') + text.count('?')

    average_word_length = sum(len(word) for word in words) / total_words
    average_sentence_length = total_words / total_sentences

    unique_characters = Counter(text)
    unique_words = Counter(words)

    modified_text = text.replace('city', 'town')

    modified_text = modified_text.translate(str.maketrans("", "", string.punctuation))

    return {
        'Total Characters': total_characters,
        'Total Words': total_words,
        'Total Sentences': total_sentences,
        'Average Word Length': average_word_length,
        'Average Sentence Length': average_sentence_length,
        'Unique Characters': dict(unique_characters),
        'Unique Words': dict(unique_words),
        'Modified Text': modified_text
    }

if __name__ == "__main__":
    input_text = """
    This is a sample text document. It contains words, sentences, and punctuation.
    The city is a busy place, but we can change it to a town.
    Let's analyze and modify this text in a step-by-step manner!
    """
    result = analyze_text(input_text)
    for key, value in result.items():
        print(f"{key}: {value}")
