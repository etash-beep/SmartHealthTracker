import joblib
import pandas as pd

def loadModel():
    model=joblib.load("models/weight_predictor.pkl")
    return model

def predictWeight(
    calories,
    protein,
    carbs,
    fats,
    fiber,
    water,
    sleep,
    workout,
    steps):
    model=loadModel()
    input_df = pd.DataFrame({
    "Calories": [calories],
    "Protein_g": [protein],
    "Carbohydrates_g": [carbs],
    "Fats_g": [fats],
    "Fiber_g": [fiber],
    "Water_L": [water],
    "Sleep_hr": [sleep],
    "Workout_Min": [workout],
    "Steps": [steps]
})
    prediction=model.predict(input_df)
    return prediction[0]