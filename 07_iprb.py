from scipy.misc import comb

with open('data/rosalind_iprb.txt') as input_data:
	hom, het, rec = map(int, input_data.read().split())

# The total number different children that can be produced by two organisms. Factor of 4 because Punit squares yield 4 potential children. 
total = 4*comb(hom+het+rec, 2)

# The number of potential children who display the recessive gene.
totalrec = 4*comb(rec,2) + 2*rec*het + 1*comb(het,2)

# Using the complementary event to find the probability of a dominant gene expression.
print 1 - totalrec/total

with open('output/007_IRPB.txt', 'w') as output_data:
	output_data.write(str(1 - totalrec/total))
