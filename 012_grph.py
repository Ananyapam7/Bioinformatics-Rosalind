def parse_fasta(fasta):
    results = []
    strings = fasta.strip().split('>')

    for s in strings:
        if len(s):
            parts = s.split()
            k = parts[0]
            v = ''.join(parts[1:])
            results.append((k, v))

    return results


def overlap_graph(fasta, n):
    results = []

    dna = parse_fasta(fasta)

    for k1, v1 in dna:
        for k2, v2 in dna:
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1, k2))

    return results


if __name__ == "__main__":
  large_dataset = open('rosalind_grph.txt').read()

    for edge in overlap_graph(large_dataset, 3):
        print edge[0], edge[1]
