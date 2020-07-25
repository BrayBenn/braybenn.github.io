# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:44:29 2020

@author: brayd
"""

import pandas as pd
import seaborn as sns
import numpy as np
import statsmodels.api as sm

#Part 1 - Exploratory Data Analysis

df = pd.read_csv('loan-data-v1.csv')
df.head(5)
df.info()
df.describe()
df[['Age','Annual Income','Loan Amount']].corr()
df['Loan Type'].unique()


df_distplot = sns.distplot(df['Age'],bins=18,color='k')
# This visualization shows the breakdown of age by density. We can see that 
# our data ranges from under 20 years old to nearly 80 years old.

df_barplot = sns.barplot(x = df['Loan Amount'], y = df['Loan Type'], orient = 'h')
# This visualization shows the breakdown of loan amounts by loan type. We see
# that the higher value loans are for home and business, with the lower amounts
# being for personal and auto loans.

df.boxplot('Annual Income','Loan Type')
# This visualizaiton shows the annual income by loan type. It shows that on average,
# people with auto and business loans make more money.

df_scatterplot = sns.scatterplot(x = df['Annual Income'] , y = df['Loan Amount'])
# This visualization is a scatterplot, plotting the points based on annual income and loan amount.
# We see that there is very little correlation between these variables, as there is no trend in 
# the data.

#Part 2 - Statistical Regression Analysis

df['Flag'] = df['Days Delinquent'] > 90
df['log_annual_income'] = np.log(df['Annual Income'])
df['log_loan_amount'] = np.log(df['Loan Amount'])
df['Loan Type'].unique()
df = pd.get_dummies(df, prefix='LoanType', columns=['Loan Type'])
# Independent variables 'X'
X = df[['Age','log_annual_income','log_loan_amount', 
        'LoanType_Auto','LoanType_Business','LoanType_Home']]
# Dependent variable 'y'
y = df['Flag']
results = sm.Logit(y, X).fit()# Estimated model summary
results.summary()
results.summary2()
# Based on the logit results, we see that we do not have a sufficient
# model to predict whether or not a customer will be delinquent for over
# 90 days. When looking at the p-values shown in our results.summary2() output,
# we see that none of our independent variables are significant at the 0.05
# alpha level to predict if a customer will be flagged or not.

# Part 3 - Predictive Analytics with Machine Learning
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=2, random_state=1)
cluster_labels = kmeans_model.fit_predict(df[['log_annual_income','log_loan_amount']])
df['cluster'] = cluster_labels

sns.scatterplot(x = df['log_annual_income'], y = df['log_loan_amount'], hue=df['cluster'])


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
#The line of code above uses sklearn to split the loan data into a train and test
# split, with the test size telling it to split it 70/30


lr_model = LogisticRegression().fit(X_train, y_train)
#The line of code above creates a logistic regression training set using
# the X_train and y_train variables


y_pred = lr_model.predict(X_test)
#The line of code above uses the lr_model we just created to predict "Flag"
# for the test set


print('Prediction accuracy of logistic regression classifier on test set:')
print('{:.2f}'.format(lr_model.score(X_test, y_test)))

from sklearn.metrics import confusion_matrix
cmat = confusion_matrix(y_test, y_pred)
# The line of code above creates a matrix showing the predicted label and
# the true label. This can be used to evaluate the performance of our
# model

print(cmat)

from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
# The line of code above creates a classification report between the true label
# and the predicted label. This can show us a report of the precision of our
# predictions so we can analyze the accuracy of our model

print(report)
