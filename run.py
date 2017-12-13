import csv
import json

if __name__ == '__main__':
	data = {}
	data['edges'] = []
	data['nodes'] = []

	nodes_f = open('Locus_aerospace_nodes.csv', 'rU')
	csv_f = csv.reader(nodes_f)
	next(csv_f, None) # skip title
	# add node to nodes
	for row in csv_f:
		group = row[2].replace('.', '_')[:3]
		data['nodes'].append({'id': row[0], 'label': row[1], 'activity_group': group, 'activity': row[2], 'object': row[3] })

	edges_f = open('Locus_aerospace_edges.csv','rU')
	csv_f = csv.reader(edges_f)
	next(csv_f, None) # skip title
	for row in csv_f:
		data['edges'].append({'source': row[0], 'target': row[1]})


	with open('graph.json', 'w') as outfile:
		json.dump(data, outfile)