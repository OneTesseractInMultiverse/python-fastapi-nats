from fastapi import APIRouter, HTTPException
from app.logging.syslog_impl import StandardOutputLogger
router = APIRouter()


# -----------------------------------------------------------------------------
# POST MESSAGE
# -----------------------------------------------------------------------------
@router.get('/item/{item_id}', tags=['Item'])
async def get_item(item_id: int):
    if item_id == 1:
        return {
            "id": "1",
            "title": "test item"
        }
    else:
        raise HTTPException(status_code=404, detail=f'Item {item_id}')
