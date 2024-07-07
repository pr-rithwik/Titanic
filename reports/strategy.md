### Feature Engineering
#### Iteration - 1
- "PassengerId" - set as index
- "Survived" - separate and remove as it is the output
- "Pclass" - one hot encoding
- "sex" - one hot encoding
- "Embarked" - handle missing data based on Pclass mode, one hot encoding
- "Age" - handle missing data based on Pclass median, bin it into categories (0-9, 10-19) & one hot encoding
- "Fare" - should be standardized and normalised

- "Ticket" - remove, not needed
- "Name" - remove, no use
- "cabin" - remove, not needed