from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "World"}

@app.get("/ping/")
def read_root():
    return{"message": "pong"}







#
# обязательно добавьте view со следующими свойствами (данный view будет использован для проверки):
# путь /ping/
# статус ответа 200
# тело ответа — JSON объект {"message": "pong"}
#


# # import FASTAPI as FASTAPI
# from fastapi import FastAPI, Path, Request
# from starlette import status
# from starlette.responses import JSONResponse
#


#
#
# @app.get("/items/{item_id}")
# def get_item(item_id):
#     return {
#         "item": {"id": item_id}
#     }
#
#
# @app.post("/items")
# def create_item(data: dict):
#     return {
#         "item": data,
#     }
#




# @app.get("/{url_path:path}")
# def all_others(
#     url_path: str,
# ):
#     return {"request to": url_path}

# @app.exception_handler(404)
# async def custom_404_handler(request, exception):
#     return JSONResponse(
#         {
#         "request url": request.url.path,
#         "exception": str(exception),
#         },
#         status_code=404,
#     )

# @app.exception_handler(status.HTTP_404_NOT_FOUND)
# async def custom_404_handler(request, exception):
#     return JSONResponse(
#         {
#         "request url": request.url.path,
#         "exception": str(exception),
#         },
#         status_code=status.HTTP_404_NOT_FOUND,
#     )


# обязательно добавьте view со следующими свойствами
# (данный view будет использован для проверки):
# путь /ping/
# статус ответа 200
# тело ответа — JSON объект {"message": "pong"}





