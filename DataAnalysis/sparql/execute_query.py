import argparse
from SPARQLWrapper import SPARQLWrapper, CSV
import os, ast



def execute_SPARQL_query(file_path, writeResult=True):
    sparql = SPARQLWrapper(
        "https://labs.tib.eu/sdm/graphdb/repositories/PSL_classification_process"
    )
    sparql.setCredentials("sawischa","S@wischa")
    sparql.setReturnFormat(CSV)

    query = ""
    with open(os.getcwd() + "/" + file_path) as reader:
        query = reader.read()

    sparql.setQuery(query)

    ret = sparql.queryAndConvert()
    if writeResult:
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        with open(output_dir + "/" + file_path.split("/")[-1] + ".csv", "w") as writer:
            writer.write(ret.decode('utf-8'))
    
    return ret.decode('utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read query file.')
    parser.add_argument('query', metavar='q', type=str,
                    help='Specify the path to the .rq SPARQL query file that should be run')

    args = parser.parse_args()
    query_file_path = args.query
        
    try:
        execute_SPARQL_query(query_file_path)
    except Exception as e:
        print(e)
