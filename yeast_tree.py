# Build a yeast family tree from a .csv file
# CSV table must be in chronological order
# Set ID of record of interest to progenitor_id to build tree of progeny
# Requires 'treelib' library

from treelib import Node, Tree
import csv

# yeast naming function
def get_yeast_name(yeast_record):
  return yeast_record['Gen'] + ": " + yeast_record['Yeast_Name']

# set ID as string for progenitor yeast record of interest
progenitor_id = '1072'

# open file and save to yeast_records list
yeast_records = {}
with open("yeast_table.csv") as yeast_table_file:
  yeast_csv = csv.DictReader(yeast_table_file)
  for row in yeast_csv:
    yeast_records[row['ID']]= row

# exit program if progenitor_id is not in the csv file
if not progenitor_id in yeast_records:
  raise SystemExit("Progenitor record ID not found.")

# Build yeast_tree
yeast_tree = Tree()

# Create first node:
yeast_name = get_yeast_name(yeast_records[progenitor_id])
yeast_tree.create_node(tag=yeast_name, identifier=progenitor_id)

# Iterate through records and add if Parent_ID is in the tree
for yeast_id, record in yeast_records.items():
  yeast_name = get_yeast_name(record)
  parent_id = record['Parent_ID']
  if parent_id in yeast_tree.nodes:
    yeast_tree.create_node(tag=yeast_name, identifier=yeast_id, parent=parent_id)

yeast_tree.show()