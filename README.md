# Network Traffic Detector using Machine Learning

This project aims to develop a machine learning model for detecting malicious network traffic using the **CICIDS2017** dataset. The model is trained to detect various types of attacks, such as DDoS, DoS, Port Scan, and others, with high accuracy.

## Project Overview

The project involves preprocessing network traffic data and training a **Random Forest** classifier to detect anomalies in network traffic. The model has been trained and evaluated on multiple attack types and benign traffic.

### Key Features:
- Data preprocessing: handling missing and infinite values.
- Classification model using **Random Forest**.
- Performance evaluation with metrics such as accuracy, precision, recall, and f1-score.
- Support for multiple attack types.

## Results

The model achieved an accuracy of **99.88%** on the test set, with strong performance in detecting attacks such as **DDoS** and **DoS Hulk**.

| Metric    | Value  |
|-----------|--------|
| Accuracy  | 99.88% |
| Precision | 99.9%  |
| Recall    | 99.9%  |
| f1-Score  | 99.9%  |

## Dataset

The dataset used is **CICIDS2017**, a network traffic dataset containing both benign and malicious traffic.

- **Dataset link**: [CICIDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)

## Project Structure

