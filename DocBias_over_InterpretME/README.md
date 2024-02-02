[![GitHub](https://img.shields.io/badge/GitHub-SDM--TIB%2FInterpretME-blue?logo=GitHub)](https://github.com/SDM-TIB/InterpretME)

# Documenting Bias over InterpretME
![Design Pattern of Tracing as a Principled Approach](https://raw.githubusercontent.com/SDM-TIB/DocBiasKG/main/images/Fake_News_InterpretME-1.png "Design Pattern of Tracing as a Principled Approach")
Figure depicts a use-case utilizing a principled Hybrid AI technique. 
The InterpretME pipeline preprocesses input datasets, e.g., News collection datasets 
in this use-case and optimizes hyperparameters for the ML classification task of detecting fake news. 
The trained model makes predictions, and LIME provides local explanations for each news. 
In the tracing layer, InterpretME creates the InterpretME KG by tracing metadata and semantically interpreting the traces.

## Getting Started to execute DocBias over InterpretME 

To execute  the implementation of the Doc-Bias approach over a hybrid AI framework, `InterpretME`
where the prediction task is to classify News based on the characteristics of Users and Publishers.

You can run the pipeline with the News collection datasets.

1. start the containers: `docker-compose up -d`
2. run the pipeline: `docker exec -it interpretme bash -c "cd example; python example_pipeline.py <config_json>"` 
where`<config_json>` is one of `example_buzz.json` and `example_politi.json`.

After running the pipeline, the produced plots can be found in `./interpretme/output/`.
Once the data is uploaded into the SPARQL endpoint. 
In the folder `queries/news` you can find the queries populated for the News collection dataset.
The queries can be executed for answering the following questions:

1. Counting news with prediction probability for `Class:Real` in BuzzFeed dataset.
2. Counting news with prediction probability for `Class:Fake` in BuzzFeed dataset.
3. Counting news with prediction probability for `Class:Real` in PolitiFact dataset.
4. Counting news with prediction probability for `Class:Fake` in PolitiFact dataset.
5. Computing Average probability, MAX probability and MIN probability.




For more information about InterpretME, check its [GitHub repository](https://github.com/SDM-TIB/InterpretME).
