import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
df = pd.read_csv("train.csv")
df = df[["LotArea", "YearBuilt", "GrLivArea", "FullBath", "BedroomAbvGr", "GarageCars", "SalePrice"]]
df = df.dropna()
X = df[["LotArea", "YearBuilt", "GrLivArea", "FullBath", "BedroomAbvGr", "GarageCars"]]
y = df["SalePrice"]
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
r2 = r2_score(y_test, predictions)
mse = mean_absolute_error(y_test, predictions)
print("Predictions:", predictions)
print("MSE:", mse)
print("R2 score:", r2)
joblib.dump(model, "house_price.pkl")
