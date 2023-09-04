
import numpy as np
from xgboost import XGBRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def func2(x_):
    y1_ = np.sin(x_[:, 0].reshape(-1, 1))
    # y1_ += np.random.rand(*y1_.shape) * 0.3
    y2_ = np.cos(x_[:, 1].reshape(-1, 1))
    # y2_ += np.random.rand(*y2_.shape) * 0.3
    return np.concatenate([y1_, y2_], axis=1)

def func1(x_):
    y1_ = np.sin(x_[:, 0].reshape(-1, 1))
    # y1_ += np.random.rand(*y1_.shape) * 0.3
    y2_ = np.cos(x_[:, 1].reshape(-1, 1))
    # y2_ += np.random.rand(*y2_.shape) * 0.3
    return y1_ + y2_


x = np.random.randn(100, 2) * 0.5
y = func1(x)
y_class = np.ones_like(y)
y_class[y<0.0] = 0
y_class[y>0.5] = 2

model = XGBRegressor()
model.fit(x, y)
print(model)

model_class = xgb.XGBClassifier()
model_class.fit(x, y_class)
print(model_class)


x2 = np.random.randn(100, 2) * 0.5
y2 = func2(x)

model2 = XGBRegressor()
model2.fit(x2, y2)

print(model2)