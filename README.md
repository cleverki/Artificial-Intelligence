# Artificial-Intelligence
2019 Spring SNU AI class Project - Hidden Markov Model(HMM) Modeling

Data
-------
Using Python HMM, I perfomed recognition of posture. I used dataset on the UCI machine learning repository. Link is below.</br>
http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones

Method
------
Hidden Markov Model(HMM) is based on Markov chain. Markov chain is stochastic model satisfying the Markov property which means conditional distribution of future state is dependent only on current state. Then, HMM can predict future state using this powerful property. </br>
In HMM, there are two components: State and Evidence. Evidence means what machine observes. In this project, state in time t is noted X(t) and evidence from time 1 to t is noted e(1:t).</br>
Also, there are three steps in HMM.</br>

1. Filtering
