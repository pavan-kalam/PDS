### Overview

In this assignment we performed various tasks on the cars dataset.

### Folder Structure

Assignment2/
├── raw_data/
│   ├── README.md
|   ├── train.csv
├── clean_data/
│   └── Question-A_after_impute.csv
│   └── Question-A.csv
├── results/
│   ├── Question-B_removing_units.csv
│   ├── Question-c_one_hot_encoding.csv
│   ├── Question-d_calucated_car_age.csv
│   ├── Action_taken_on _missing_values.docx
│   ├── Question-e(results)\
│   │   ├── selected_columns.csv
│   │   ├── filter.csv
│   │   ├── rename.csv
│   │   ├── mutate.csv
│   │   ├── arrange.csv
│   │   └── summary.csv
├── src/
│   ├── Question-a_(finding_missing_impute).py
│   ├── Question-b_(removing_units_from_attributes).py
│   ├── Question-c(one_hot_encoded).py
│   ├── Question-d_(calculating_car_age).py
│   └── Question-e_(performing_operations).py


### Data Cleaning:
   Here we will clean the given raw data, by running the 'Question-a_(finding_missing_impute).py' file from 'src' folder.
   By running this code, it will check all the missing valules from all the columns in the given dataset.
   Once identifying the missing values, it will mutate the catagorical values with 'mode' operation, and for numerical values, it will mutate with 'median' operation.
   For 'New_Price' column, as the column contains 86% of missing values, I prefer to 'drop' the column.

   After performing this action, we have to make sure that there will be no missing values in the dataset.


### Actions performed

 ## Finding and taking action on missing values
     First we find the missing values and replace the catagorical columns with 'mode' and numerical columns with 'median' and the 'New_Price' column with more missing values will drop.

     File: clean_data/Question-A_after_impute.csv
 
 ## Removing units from the attributs
     Here we will remove the units from the attributes.

     File: results/Question-B_removing_units.csv

 ## Categorical to numerical
     Here we will convert categorical values to numerical for required attributs.

     File: results/Question-c_one_hot_encoding.csv

 ## Adding column to dataset
     Here we can add a new column by calculating the age of the car.

     File: results/Question-d_calucated_car_age.csv

 ## Performing the operations
     Here we will perform operations like select, filter, rename, mutate, arrange and summary on the dataset.



#### Running scripts

# Install the required libraries
  pip install pandas numpy datetime

# Run the scripts individually
  python3 src/Question-a_(finding_missing_impute).py
  python3 src/Question-a(finding_missing_impute).py
  python3 src/Question-b_(removing_units_from_attributes).py
  python3 src/Question-c(one_hot_encoded).py
  python3 src/Question-d_(calculating_car_age).py
  python3 src/Question-e_(performing_operations).py