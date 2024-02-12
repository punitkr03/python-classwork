import string

text = "This is a sample text. You can replace this with your own data."

def tokenized(text):
    words = text.split(" ")
    return words

def strip(words):
    stripped = [token.strip(string.punctuation).lower() for token in words]
    return stripped

def get_unique(words):
    unique_words = list(set(words))
    return unique_words

def build_distance_matrix(words):
    dist_matrix = []
    num_words = len(words)
    for i in range(num_words):
        dist_matrix.append([0]*num_words)

    return dist_matrix

def build_cooccurence_matrix(text_tokens, dist_matrix):
    for i in range(len(text_tokens)):
        for j in range(len(text_tokens)):
            if i != j:
                dist_matrix[i][j] = text.count(text_tokens[i] + " " + text_tokens[j])

    return dist_matrix

def print_suggestion(user_input, text_tokens, dist_matrix):
    tokenized_words = tokenized(text)
    stripped_words = strip(tokenized_words)
    unique_words = get_unique(stripped_words)
    if user_input in unique_words:
        index_of_user_input = unique_words.index(user_input)
        max_value = max(dist_matrix[index_of_user_input])
        max_index = dist_matrix[index_of_user_input].index(max_value)
        print("Top suggestion: ", unique_words[max_index])

user_input = input("Enter a word: ")
tokenized_words = tokenized(text)
stripped_words = strip(tokenized_words)
unique_words = get_unique(stripped_words)
dist_matrix = build_distance_matrix(unique_words)
cooccurence_matrix = build_cooccurence_matrix(unique_words, dist_matrix)
print_suggestion(user_input, unique_words, dist_matrix)
