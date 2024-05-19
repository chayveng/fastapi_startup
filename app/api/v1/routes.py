from fastapi import APIRouter

from app.api.v1.endpoints.todo import router as todo_router

routers = APIRouter()
router_list = [todo_router]

for router in router_list:
    router.tags = router.tags.append("v1")
    routers.include_router(router)