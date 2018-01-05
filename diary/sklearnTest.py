#!/user/bin/env python
# -*- coding:utf-8 -*-
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    # Create logistic regression object
    model = LogisticRegression()

    # Train the model using the training sets and check score
    model.fit(X, y)
    model.score(X, y)

    # Equation coefficient and Intercept
    print('Coefficient: n', model.coef_)
    print('Intercept: n', model.intercept_)

    # Predict Output
    predicted = model.predict(x_test)