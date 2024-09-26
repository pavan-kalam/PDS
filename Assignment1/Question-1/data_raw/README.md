Question-1 : Frailty Analysis
-----------------------------------

Work Flow:
---------
Question-1/
├── data_raw/
│   ├── frailty_data.csv
│   ├── README.md
├── data_clean/
│   ├── frailty_data_clean.csv
├── data_analysis/
│   ├── frailty_analysis.csv
│   ├── frailty_analysis_with_age_weight.csv
├── results/
│   ├── boxplot.png
│   ├── grip_strength_analysis.png
│   ├── grip_strength_curve_plotly1.html
│   ├── pairplot.png
├── src/
    ├── data_clean.py
    ├── data_analysis.py
    ├── data_analysis-2.py
    ├── visualization.py
    ├── visualization2.py
    ├── visualization_plotly.py


### Step-1: Raw data collection
 -- Here raw data will be collected and saved to the 'data_raw' folder

### Step-2: Data cleaning
 -- Here we will clean the raw data, by running the 'data_clean.py' python file from 'src' directory.
 -- Here we will ensure that there will be no missing values or invalid entities.

### Step-3: Data Analysis
 -- Now we will use the claned data results for the frailty analysis and results will be saved under 'data_analysis' directory.

### Step-4: Visualization results
 -- Now run the 'visualization.py' file from the 'src' directory to get the visualization results.
 -- In this case there are visualization results, 
    1) Pair plot: Here it shows the relation between 'Age', 'Weight', 'Grip strength' and it helps to identify the correlations between the given attributes.
    2) Box Plot: Here it shows the 'Age', 'Weight', 'Grip strengt' and it highlights the median values and outliers.

### Graphical Visualization:
    Here also included plot graph using plotly, for the comparison among 'Grip strength' and 'Age' with 'Frailty' curve.

    File: /Question-1/result/grip_strength_curve_plotly1.html


# Run the individual scripts
  cd Question-1
  python3 src/data_clean.py
  python3 src/data_analysis.py
  python3 src/data_analysis-2.py
  python3 src/visualization.py
  python3 src/visualization2.py
  python3 src/visualization_plotly.py