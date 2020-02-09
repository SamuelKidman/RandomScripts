from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist
import pandas as pd

input_table = pd.read_csv("Haplotype_definitions.csv", index_col=0)
input_table2 = input_table

#print(input_table, '\n')
#print(input_table2, '\n')


pairwise = pd.DataFrame(squareform(pdist(input_table)), columns = input_table.index, index = input_table.index)

#print(pairwise, '\n')


for row1 in range(0, len(input_table.index)):
	row1_name = input_table.iloc[[row1]].index.tolist()
	#print(row1_name[0])

	for row2 in range(0, len(input_table2.index)):
		row2_name = input_table2.iloc[[row2]].index.tolist()
		#print(row2_name[0])
		diff1 = 0

		for col1 in range(0, len(input_table.columns)):
			if input_table2.iloc[row2, col1] == input_table.iloc[row1, col1]:
				diff1 = diff1
			else:
				diff1 += 1

		pairwise.loc[row1_name, row2_name] = diff1

pairwise.to_csv("out_diff.csv")
