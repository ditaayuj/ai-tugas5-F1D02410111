import json
from pathlib import Path

def load_knowledge_base():
    file_path = Path(__file__).with_name("kb_laptop.json")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def collect_facts(knowledge_base):
    facts = set()

    print("=" * 60)
    print("SISTEM PAKAR IDENTIFIKASI MASALAH PENGISIAN DAYA LAPTOP")
    print("=" * 60)
    print("Jawab pertanyaan dengan Y (Ya) atau T (Tidak).\n")

    for fact_id, detail in knowledge_base["facts"].items():

        if detail["type"] != "input":
            continue

        while True:
            answer = input(detail["question"] + " (Y/T): ").strip().lower()

            if answer in ["y", "ya"]:
                facts.add(fact_id)
                break
            elif answer in ["t", "tidak"]:
                break
            else:
                print("Masukkan Y atau T.")

        print()

    return facts

def forward_chaining(knowledge_base, initial_facts):
    facts = set(initial_facts)
    fired_rules = []
    used_rule_ids = set()
    conclusions = set()

    while True:
        new_fact_found = False

        for rule in knowledge_base["rules"]:

            if rule["id"] in used_rule_ids:
                continue

            if all(condition in facts for condition in rule["if"]):
                used_rule_ids.add(rule["id"])
                fired_rules.append(rule)

                result = rule["then"]

                if result not in facts:
                    facts.add(result)
                    new_fact_found = True

                if result in knowledge_base["conclusions"]:
                    conclusions.add(result)

        if not new_fact_found:
            break

    return conclusions, fired_rules

def display_results(knowledge_base, conclusions, fired_rules):
    print("\n" + "=" * 60)
    print("HASIL IDENTIFIKASI")
    print("=" * 60)

    if conclusions:
        for number, conclusion_id in enumerate(sorted(conclusions), start=1):
            print(f"\n{number}. {knowledge_base['conclusions'][conclusion_id]}")
    else:
        print("\nSistem belum dapat menentukan kemungkinan penyebab.")
        print("Tidak ada aturan yang terpenuhi.")

    print("\n" + "-" * 60)
    print("ATURAN YANG DIGUNAKAN")
    print("-" * 60)

    if fired_rules:
        for rule in fired_rules:
            print(f"\n{rule['id']}")
            print("IF   :", " DAN ".join(rule["if"]))
            print("THEN :", rule["then"])
            print("Sumber:", ", ".join(rule["source"]))
    else:
        print("Tidak ada aturan yang dijalankan.")

    print("\nCatatan: Hasil merupakan dugaan awal, bukan diagnosis pasti.")

def main():
    knowledge_base = load_knowledge_base()

    initial_facts = collect_facts(knowledge_base)

    conclusions, fired_rules = forward_chaining(
        knowledge_base,
        initial_facts
    )

    display_results(knowledge_base, conclusions, fired_rules)

if __name__ == "__main__":
    main()