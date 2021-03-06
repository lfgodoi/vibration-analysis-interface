"""

Analysis API

"""

# Importing packages and modules
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from sources.classes.dao import DAO
from sources.classes.processing import Processing
from sources.classes.visualization import Visualization

# Setting the route
router = APIRouter(prefix="/analysis", tags=["analysis"])

# Endpoint
@router.post("/")
async def run_analysis(request: Request):
    form = await request.form()
    try:
        data = jsonable_encoder(form)
        print(data)
        dataset_id = data["datasetId"]
        channel = data["channel"]
        slice_start = float(data["sliceStart"])
        slice_end = float(data["sliceEnd"])
        figure = data["figure"]
        dao = DAO(dataset_id, channel)
        sampling_frequency = dao.read_sampling_frequency()      
        samples = dao.read_samples(slice_start, slice_end)
        processing = Processing(sampling_frequency)
        processing.run(samples)
        visualization = Visualization()
        visualization.run(processing, figure)
        content = visualization.figure
        status = "success"
    except:
        content = "empty"
        status = "fail"
    return jsonable_encoder({"content": content, "status": status})