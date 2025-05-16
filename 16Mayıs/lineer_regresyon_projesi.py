import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "TV": [230,44,17,151,180,8,57,120,100,220],
    "Radio": [37,39,45,40,41,2,20,35,15,23],
    "Newspaper": [69,45,78,20,15,10,25,14,50,20],
    "Sales": [22,10,9,18,19,5,8,15,12,21]
}

df = pd.DataFrame(data)

x = df[["TV","Radio","Newspaper"]]
y = df["Sales"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)
print("Katsayı:")
print(model.coef_)
print(f"Intercept: {model.intercept_}")
