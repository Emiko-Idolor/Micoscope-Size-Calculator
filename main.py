from core import calculate_real_size
from db.database import save_specimen, init_db


def prompt_float(label: str) -> float:
    while True:
        response = input(f"{label}: ").strip()
        try:
            return float(response)
        except ValueError:
            print("→ Please enter a valid number.")


def prompt_user_inputs():
    name = input("Username: ").strip()
    size = prompt_float("Microscope size (units)")
    zoom = prompt_float("Magnification")
    return name, size, zoom


def notify_success(value: float):
    print(f"\n✔ Real size: {value:.2f} units")
    print("✔ Specimen data saved.")


def run():
    print("\n--- Microscope Size Calculator ---\n")
    try:
        name, size, zoom = prompt_user_inputs()
        actual_size = calculate_real_size(size, zoom)
        save_specimen(name, size, zoom, actual_size)
        notify_success(actual_size)
    except Exception as err:
        print(f"✘ Error: {err}")


if __name__ == "__main__":
    init_db()
    run()
