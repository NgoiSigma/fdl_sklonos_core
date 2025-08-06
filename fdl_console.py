# fdl_console.py — Консольный интерфейс Σ-FDL системы падежного смысла

from fdl_compiler import FDLCompiler
from fdl_gateway import FDLGateway
from fdl_translator import FDLTranslator
from fdl_ontology_map import FDLOntologyMap
from sklon_graph import SklonGraphVisualizer


def main():
    print("\nΣ-FDL Консоль :: Склоняющий Логос")
    print("Выберите режим:")
    print("1 — Склонение слова (токен)")
    print("2 — Обработка текста (пакетно)")
    print("3 — Визуализация графа склонения")
    print("4 — Глобальная карта падежей мира")
    print("5 — Трансляция текста в FDL-вектор")
    print("0 — Выход")

    choice = input("→ Введите номер: ").strip()

    if choice == "1":
        word = input("Введите слово: ").strip()
        compiler = FDLCompiler(word)
        compiler.compile()

    elif choice == "2":
        text = input("Введите текст: ").strip()
        gateway = FDLGateway()
        result = gateway.process_text(text)
        from pprint import pprint
        pprint(result)

    elif choice == "3":
        word = input("Введите слово для визуализации: ").strip()
        vis = SklonGraphVisualizer(word)
        vis.build_graph()
        vis.visualize()

    elif choice == "4":
        ontology = FDLOntologyMap()
        ontology.display_map()

    elif choice == "5":
        text = input("Введите текст для трансляции: ").strip()
        translator = FDLTranslator()
        result = translator.translate_text(text)
        for word, declensions in result.items():
            print(f"\n🔤 {word.upper()}:")
            for case, data in declensions.items():
                print(f"  {case.title()}: {data['form']} → {data['role']}")

    elif choice == "0":
        print("До встречи в Слове.")
        return

    else:
        print("Неверный ввод. Попробуйте снова.")

    print("\n--- Завершено ---\n")
    main()


if __name__ == "__main__":
    main()