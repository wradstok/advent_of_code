from copy import deepcopy

with open("2023/day13/input.txt") as f:
    lines = f.read().splitlines()
    mirror: list[str] = []
    mirrors: list[list[str]] = []
    for line in lines:
        if line == "":
            mirrors.append(mirror)
            mirror = []
        else:
            mirror.append(line)
    mirrors.append(mirror)


def check_mirror(hash_list: list[int]):
    # Find all equal adjacent hashes
    starts = []
    for i in range(len(hash_list) - 1):
        if hash_list[i] == hash_list[i + 1]:
            starts.append(i)
    found = []
    for i in starts:
        for j in range(0, min(i + 1, len(hash_list) - i - 1)):
            if hash_list[i - j] != hash_list[i + 1 + j]:
                break
        else:
            found.append(i + 1)
    return found


def get_scores(v_hashes, h_hashes):
    return [100 * x for x in check_mirror(v_hashes)] + [x for x in check_mirror(h_hashes)]


def gen_hashes(mirror):
    v_hashes = [hash(line) for line in mirror]
    h_hashes = [hash("".join([line[i] for line in mirror])) for i in range(len(mirror[0]))]
    return v_hashes, h_hashes


res = 0
for mirror in mirrors:
    v_hashes = [hash(line) for line in mirror]
    h_hashes = [hash("".join([line[i] for line in mirror])) for i in range(len(mirror[0]))]

    res += sum([100 * x for x in check_mirror(v_hashes)]) + sum(check_mirror(h_hashes))
print(res)


res = 0
for mirror in mirrors:
    v_hashes, h_hashes = gen_hashes(mirror)
    orig_scores = get_scores(v_hashes, h_hashes)

    found = False
    for y in range(len(mirror)):
        if found:
            break

        for x in range(len(mirror[0])):
            smudged = deepcopy(mirror)
            smudged[y] = smudged[y][:x] + ("#" if smudged[y][x] == "." else ".") + smudged[y][x + 1 :]

            v_hashes, h_hashes = gen_hashes(smudged)
            new_scores = get_scores(v_hashes, h_hashes)

            valid = [score for score in new_scores if score not in orig_scores]
            if valid:
                res += sum(valid)
                found = True
                break

print(res)
