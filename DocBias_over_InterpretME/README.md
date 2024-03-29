[![GitHub](https://img.shields.io/badge/GitHub-SDM--TIB%2FInterpretME-blue?logo=GitHub)](https://github.com/SDM-TIB/InterpretME)

# Documenting Bias over InterpretME
![Design Pattern of Tracing as a Principled Approach](https://raw.githubusercontent.com/SDM-TIB/DocBiasKG/main/images/Fake_News_InterpretME-1.png "Design Pattern of Tracing as a Principled Approach")
The figure represents a use-case involving a principled Hybrid AI methodology. ``InterpretME`` is a principled hybrid AI framework used to trace bias involved in the predictive pipeline. In the training layer, the pipeline accepts raw data on News, Users, and Publishers from two different benchmark datasets: Dataset 1: BuzzFeed News and Dataset 2: PolitiFact. Further hyperparameter optimization is carried out to train the model on the best-suited parameters obtained from AutoML. In this scenario, Random Forest classifier model is used to select the top-ranking features for training the decision tree classifier. In addition, `LIME` generates local explanations for all instances in the news dataset. Simultaneously, all traced metadata obtained during pipeline execution is used semantically to generate ``InterpretME KG``.

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
