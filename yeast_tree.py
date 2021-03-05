# Build a yeast family tree from a .csv file
# CSV table must be in chronological order
# Set ID of record of interest to progenitor_id to build tree of progeny
# Requires 'treelib' library

from treelib import Node, Tree
import csv

# set ID for progenitor yeast record of interest
progenitor_id = 562

# open file and save to yeast_records list
yeast_records = {}
with open("yeast_table.csv") as yeast_table_file:
  yeast_csv = csv.DictReader(yeast_table_file)
  for row in yeast_csv:
    yeast_records[int(row['ID'])]= row

# exit program if progenitor_id is not in the csv file
if not progenitor_id in yeast_records:
  raise SystemExit("Progenitor record ID not found.")

yeast_tree = Tree()

# Create first node:
first_record = yeast_records[progenitor_id]
yeast_id = first_record['ID']
yeast_name = first_record['Yeast_Name'] + " (" + str(first_record['Gen']) + ")"
yeast_tree.create_node(tag=yeast_name, identifier=yeast_id)

# Iterate through records and add if Parent_ID is in the tree
for record in yeast_records.values():
  yeast_id = record['ID']
  yeast_name = record['Yeast_Name'] + " (" + str(record['Gen']) + ")"
  parent_id = record['Parent_ID']
  if parent_id in yeast_tree.nodes:
    yeast_tree.create_node(tag=yeast_name, identifier=yeast_id, parent=parent_id)

yeast_tree.show()