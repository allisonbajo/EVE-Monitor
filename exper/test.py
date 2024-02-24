import numpy as np

names = "CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"
feature_names = np.array(names)
print(feature_names[:-1])