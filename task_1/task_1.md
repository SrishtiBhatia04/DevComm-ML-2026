# Task 1 - Spaceship Titanic Classification

# Overview
This task focuses on solving a binary classification problem using the Spaceship Titanic dataset. The objective is to predict whether a passenger was transported to another dimension based on the information available about them. The target variable for this task is:- `Transported`. It indicates whether a passenger was transported (True/False). The overall goal was to build a reliable machine learning model that can accurately classify passengers while ensuring proper validation and generalization.

The following file has been included for this task:

# 1. task-1-notebook.ipynb
This notebook contains the complete workflow used to develop the final model.
It includes:
- Data exploration and understanding
- Data preprocessing and cleaning
- Handling of missing values
- Feature transformations
- Model training process
- Model evaluation and results

The notebook is structured to clearly show how the raw dataset was processed and how the final model was obtained.

# Dataset
Spaceship Titanic (Kaggle)

The dataset consists of passenger-related features, including a mix of categorical and numerical variables. It also contains missing values and certain grouped relationships between passengers, which were important considerations during preprocessing. These features were used to predict the `Transported` outcome.

# Approach
The approach taken in this task involved multiple stages, starting from understanding the dataset to building the final model.
Initial exploration was performed to understand the structure and distribution of the data. Based on these observations, the dataset was cleaned and prepared by handling missing values and ensuring consistency across features.
Feature transformations were then applied to better represent the underlying patterns in the data. These transformations helped improve the model’s ability to learn meaningful relationships.
Different modeling approaches were considered, and care was taken to ensure that the evaluation process was reliable. A group-based validation strategy was used to prevent data leakage and ensure that related samples were not split across training and validation sets.

## Final Model
The final model was built using a CatBoost classifier, which was chosen due to its strong performance on structured datasets and its ability to handle categorical features effectively.The model was trained on the processed dataset using the selected features and validated using a robust cross-validation strategy.

## Results
The final model demonstrated stable and consistent performance across validation folds. The evaluation approach ensured that the model generalized well to unseen data while avoiding data leakage. The results indicate that the chosen preprocessing steps, feature handling, and modeling approach were effective in capturing the underlying patterns in the dataset.

