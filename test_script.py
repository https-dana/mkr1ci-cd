import pytest
from ci_python_project import read_file, count_words, count_sentences

@pytest.fixture
def sample_text(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Привіт, світ! Як справи? Все добре...")
    return file

@pytest.mark.parametrize("text, expected_words, expected_sentences", [
    ("Привіт, світ! Як справи?", 4, 2),
    ("Це тестовий файл. Він містить три речення...", 6, 3),
    ("Один. Два!", 2, 2)
])
def test_count_functions(tmp_path, text, expected_words, expected_sentences):
    file = tmp_path / "test.txt"
    file.write_text(text)
    words = count_words(text)
    sentences = count_sentences(text)
    assert words == expected_words
    assert sentences == expected_sentences