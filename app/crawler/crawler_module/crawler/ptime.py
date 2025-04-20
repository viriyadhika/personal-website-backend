import json
import requests
from app.crawler.db.ptime.ptime import insert_ptime
from app.env import PTIME_URL
from app.crawler.model.base import VPTime


def crawl_ptime():
    response = requests.get(PTIME_URL)
    data: dict[str, dict[str, str]] = response.json()

    res = []
    for v_type, ctry_mapping in data.items():
        for ctry, p_time in ctry_mapping.items():
            if type(p_time) is str:
                res.append(VPTime(v_type=v_type, ctry_code=ctry, p_time=p_time))

    insert_ptime(res)
