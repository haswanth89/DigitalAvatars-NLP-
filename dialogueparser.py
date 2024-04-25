import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import string
import matplotlib.pyplot as plt

# Download necessary NLTK resources
nltk.download('punkt')

def lexical_diversity(text):
    words = word_tokenize(text.lower())
    unique_words = len(set(words))
    total_words = len(words)
    return unique_words, total_words

def average_sentence_length(text):
    sentences = sent_tokenize(text)
    sentence_lengths = [len(word_tokenize(sentence)) for sentence in sentences]
    return sentence_lengths

# def word_frequency(text):
#     # Remove punctuation marks
#     text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
#     words = word_tokenize(text_without_punctuation.lower())
#     word_counts = Counter(words)
#     print(word_counts)
#     return word_counts
def word_frequency(text):
    # Remove specific characters
    text_without_chars = text.replace('’', '').replace('—', '').replace('”','')
    # Remove punctuation marks
    text_without_punctuation = text_without_chars.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text_without_punctuation.lower())
    word_counts = Counter(words)
    return word_counts
def analyze_dialogues(dialogues):
    harry_dialogues = []
    all_dialogues = []

    for dialogue_list in dialogues:
        for dialogue in dialogue_list:
            sender = dialogue["sender"]
            text = dialogue["text"]
            all_dialogues.append(text)
            if sender == "Harry":
                harry_dialogues.append(text)

    harry_text = " ".join(harry_dialogues)
    all_text = " ".join(all_dialogues)

    # Analysis for Harry's dialogues
    print("Analysis for Harry's dialogues:")
    harry_unique_words, harry_total_words = lexical_diversity(harry_text)
    print(f"Harry Unique words: {harry_unique_words}")
    print(f"Harry Total words: {harry_total_words}")
    harry_sentence_lengths = average_sentence_length(harry_text)
    harry_word_freq = word_frequency(harry_text)
    print(harry_word_freq)

    # Analysis for all dialogues
    print("\nAnalysis for all dialogues:")
    all_unique_words, all_total_words = lexical_diversity(all_text)
    print(f"All Unique words: {all_unique_words}")
    print(f"All Total words: {all_total_words}")
    all_sentence_lengths = average_sentence_length(all_text)
    all_word_freq = word_frequency(all_text)

    # Create subplots
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    # Visualize lexical diversity
    axs[0, 0].bar(["Unique Words", "Total Words"], [harry_unique_words, harry_total_words], color=['#97a6c4', '#384860'])
    axs[0, 0].set_title("Harry potter dialogues: Lexical Diversity")
    axs[0, 0].set_ylabel("Count")

    axs[1, 0].bar(["Unique Words", "Total Words"], [all_unique_words, all_total_words], color=['#97a6c4', '#384860'])
    axs[1, 0].set_title("All characters dialogues: Lexical Diversity")
    axs[1, 0].set_ylabel("Count")

    # Visualize sentence length distribution
    axs[0, 1].hist(harry_sentence_lengths, bins=20, color='#97a6c4')
    axs[0, 1].set_title("Harry potter dialogues : Sentence Length Distribution")
    axs[0, 1].set_xlabel("Number of Words")
    axs[0, 1].set_ylabel("Frequency")

    axs[1, 1].hist(all_sentence_lengths, bins=20, color='#97a6c4')
    axs[1, 1].set_title("All characters dialogues: Sentence Length Distribution")
    axs[1, 1].set_xlabel("Number of Words")
    axs[1, 1].set_ylabel("Frequency")

    # Visualize word frequency
    harry_words, harry_counts = zip(*harry_word_freq.most_common(25))
    all_words, all_counts = zip(*all_word_freq.most_common(25))

    axs[0, 2].bar(harry_words, harry_counts, color='#384860')
    axs[0, 2].set_title("Harry potter dialogues: Word Frequency")
    axs[0, 2].set_xlabel("Words")
    axs[0, 2].set_ylabel("Frequency")
    axs[0, 2].tick_params(axis='x', rotation=45)

    axs[1, 2].bar(all_words, all_counts, color='#384860')
    axs[1, 2].set_title("All characters dialogues: Word Frequency")
    axs[1, 2].set_xlabel("Words")
    axs[1, 2].set_ylabel("Frequency")
    axs[1, 2].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

def main():
    # Read JSON file
    with open('dialogue.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract dialogues
    dialogues = [dialogue["dialog"] for dialogue in data]

    # Analyze dialogues
    analyze_dialogues(dialogues)

if __name__ == "__main__":
    main()
