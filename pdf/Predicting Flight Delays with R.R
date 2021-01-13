# Sets the R Working Directory
setwd('C:\\Users\\brayd\\Documents\\CIS 375\\FlightDelays')

######################
## Data Pre-Processing ##
######################

# Creates an object from the data set
delays_source = read.csv('FlightDelays.csv', stringsAsFactors = TRUE)

# Gets overall information from the data set using str()
str(delays_source)

# Creates a new object with the variables needed for analysis
delays <- delays_source[c(1, 2, 4, 8, 9, 10, 11, 13)]

# Gets the number of observations in each level in target variable using table()
table(delays$Flight.Status)

# Sets the random seed as 123
set.seed(123)

# Creates an object named train_sample with 90% of the data
library(caret)
train_sample <- createDataPartition(delays$Flight.Status, p = 0.9, list = FALSE)

# Creates delay_train and delay_test variables and divides the data using the train_sample
delays_train <- delays[train_sample,]
delays_test <- delays[-train_sample,]

# Gets the proportion of levels in target variables using prop.table() and table()
prop.table(table(delays$Flight.Status))
prop.table(table(delays_train$Flight.Status))
prop.table(table(delays_test$Flight.Status))

# Load "C50" package using library()
install.packages("C50")
library(C50)

# Creates an object named churn_model using C5.0() to build a decision tree model
delays_model <- C5.0.default(delays_train[ , -8], delays_train$Flight.Status)

# Uses summary to see the results
summary(delays_model)

# Uses plot() to visualize the tree
plot(delays_model)

# Loading "gmodels" package using library()
library(gmodels)

# Creates an object named delays_pred to see how the model performs
install.packages("pROC")
library("pROC")
delays_pred <- predict(delays_model, delays_test)

# Confusion Matrix Model
confMat_model <- confusionMatrix(delays_pred, delays_test$Flight.Status)
confMat_model

# Create an ROC Curve
delays_test_pred <- predict(delays_model, delays_test, type = "prob")
delays_test_roc <- roc(delays_test$Flight.Status, delays_test_pred[ , 2],
                       plot = TRUE, print.auc = TRUE)

## RANDOM FOREST

ctrl <- trainControl(method = 'cv', number = 5, 
                     selectionFunction = 'oneSE')
grid <- expand.grid(model = 'tree', 
                    trials = c(1,3,5,7,9),
                    winnow = FALSE) 
grid
#Random Forest - Overall
install.packages("randomForest")
library(randomForest)
set.seed(123)
delays_rf <- randomForest(as.factor(Flight.Status) ~ ., data = delays_train)
delays_rf_pred <- predict(delays_rf, delays_test)
confMat_rf <- confusionMatrix(delays_rf_pred, as.factor(delays_test$Flight.Status))
confMat_rf

#Random Forest - Tuned
grid_rf <- expand.grid(mtry = c(4, 8, 16))
grid_rf
set.seed(123)
delays_rf_tuned <- train(Flight.Status ~ .,
                          data = delays_train,
                          method = "rf",
                          metric = "Kappa", 
                          trControl = ctrl, 
                          tuneGrid = grid_rf)
delays_rf_tuned
delays_rf_tuned_pred <- predict(delays_rf_tuned,delays_test)
confMat_rf_tuned <- confusionMatrix(delays_rf_tuned_pred, as.factor(delays_test$Flight.Status))
confMat_rf_tuned

