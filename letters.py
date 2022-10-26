import time
def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        first = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        second = time.time() - initial_time
        print(f1.name if first < second else f2.name)
    return f

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

funcion = worktime(count_duplicates, clone_letters)
funcion('aaaBBnn')