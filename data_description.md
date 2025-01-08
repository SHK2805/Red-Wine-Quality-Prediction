# Data Description
* This dataset is related to red variants of the Portuguese "Vinho Verde" wine.
* The dataset used in this project is the Wine Quality dataset from UCI Machine Learning Repository.
* This project predicts the wine quality based on the input features.
* [Data URL](https://github.com/SHK2805/datasets/raw/refs/heads/main/winequality/winequality-data.zip)

### Description
* The url contains the **winequality-data.zip** file which contains the file **winequality-red.csv**
* The dataset is clean and ready for analysis.
* Input features are given in the **winequality-red.csv** file
  * fixed acidity 
  * volatile acidity 
  * citric acid 
  * residual sugar 
  * chlorides 
  * free sulfur dioxide 
  * total sulfur dioxide 
  * density 
  * pH 
  * sulphates 
  * alcohol
* Output feature 
  * quality (score between 0 and 10)

### Details

| Column Name           | Data Type | Non-Null Count | Description                          |
|-----------------------|-----------|----------------|--------------------------------------|
| fixed acidity         | float64   | 15,000         | Measure of acidity in the wine       |
| volatile acidity      | float64   | 15,000         | Acidity that evaporates easily       |
| citric acid           | float64   | 15,000         | Amount of citric acid in the wine    |
| residual sugar        | float64   | 15,000         | Sugar remaining after fermentation   |
| chlorides             | float64   | 15,000         | Chloride content in the wine         |
| free sulfur dioxide   | float64   | 15,000         | Sulfur dioxide that hasn't bonded yet|
| total sulfur dioxide  | float64   | 15,000         | Total sulfur dioxide in the wine     |
| density               | float64   | 15,000         | Density of the wine                  |
| pH                    | float64   | 15,000         | pH level of the wine                 |
| sulphates             | float64   | 15,000         | Sulphate content in the wine         |
| alcohol               | float64   | 15,000         | Alcohol content in the wine          |
| quality               | float64   | 15,000         | Quality score (0-10) of the wine     |

#### Shape of the dataset
* The dataset contains 15,000 rows and 12 columns

#### Missing Values:
* There are no missing or null values in any of the columns. All 15,000 entries are complete.

#### Unique Values:
* As there are no categorical-like features, this dataset doesn't require analysis of unique values.
