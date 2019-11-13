# Artificial-Intelligence
2019 Spring SNU AI class Project - Hidden Markov Model(HMM) Modeling

Data
-------
Using Python HMM, I perfomed recognition of posture. I used dataset on the UCI machine learning repository. Link is below.</br>
http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones

What is HMM?
------
Hidden Markov Model(HMM) is based on Markov chain. Markov chain is stochastic model satisfying the Markov property which means conditional distribution of future state is dependent only on current state. Then, HMM can predict future state using this powerful property. </br>
In HMM, there are two components: State and Evidence. Evidence means what machine observes. In this project, state in time t is noted <code>X(t)</code> and evidence from time 1 to t is noted <code>e(1:t)</code>.</br>

How does HMM work?
------
There are three steps in HMM.</br></br>

1. Filtering</br>
Filtering is a step to assign current time(t) state using evidence from time 1 to t using below conditional probability.</br>
<pre>P(X(t)|e(1:t))</pre>
Using bayesian rule and Markov property, the conditional probability can be calculated from the previous state.</br>

2. Prediction</br>
Prediction is literally predicting future state using evidence.</br>
<pre>P(X(t')|e(1:t))   (for t' > t)</pre>
In this step, HMM uses most likely path which is called Viterbi algorithm.</br>

3. Smoothing</br>
Now, we need more accruate state prediction </br>
<pre>P(X(k)|e(1:t))   (for 0 <= k < t)</pre></br>
Also, bayesian rule is applied in this step.</br>

Method
---------
I classify posture in two categories. First is static posture which contains sitting, standing, laying.
Second is dynamic posture which contains walking, walking upstair, walking downstair.
In each posture, angular velocity and acceleration is recored with smartphone.
The average was calculated for every 5~7 time because there are some rhythm while perfome activity.
</br>
But there are some problems. Because of long sequence, value get smaller and smaller in Viterbi algorithm.
So, It cannot predict well. To solve thie problem, I little bit changed PythonHMM code using logarithm.

Discussion
-------
It can predict current state(static or dynamic posture). 
However, I didn't use validation set and training set. So, It seems to be well trained.

Limitation of HMM
--------
HMM may have memory loss in temporal sequence because of Markov property. 
If training set is more complicated and dependent on more previous state, It cannot predict next state well.
I think this is why we use machine learning. RNN or LSTM may solve the problem more correctly.
