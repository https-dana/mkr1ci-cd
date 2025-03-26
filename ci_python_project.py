import re

def count_sentences(text):
    """Рахує кількість речень у тексті."""
    sentence_endings = re.compile(r'[.!?]+')
    sentences = sentence_endings.split(text)
    return sum(1 for s in sentences if s.strip())


def read_file(file_path):
    """Зчитує текстовий файл і повертає його вміст."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def count_words(text):
    """Рахує кількість слів у тексті."""
    word_delimiters = re.compile(r'[,\\s;:-]+')
    words = word_delimiters.split(text)
    return sum(1 for w in words if w.strip())

if __name__ == "__main__":
    file_path = "sample.txt"  
    text = read_file(file_path)
    words = count_words(text)
    sentences = count_sentences(text)
    print(f"Words: {words}, Sentences: {sentences}")
