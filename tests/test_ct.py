import pytest
from fastapi.testclient import TestClient
from src.app import app
import numpy as np

client = TestClient(app)

def test_simple():
    response = client.get('/health')
    print('response.json()->', response.json())
    assert response.status_code == 200
    assert response.json() == {'health':'ok'}


@pytest.mark.parametrize(('list_music_time'), [
    ([100, 110, 120, 130, 0, 140, 160, 170, 180, 190, 200, 101]),
    ([100.0, 110.0, 120.0, 130.0, 140.0, 160.0, 170.0, 180.0, 190.0, 200.0, 101.0]),
    ([100, 110, 120, 130, 140, 160, 170, 180, 190, 200, 101]),
    ([100, 110, 120, 130, 140, 160, 170, 180, 190, 200, 101, 100000]),
    ([100, 110, 120, 130, 140, 160, 170, 180, 190, 200, 101] * 1000)
])
def test_recommend_normal(list_music_time):
    header = {"Content-Type": "application/json" }
    response = client.post('/recommend', headers=header, json={'list_music_time': list_music_time})
    assert response.status_code == 200
    result = response.json()['recommend']
    assert np.concatenate(result).dtype == int
    assert max(np.concatenate(result)) < len(list_music_time) and min(np.concatenate(result)) >= 0

@pytest.mark.parametrize(('list_music_time', 'error_code'), [
    ([100, 110, 120, 130, 140, 'string', 'hogehoge', 180, 190, 200, 101], 422)
])
def test_recommend_abnormal(list_music_time, error_code, ):
    header = {"Content-Type": "application/json" }
    response = client.post('/recommend', headers=header, json={'list_music_time': list_music_time})
    assert response.status_code == error_code
