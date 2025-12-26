data <- read.csv("../data/dataset_somniferes.csv")

differences <- data$hyoscine - data$hyosciamine

shapiro_result <- shapiro.test(differences)
print(shapiro_result)

test_result <- wilcox.test(data$hyosciamine, 
                           data$hyoscine, 
                           paired = TRUE)

print(test_result)
