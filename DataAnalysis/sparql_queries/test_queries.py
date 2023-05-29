import unittest
import os
from execute_query import execute_SPARQL_query
import os
from glob import glob

class TestQueries(unittest.TestCase):

    def getSPARQLQueryPaths(self):
        paths = [y for x in os.walk("DataAnalysis/sparql_queries/queries") for y in glob(os.path.join(x[0], '*.rq'))]
        return paths

    def test_all(self):
        paths = self.getSPARQLQueryPaths()
        for i, path in enumerate(paths):
            try:
                result = execute_SPARQL_query(file_path=path)
                print("Passed ({}/{}) - {}".format(i+1, len(paths), path))
            except Exception as e:
                self.fail(msg="Failed query at {} with error message {}".format(path, e))
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()