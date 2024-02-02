[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Doc-Bias KG

![Design Pattern of Tracing as an Integrated Approach](https://raw.githubusercontent.com/SDM-TIB/DocBiasKG/main/images/DocBias.png "Design Pattern of Tracing as a Principled Approach")

A hybrid AI system capable of identifying bias patterns in datasets used by predictive AI models. The proposed system captures knowledge about dataset characteristics and represents it as factual statements in a knowledge graph.

The proposed hybrid AI system is used to trace the PSL implementation of the AI model for fake news detection (https://doi.org/10.1145/3340531.3412066). 

This repository contains following contents: 
1. `DataSources:` The data files generated to trace the fake news model and dataset defined in: https://github.com/linqs/chowdhury-cikm20.
2. `Doc-BiasKG:` schema, mapping rules, resulting experiments.
3. Folder `sparql_queries` contains all the necessary bias analysis performed over the generated Doc-Bias KG.
4. `DocBias_over_InterpretME:` Doc-Bias analysis applied over a principled approach, InterpretME. The necessary instructions for execution of InterpretME pipeline and running sparql queries over the InterpretME KG is available in this folder.

### Getting Started
Clone the repository
```bash
git clone git@github.com:SDM-TIB/DocBiasKG.git
```
### Running Doc Bias
Install necessary dependencies for `Doc-Bias` approach, create a virtual environment and run the following command:
```python
pip install -r requirements.txt
```

**References**

[1] Marco Ribeiro, Sameer Singh, and Carlos Guestrin. "Why Should I Trust You?": Explaining the Predictions of Any Classifier. In: *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '16)*. ACM. 2016. DOI: [10.1145/2939672.2939778](https://doi.org/10.1145/2939672.2939778)

[2] Yashrajsinh Chudasama, Disha Purohit, Philipp D. Rohde, Julian Gercke, Maria-Esther Vidal. "InterpretME: A Tool for Interpretations of Machine Learning Models Over Knowledge Graphs" *In
Semantic Web Journal, Special Issue on Tools & Systems*. DOI: [10.3233/SW-233511](https://content.iospress.com/articles/semantic-web/sw233511)
