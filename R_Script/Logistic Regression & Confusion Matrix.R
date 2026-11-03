install.packages("readxl")
install.packages("dplyr")
install.packages("caret")
install.packages("pROC")

library(readxl)
library(dplyr)
library(caret)
library(pROC)

getwd()

setwd("C:/Users/sarka/OneDrive/Desktop/Dissertation")
getwd()

library(readxl)

data <- read_excel("Financial Statements.xlsx")
head(data)
str(data)
summary(data)


colnames(data)

model_data <- data %>%
  select(`Current Ratio`,
         `Debt/Equity Ratio`,
         ROA,
         `Interest Coverage Ratio`,
         `Cash Flow from Operating`,
         `Inflation Rate(in US)`,
         Distress)

model_data$Distress <- as.factor(model_data$Distress)
str(model_data)

model <- glm(Distress ~ `Current Ratio` +
               `Debt/Equity Ratio` +
               ROA +
               `Interest Coverage Ratio` +
               `Cash Flow from Operating` +
               `Inflation Rate(in US)`,
             data = data,
             family = binomial)
summary(model)
pred_prob <- predict(model, type = "response")
pred_class <- ifelse(pred_prob > 0.5, 1, 0)
library(caret)
confusionMatrix(as.factor(pred_class), as.factor(data$Distress))

library(pROC)

roc_curve <- roc(data$Distress, pred_prob)
plot(roc_curve)
auc(roc_curve)
