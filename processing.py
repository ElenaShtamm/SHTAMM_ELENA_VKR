import pickle

import pickle
def load_file(path='models/regressor_pipeline_1.pkl'):
    with open(path, 'rb') as f:
        model = pickle.load(f)

        return model


def predict(X):
    model = load_file('models/regressor_pipeline_1.pkl')
    y=model.predict([X])
   # preprocessor = load_file('models/preprocessor.pkl')
    #preprocessor.inverse_transform([y])
    return y
    #

