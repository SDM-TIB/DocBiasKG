
## How we aggregated the data files

The data files were created tracing the fake news model and dataset defined in: https://github.com/linqs/chowdhury-cikm20

While we could easily aggregate the data for the actors, getting the [PSL](https://psl.linqs.org/wiki/) model data was a bit more tricky. 

To get more insights into the optimization process of PSL, a customized version needs to be created that exposes more information to the logs. We modified the [ADMMReasoner class](https://github.com/linqs/psl/blob/main/psl-core/src/main/java/org/linqs/psl/reasoner/admm/ADMMReasoner.java) such that it writes detailed info to the logs about atoms, terms and ground rules after each optimization iteration.

Due to size, data files are not included. We included a sample log for the first fold of the Buzzfeed joint credibility model under DataSources/ModelSample > buzzfeed-cs-1-eval.out

