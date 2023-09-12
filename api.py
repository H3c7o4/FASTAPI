from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'hello': 'world'}

@app.get('/component/{component_id}')
async def get_component(component_id: int):
    return {'component_id': component_id}

@app.get('/component/')
async def read_component(number: int, text: str):
    return {'number': number, 'text': text}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)