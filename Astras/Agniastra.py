# Importing the Regression Libraries
from sklearn import *
import xgboost
import catboost

# Importing Basic Libraries
import numpy as np
import pandas as pd
import warnings as w

w.filterwarnings("ignore")
pd.set_option("display.float_format", lambda x: "%.2f" % x)


# Making a dataframe to store metrics and comparing the models
def regression_model_comparison(X, y, scaling=None):
    """This function takes in the X , y dataframes and Scaling method and Returns a dataframe with the metrics of the models.

    Args:
        X (pd.DataFrame): _description_
        y (pd.DataFrame): _description_
        scaling (str, optional): _description_. Defaults to None. (ss: StandardScaler, mm: MinMaxScaler)

    Returns:
        pd.DataFrame: The dataframe with the metrics of the models.
    """
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=69)

    numerical_features = [feature for feature in X.columns if X[feature].nunique() > 10]
    
    if scaling == "ss":
        sc = sklearn.preprocessing.StandardScaler()
        X_train[numerical_features] = sc.fit_transform(X_train[numerical_features])
        X_test[numerical_features] = sc.transform(X_test[numerical_features])
        pass
    elif scaling == "mm":
        mm = sklearn.preprocessing.MinMaxScaler()
        X_train[numerical_features] = mm.fit_transform(X_train[numerical_features])
        X_test[numerical_features] = mm.transform(X_test[numerical_features])
        pass

    df_metrics = {}

    # Fitting the models and storing the metrics
    for name, model in model_list:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        df_metrics[name] = {
            "Train Score": model.score(X_train, y_train),
            "Test Score": model.score(X_test, y_test),
            "MSE": sklearn.metrics.mean_squared_error(y_test, y_pred),
            "MAE": sklearn.metrics.mean_absolute_error(y_test, y_pred),
            "RMSE": np.sqrt(sklearn.metrics.mean_squared_error(y_test, y_pred)),
            "R2 Score": sklearn.metrics.r2_score(y_test, y_pred),
        }
    # Comparing the models
    comparison = pd.DataFrame(df_metrics).T
    comparison.sort_values(by="R2 Score", ascending=False, inplace=True)
    return comparison
