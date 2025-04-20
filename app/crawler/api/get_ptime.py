from app.crawler.db.ptime.ptime import query_ptime
from .dto.get_ptime import PtimeRequest, PtimeResponse


def get_ptime(request: PtimeRequest):
    return [
        PtimeResponse(
            v_type=item.v_type,
            date=str(item.last_updated),
            ptime=item.p_time,
            ctry=item.ctry_code,
        )
        for item in query_ptime(request.ctry)
    ]
