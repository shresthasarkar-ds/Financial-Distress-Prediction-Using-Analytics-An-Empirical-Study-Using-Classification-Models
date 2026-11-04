install.packages("readxl")
install.packages("dplyr")
install.packages("caret")
install.packages("pROC")

library(readxl)
library(dplyr)
library(caret)
library(pROC)

getwd()

setwd("D:/Desktop 2/Dissertation")
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

# Generate predicted probabilities
pred_prob <- predict(model, type = "response")

# Create ROC curve
roc_curve <- roc(data$Distress, pred_prob)

# Calculate AUC
auc_value <- auc(roc_curve)

# Print AUC
print(auc_value)

# Convert ROC data into a data frame
roc_data <- data.frame(
  Specificity = roc_curve$specificities,
  Sensitivity = roc_curve$sensitivities
)

# Create a beautiful ROC curve
ggplot(roc_data, aes(x = 1 - Specificity,
                     y = Sensitivity)) +
  
  geom_line(color = "#1565C0", linewidth = 1.4) +
  
  geom_abline(intercept = 0, slope = 1,
              linetype = "dashed",
              color = "grey50",
              linewidth = 0.8) +
  
  annotate("text",
           x = 0.65,
           y = 0.20,
           label = paste("AUC =", round(as.numeric(auc_value), 4)),
           size = 5,
           fontface = "bold",
           color = "#1565C0") +
  
  labs(
    title = "ROC Curve – Logistic Regression",
    subtitle = "Financial Distress Prediction Model",
    x = "1 - Specificity (False Positive Rate)",
    y = "Sensitivity (True Positive Rate)"
  ) +
  
  theme_minimal() +
  
  theme(
    plot.title = element_text(size = 16, face = "bold",
                              hjust = 0.5),
    plot.subtitle = element_text(size = 11, hjust = 0.5),
    axis.title = element_text(size = 12, face = "bold"),
    axis.text = element_text(size = 10),
    panel.grid.minor = element_blank()
  ) +
  
  coord_equal()