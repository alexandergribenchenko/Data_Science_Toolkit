from fastapi import FastAPI
from pydantic import BaseModel

class Penguin(BaseModel):
    culmen_length: float
    culmen_depth: float
    flipper_length: float

class PenguinSpeciesPrediction(BaseModel):
    features: Penguin
    prediction: str

app =FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de predicción de pingüinos"}

@app.get('/get', response_model=PenguinSpeciesPrediction)
def get_func(cl: float, cd: float, fl: float):
    """
    Serves predictions given query parameters specifying the penguin's
    features.

    Inputs:
        - cl: culmen length in millimeters
        - cd: culmen depth in millimeters
        - fl: flipper length in millimeters
    """

    return {
        'features': {
            'culmen_length': cl,
            'culmen_depth': cd,
            'flipper_length': fl
        },

        'prediction': cl+cd+fl,
    }

@app.post('/json', response_model=PenguinSpeciesPrediction)
def post_json(penguin: Penguin):
    """
    Serves predictions given a request body specifying the penguin's features.

    Inputs:
        - penguin: request body of type `Penguin` with culmen_length,
                   culmen_depth, and flipper_length attributes
    """

    cl = penguin.culmen_length
    cd = penguin.culmen_depth
    fl = penguin.flipper_length

    return {
        'features': penguin,
        'prediction': cl+cd+fl,
    }


if __name__ == '__main__':
    import uvicorn

    # For local development:
    # uvicorn.run("main:app", port=3000, reload=True)

    # For Docker deployment:
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
