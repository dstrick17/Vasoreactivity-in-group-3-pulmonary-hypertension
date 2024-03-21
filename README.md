# Vasoreactivity and Mortality in WHO Group 3 Pulmonary Hypertension

# Introduction - 
## In our study, explored how several variables impacted survival in patients with WHO group 3 pulmonary hypertension. This is a novel cohort of patients who underwent vasoreactivty testing with inhaled nitric oxide during their right heart catheterizations upon diagnsois.

## Before running this script, ensure you have the following installed: Python 3.x, pandas, lifelines, openpyxl (for reading Excel files). 

## We employed a two-stage statistical analysis to identify significant predictors of mortality. 

### cox-univariate.py - Initially, univariate Cox proportional hazards models were applied to each potential predictor to assess its individual association with mortality. Variables demonstrating a p-value of less than 0.10 in these univariate analyses as well as variables considered relevant by clinical expertise, such as age, sex, mPAP, were selected for further evaluation.

### cox-stepwise.py - Subsequently, we constructed a multivariate Cox proportional hazards model incorporating these selected variables. A backward stepwise elimination process was implemented to systematically remove variables if their association with the outcome, adjusted for the presence of other variables in the model, resulted in a p-value greater than 0.10. 

## We employed Kaplan-Meier survival analysis to better visualize mortality in this cohort.

### kaplan.py - Kaplan-Meier curve for all patients in this cohort.

### kaplan-delta-mpap.py and kaplan-delta-pvr.py - investigates the impact of changes in pulmonary vascular resistance (∆ PVR) as well as the change in mean pulmonary artery pressure (∆ mPAP ) after testing for vasoreactivity on survival outcomes within our dataset. Two distinct groups were then created based on the magnitude of change in PVR as well as change in mPAP. Kaplan-Meier estimators were then fitted to the data for each group to model survival probabilities over time. This allowed us to visualize the survival curves for both groups, providing insights into their respective survival trends. A log rank test was used to statistically compare the survival distributions between the two groups. 

## We conducted linear regressions to explore the relationship between parameters within our dataset. 

### linear-pvr.py - Visual representations of the regression lines were created to show the relationships between baseline pulmonary vascular resistance and the change in pulmonary vascular resistance after inhaled nitric oxide challenge..  
