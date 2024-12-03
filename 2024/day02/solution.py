with open("2024/day02/input.txt") as f:
    lines = f.readlines()
    records = []
    for line in lines:
        records.append([int(x) for x in line.split()])


def check_record(record: list[int]) -> bool:
    if not (sorted(record) == record or sorted(record, reverse=True) == record):
        return False

    for a, b in zip(record, record[1:]):
        diff = abs(a - b)
        if 1 <= diff <= 3:
            continue
        else:
            return False

    return True


safe = 0
for record in records:
    valid = check_record(record)
    if valid:
        safe += 1

print(safe)


safe = 0
for record in records:
    valid = check_record(record)
    if valid:
        safe += 1
    else:
        for idx in range(len(record)):
            record_copy = record.copy()
            record_copy.pop(idx)
            valid = check_record(record_copy)
            if valid:
                safe += 1
                break

print(safe)
