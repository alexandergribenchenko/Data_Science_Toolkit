from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI(title="POC API Test")

class InputObject(BaseModel):
    inp_obj_attr_01: float
    inp_obj_attr_02: float
    inp_obj_attr_03: float

class OutputObject(BaseModel):
    out_obj_attr_01: InputObject
    out_obj_attr_02: str

@app.get('/')
def root_func():
    return {'message': 'Wellcome to de POC API Test'}

@app.get('/get_method_test', response_model=OutputObject)
def get_method_test_function(
    inp_obj_attr_01: float, 
    inp_obj_attr_02: float, 
    inp_obj_attr_03: float
):
    return {
        'out_obj_attr_01': {
            'inp_obj_attr_01': inp_obj_attr_01,
            'inp_obj_attr_02': inp_obj_attr_02,
            'inp_obj_attr_03': inp_obj_attr_03
        },
        'out_obj_attr_02': str(inp_obj_attr_01 + inp_obj_attr_02 + inp_obj_attr_03)
    }

@app.post('/post_method_test', response_model=OutputObject)
def post_method_test_function(input_object: InputObject):

    v_01 = input_object.inp_obj_attr_01
    v_02 = input_object.inp_obj_attr_02
    v_03 = input_object.inp_obj_attr_03

    return {
        'out_obj_attr_01': input_object,
        'out_obj_attr_02': str(v_01 + v_02 + v_03)
    }


if __name__ == '__main__':
    import uvicorn

    # For local development:
    # uvicorn.run("main:app", port=3000, reload=True)

    # For Docker deployment:
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
