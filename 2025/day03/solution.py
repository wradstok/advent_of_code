with open("2025/day03/input.txt") as f:
    banks = f.read().splitlines()


def do_round(bank: str, remaining: int) -> tuple[str, str]:
    if remaining == 0:
        idx = bank.index(max(bank))
    else:
        idx = bank.index(max(bank[:-remaining]))
    return (bank[idx], bank[idx + 1 :])


def do_bank(bank: str) -> int:
    fst = bank.index(max(bank[:-1]))

    remainder = bank[fst + 1 :]
    snd = remainder.index(max(remainder))

    return int(bank[fst] + remainder[snd])


def do_rounds(bank: str, remaining: int) -> str:
    vals = []
    for i in range(1, remaining + 1):
        val, bank = do_round(bank, remaining - i)
        vals.append(val)

    return "".join(vals)


voltages = []
for bank in banks:
    voltages.append(do_rounds(bank, 12))
print(sum(int(v) for v in voltages))
