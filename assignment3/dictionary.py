import time


def collect_items(student_input):
    values = []
    while True:
        values.append(input(f"Enter {student_input}: "))
        if input(f"Add another {student_input}? (yes/no): ").strip().lower() != 'yes':
            break
    return values


def main():
    print("Collecting names")
    names = collect_items('name')

    print("Collecting tech tracks")
    tech_tracks = collect_items('tech track')

    if len(names) != len(tech_tracks):
        print("Lengths don't match")
        return

    print("Lengths match. Proceeding")
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(1)
    print()

    result = dict(zip(names, tech_tracks))
    print(result)


if __name__ == '__main__':
    main()
