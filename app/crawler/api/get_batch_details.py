from typing import List
from app.crawler.api.dto.get_batch_details import (
    GetBatchDetailRequest,
    GetBatchDetailResponse,
)
from app.crawler.db.batch_company import get_batch_content
from datetime import datetime


def get_db_result(id: str, timestamp: int):
    timestampStr = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    return get_batch_content(id, timestampStr)


def handle_get_batch_details(
    request: GetBatchDetailRequest,
) -> List[GetBatchDetailResponse]:
    s = set()
    for i in get_db_result(request.id, request.comparison_timestamp):
        s.add(i.job_id)

    final_result = []
    for i in get_db_result(request.id, request.timestamp):
        final_result.append(
            GetBatchDetailResponse(
                company=i.company,
                job_id=i.job_id,
                job_name=i.job_name,
                link=i.link,
                description=i.description,
                employee=i.employee,
                is_new=i.job_id not in s,
            )
        )

    return final_result
