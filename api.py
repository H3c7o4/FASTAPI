from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
from starlette.responses import RedirectResponse


class CoordIn(BaseModel):
    password: str
    lat: float
    lon: float
    zoom: Optional[int] = None

class CoordOut(BaseModel):
    lat: float
    lon: float
    zoom: Optional[int] = None

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'hello': 'world'}

@app.get('/component/{component_id}')
async def get_component(component_id: int):
    return {'component_id': component_id}

@app.get('/component/')
async def read_component(number: int, text: Optional[str]):
    return {'number': number, 'text': text}

@app.post('/postion/', response_model=CoordOut)
async def make_position(coord: CoordIn):
    return coord #CoordOut(lat=coord.lat, lon=coord.lon, zoom=coord.zoom)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)