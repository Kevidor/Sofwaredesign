#from scipy.special import jn, yn, jn_zeros, yn_zeros
#from scipy.integrate import quad, dblquad, tplquad
#import sympy as sp
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()
x_train_full, x_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state= 42)
x_train, x_vaild, y_train, y_vaild = train_test_split(housing.data, housing.target, random_state= 42)
mlp_reg = MLPRegressor(hidden_layer_sizes= [50, 50, 50], random_state= 42)
pipeline = make_pipeline(StandardScaler(), mlp_reg)
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_vaild)
rmse = mean_squared_error(y_vaild, y_pred, squared= False)
print(f"RMSE = {rmse}")
