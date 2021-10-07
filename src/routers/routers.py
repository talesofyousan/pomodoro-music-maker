import uuid
from logging import getLogger
from typing import Any, Dict, List

from fastapi import APIRouter
from src.optimizer import Recommender, SampleData

logger = getLogger(__name__)
router = APIRouter()


@router.get("/health")
def health() -> Dict[str, str]:
    return {"health": "ok"}


@router.get("/metadata")
def metadata() -> Dict[str, Any]:
    return {
        "input_type": "int",
        "input_shape": "(any, )",
        "input_sample": SampleData().list_music_time,
        "prediction_type": "int",
        "prediction_shape": "(any, any,)",
        "prediction_sample": [[4, 13, 3, 10, 1, 11, 12], [0, 2, 17, 5, 15, 16], [6, 7, 8, 9, 14, 18]],
    }


@router.get("/recommend/test")
def recommend_test() -> Dict[str, List[float]]:
    job_id = str(uuid.uuid4())
    recommendation = Recommender().get_recommended_music_index(SampleData().list_music_time)
    logger.info(f'test {job_id}: {recommendation}')
    return {"prediction":recommendation}


@router.post("/recommend")
def recommend(data: SampleData) -> Dict[str, List[List[int]]]:
    job_id = str(uuid.uuid4())
    recommendation = Recommender().get_recommended_music_index(data.list_music_time)
    logger.info(f"{job_id}: {recommendation}")
    return {"recommend": recommendation}

