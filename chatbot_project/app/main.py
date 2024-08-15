from fastapi import FastAPI, Request, HTTPException
from fastapi.openapi.utils import get_openapi
from app.router import route_input
from app.utils import handle_error, log_user_interaction
import logging

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message", "")
        if not user_input:
            raise HTTPException(status_code=400, detail="No input provided")
        
        response = route_input(user_input)
        log_user_interaction(user_input, response)
        return {"response": response}
    
    except Exception as e:
        logging.error(f"Error during chat processing: {str(e)}")
        return {"error": handle_error(e)}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Chatbot API",
        version="1.0.0",
        description="API documentation for the Chatbot project",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
