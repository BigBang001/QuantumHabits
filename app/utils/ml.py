from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Function to predict habits using Decision Tree Regression
def predict_habits(data):
    
    model = DecisionTreeRegressor(random_state=42)
    
    
    X = np.array([d[0] for d in data]).reshape(-1, 1)  
    y = np.array([d[1] for d in data])                
    
    model.fit(X, y)
    
    predictions = model.predict(X)
    
    return predictions


if __name__ == "__main__":
    #  (daily exercise time in minutes and corresponding steps taken)
    data = [
        (30, 5000),    # Exercise for 30 minutes results in 5000 steps
        (45, 7000),    # Exercise for 45 minutes results in 7000 steps
        (60, 9000),    # Exercise for 60 minutes results in 9000 steps
        (15, 3000),    # Exercise for 15 minutes results in 3000 steps
        (90, 11000),   # Exercise for 90 minutes results in 11000 steps
    ]
    
    # Predict habits
    predictions = predict_habits(data)
    
    print("Daily Exercise Time (minutes) - Steps Taken:", data)
    print("Predicted Steps:", predictions)
