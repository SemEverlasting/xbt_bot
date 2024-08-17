from spellchecker import SpellChecker
# исправление орфографических ошибок
# Создание объекта SpellChecker для русского языка
spell = SpellChecker(language='ru')


def correct_spelling(text):
    # Разделяем текст на слова
    words = text.split()

    # Исправляем каждое слово
    corrected_words = []
    for word in words:
        # Получаем кандидатов на исправление
        candidates = spell.candidates(word)
        # Выбираем первое исправление из кандидатов
        corrected_word = next(iter(candidates), word)
        corrected_words.append(corrected_word)

    # Объединяем исправленные слова обратно в строку
    return ' '.join(corrected_words)
