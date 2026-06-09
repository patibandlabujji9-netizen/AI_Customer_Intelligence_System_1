from utils.helpers import load_model
import pandas as pd

def predict_segments(df):
    model = load_model("saved_models/segment_model.pkl")
    return model.predict(df)