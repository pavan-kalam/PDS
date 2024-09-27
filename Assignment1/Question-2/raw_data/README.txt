### Overview

In this question we had performed five visualization tasks on the Student perfromance dataset to make the analysis eazier.

### Folder Structure

Question-2/
├── raw_data/
│   ├── README.md
|   ├── StudentsPerformance.csv
├── clean_data/
│   └── student_performance_clean.csv
├── analysis_results/
│   ├── Explanation_on_Results.docx
│   ├── visualizations\
│   │   ├── test_score_distribution(Box plot).png
│   │   ├── reading_scores_by_gender(bar_graph).png
│   │   ├── line_plot.png
│   │   ├── test_score_distribution(Box plot).png
│   │   └── test_prep_by_race_and_lunch(Stacked Bar Plot).png
├── src/
│   ├── Bar_plot.py
│   ├── Box_plot.py
│   ├── line_plot.py
│   ├── Stacked_bar_chart.py
│   └── Star_plot.py
│   └── analysis_and_data_clean.py


### Data Cleaning:
   Here we will clean the raw data, by running the 'analysis_and_data_clean.py' file from 'src' folder.
   To do this to ensure that there will be no missing values or invalid entities in the data.


### Visualization:
 
 ## 1. Bar Graph:
    Here bar graph was used to check the performance among the the genders with reading scores.
    
    File: /Question-2/analysis_results/visualizations/reading_scores_by_gender(bar_graph).png

 ## 2. Box Plot:
    Here box plot was used to compare the student scores of all three (i.e., maths, reading and writing) based on completion of test preparation.

    File: /Question-2/analysis_results/visualizations/test_score_distribution(Box plot).png

 ## 3. Line Plot:
    Here the line plot compares the students from different races/ethnicities and their lunch types.

    File: /Question-2/analysis_results/visualizations/line_plot.png

 ## 4. Star plot:
    Here it creates a holistic view on the comparison for parental education and their children performance on all the three subjects.

    File: /Question-2/analysis_results/visualizations/radar_chart_parental_education(star_plot).png

 ## 5. Stacked bar chart:
    This visualization creates the comparasion on students those who completed or not completed the test preparation, grouped by their races/ethnicity and their lunch type.

    File: /Question-2/analysis_results/visualizations/test_prep_by_race_and_lunch(Stacked Bar Plot).png


#### Running the scripts

# Install the required libraries
  pip install pandas seaborn matplotlib

# Run the individual scripts
  python3 src/analysis_and_data_clean.py
  python3 src/Bar_plot.py
  python3 src/Box_plot.py
  python3 src/line_plot.py
  python3 src/Stacked_bar_chart.py
  python3 src/Star_plot.py


