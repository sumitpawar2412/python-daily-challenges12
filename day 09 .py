import copy
import random

ROLL_NUM = 569


def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10},
            "supplier": {"name": "TechFlow", "rating": 4.7},
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25},
            "supplier": {"name": "MobileLab", "rating": 4.4},
        },
        {
            "item": "Headset",
            "details": {"price": 3200, "stock": 40},
            "supplier": {"name": "SoundNest", "rating": 4.2},
        },
    ]


def apply_discount(data):
    size = len(data)
    target = ROLL_NUM % size
    for idx, entry in enumerate(data):
        if idx == target:
            entry["details"]["price"] = int(entry["details"]["price"] * 0.9)
            entry["details"]["stock"] = max(0, entry["details"]["stock"] - 3)
            entry["supplier"]["rating"] = round(entry["supplier"]["rating"] - 0.1, 1)
    return data


def compare_data(before, after):
    changed = 0
    same = 0
    notes = []

    for a, b in zip(before, after):
        if a == b:
            same += 1
        else:
            changed += 1
            notes.append(
                f"Item '{a['item']}' changed: before {a['details']} / {a['supplier']} -> after {b['details']} / {b['supplier']}"
            )
    return changed, same, notes


def show_inventory(label, records):
    print(f"\n{label}")
    for rec in records:
        print(f" - {rec['item']}: price={rec['details']['price']}, stock={rec['details']['stock']}, supplier={rec['supplier']}")


def main():
    inv = create_inventory()
    baseline = copy.deepcopy(inv)

    shallow = copy.copy(inv)
    deep = copy.deepcopy(inv)

    apply_discount(shallow)
    apply_discount(deep)

    changed_sh, same_sh, notes_sh = compare_data(baseline, shallow)
    changed_dp, same_dp, notes_dp = compare_data(baseline, deep)

    show_inventory("Original inventory before mutation:", baseline)
    show_inventory("Original inventory after shallow-copy mutation:", inv)
    show_inventory("Deep copy result:", deep)

    print("\n--- Analysis ---")
    print("Shallow copy changed original data because nested dictionaries are shared by reference.")
    print("Deep copy stayed independent because every nested dictionary was cloned separately.")
    print("Example: the Laptop item details were modified in the shallow copy and the original list also changed.")

    print("\nDifferences detected for shallow copy vs original baseline:")
    for line in notes_sh:
        print(" ", line)

    print("\nDifferences detected for deep copy vs original baseline:")
    for line in notes_dp:
        print(" ", line)

    print("\nSummary tuple for shallow copy comparison:")
    print((changed_sh, same_sh))
    print("Summary tuple for deep copy comparison:")
    print((changed_dp, same_dp))

    print("\nAP ID: AP24110011569")


if __name__ == "__main__":
    main()
