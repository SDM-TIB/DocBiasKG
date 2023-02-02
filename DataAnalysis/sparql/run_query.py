import argparse
from SPARQLWrapper import SPARQLWrapper, CSV
import os, ast

parser = argparse.ArgumentParser(description='Read query file.')
parser.add_argument('query', metavar='q', type=str,
                    help='Specify the path to the .rq SPARQL query file that should be run')


args = parser.parse_args()
query_file_path = args.query
print(query_file_path)

sparql = SPARQLWrapper(
    "https://labs.tib.eu/sdm/nobias1/sparql"
)
sparql.setReturnFormat(CSV)

query = ""
with open(os.getcwd() + "/" + query_file_path) as reader:
    query = reader.read()

sparql.setQuery(query)

try:
    ret = sparql.queryAndConvert()
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_dir + "/" + query_file_path.split("/")[-1] + ".csv", "w") as writer:
        writer.write(ret.decode('utf-8'))
except Exception as e:
    print(e)
