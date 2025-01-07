import sys
import joblib
from shared.constants import SP_FEATS_NAMES, SPECTRUM_FEATURES
from shared.feature_extraction import get_all_features_from_sample

MODEL = "models/10-04-2023/FoR/Fake_or_Real_silence_ADC.sav"
# MODEL = "models/15-01-2022/ASVspoof_ADC_trained_model.sav"
FILE_PATH = sys.argv[1]

sample_features = get_all_features_from_sample(FILE_PATH)

with open("output_features.csv", "a+", encoding="utf8") as f:
    feats_names = SP_FEATS_NAMES + ["bit_rate"] + SPECTRUM_FEATURES
    f.write(",".join(feats_names))
    f.write("\n")
    f.write(",".join([str(v) for v in sample_features]))
    f.write("\n")

print("Features saved in output_features.csv")

# model = joblib.load(MODEL)
# results = model.predict([sample_features])

# print(results)

# res = "fake" if results[0] == 1 else "real"
# print("The sample audio is " + res)
