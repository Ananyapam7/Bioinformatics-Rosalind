def parse_fasta(s):
    results = {}
    strings = s.strip().split('>')

    for s in strings:
        if len(s) == 0:
            continue

        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        results[label] = bases
        
    return results


def gc_content(s):
    n = len(s)
    m = 0

    for c in s:
        if c == 'G' or c == 'C':
            m = m+1

    return 100 * (float(m) / n)


if __name__ == "__main__":

    large_dataset = open('rosalind_gc.txt').read()

    results = parse_fasta(large_dataset)
    results = dict([(k, gc_content(v)) for k, v in results.iteritems()])

    highest_k = None
    highest_v = 0

    for k, v in results.iteritems():
        if v > highest_v:
            highest_k = k
            highest_v = v

    print highest_k
    print '%f%%' % highest_v
