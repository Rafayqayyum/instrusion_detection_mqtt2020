# Intrusion Detection on MQTT-IOT-IDS2020 dataset

## About Notebook

The jupyter notebook contains detailed process of different models(logistic regression, K nearest neighbors, Decision trees, random forests, naive Bayes and support vector machines) compared on MQTT-IOT-IDS2020 dataset. The results are available in CSV files for the comparison.
Decision trees and Random Forests clearly dominate in the results but random forest performs better than Decision trees even when considering time constraint.
Random forest can be parallelized which reduces its training time to roughly the same as Decision trees. 


There is a script uploaded along with the notebook. The sample csv is provided with the script. Refer to script for help on how to run it.
**Extract the zip file in the resources folder for the script to work. Github doesn't allow files larger than 100mbs so it had to be compressed**

## About Dataset

The dataset was obtained from [IEEE dataport](https://ieee-dataport.org/open-access/mqtt-iot-ids2020-mqtt-internet-things-intrusion-detection-dataset). Since the dataset
is large, it wasn't uploaded here.
Dataset is divided into 3 different types. There are 5 different classes and each class has its own csv file except normal. This makes it about 12 different files.
They were all read seperately. They were combined and shuffled later.
To handle the class imbalance and loading data into RAM problem, Only a percentage of random samples were read.

**Types:**
1. Packetflow
2. Bi-flow
3. Uni-flow

**Classes:**
1. bruteforce
2. normal
3. scan_A     
4. scan_SU
5. sparta

## Libraries used

1. Sklearn    
2. Pandas  
3. Category Encoders
4. Random     
5. Numpy    
6. Matplotlib
7. Zipfile
