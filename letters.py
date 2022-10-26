def clone_letters(line: str):
    line = line.lower()
    uniquq_let = set(line)
    count = 0
    for sym in uniquq_let:
        if line.count(sym) > 1:
            count += 1
    return count

def count_duplicates(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])
