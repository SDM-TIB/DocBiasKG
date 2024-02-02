import os
import sys

from InterpretME import pipeline, plots

path_config = str(sys.argv[1])
if not os.path.isfile(path_config):
    print('No valid configuration path given!')

results = pipeline(
    path_config=path_config,
    lime_results='./interpretme/files/LIME',
    server_url='http://localhost:8891/',
    username='dba',
    password='dba'
)

plots.feature_importance(results=results, path='interpretme/output')
plots.decision_trees(results=results, path='interpretme/output')
