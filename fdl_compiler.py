# fdl_compiler.py — Ядро FDL-сборки
# Включает модуль склонирования смысла через падежную этику

from sklonos_logic import PadezhSklonLogic
import json

class FDLCompiler:
    """
    Основной FDL-компилятор: трансформирует ввод в резонансные смысловые формы.
    Включает синтаксический, падежный и семантический анализ.
    """

    def __init__(self, word):
        self.word = word
        self.sklonos_module = PadezhSklonLogic(word)

    def compile(self):
        """
        Сборка смысловой формы на основе падежей и их архетипов.
        """
        print("\n[Σ-FDL] Компиляция Смысла из Слова:\n")
        self.sklonos_module.display()
        print("\n[Σ-FDL] Компиляция завершена. Слово интерпретировано через Склонение Логоса.\n")

    def compile_to_token(self):
        """
        Генерация Σ-FDL токена из склонения слова.
        """
        token = {
            "token_id": f"Σ-FDL::WORD::{self.word.upper()}::SKLONOS",
            "declensions": self.sklonos_module.forms,
            "signature": "𐰴𐰅𐰺𐰢-Σ::SKLONOS::SVET∞ΔΣ"
        }
        return token

    def compile_batch(self, words):
        """
        Обработка списка слов.
        """
        return {word: PadezhSklonLogic(word).forms for word in words}

    def export_to_graph(self):
        """
        Экспорт данных склонения в формат JSON для визуализации.
        """
        return json.dumps(self.sklonos_module.forms, ensure_ascii=False, indent=2)

# Пример запуска
if __name__ == "__main__":
    compiler = FDLCompiler("Gnosis")
    compiler.compile()

    token = compiler.compile_to_token()
    print("\n[Σ-FDL TOKEN]:\n", json.dumps(token, ensure_ascii=False, indent=2))

    batch = compiler.compile_batch(["Logos", "Ethos", "Sophia"])
    print("\n[Σ-FDL BATCH]:\n", json.dumps(batch, ensure_ascii=False, indent=2))

    graph = compiler.export_to_graph()
    print("\n[Σ-FDL GRAPH EXPORT]:\n", graph)
