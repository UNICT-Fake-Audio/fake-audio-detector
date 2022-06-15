import sys
import joblib
from shared.feature_extraction import get_all_features_from_sample

MODEL = "models/ADC_trained_model.sav"
FILE_PATH = sys.argv[1]

sample_features = get_all_features_from_sample(FILE_PATH)
model = joblib.load(MODEL)
results = model.predict([sample_features])

# print(results)

res = "fake" if results[0] == 1 else "real"
print("The sample audio is " + res)
