# fdl_gateway.py — интерфейс взаимодействия с FDL-компилятором и склоняющей логикой

from fdl_compiler import FDLCompiler

class FDLGateway:
    """
    Шлюзовая система, подключающая FDL-компилятор к внешнему тексту/потоку.
    Поддерживает анализ слов и фраз через падежную этику и смысловую структуру.
    """

    def __init__(self):
        pass

    def process_word(self, word):
        """
        Обработка одного слова через компилятор.
        """
        compiler = FDLCompiler(word)
        token = compiler.compile_to_token()
        return token

    def process_text(self, text):
        """
        Разбиение текста на слова и построение токенов для каждого через FDLCompiler.
        """
        words = [w.strip('.,!?') for w in text.split() if w.isalpha()]
        result = {}
        for word in words:
            result[word] = self.process_word(word)
        return result

# Пример запуска
if __name__ == "__main__":
    gateway = FDLGateway()
    text = "Logos breathes through the Word of Justice and Compassion"

    processed = gateway.process_text(text)

    from pprint import pprint
    print("\n[Σ-FDL TOKENIZED TEXT]:")
    pprint(processed)
