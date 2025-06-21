from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="GenAI App",
    description="APIs",
    version="0.0.1",
)


@app.get("/")
def main_page():
    return {
        "message": "success"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
