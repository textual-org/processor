from fastapi import FastAPI, WebSocket
import whisper

app = FastAPI()

model = whisper.load_model("base")


@app.get("/")
def index():
    return {"message": "This is the Whisper API."}


@app.get("/test-audio")
def index():
    print("Testing audio processing...")
    result = model.transcribe("audio.mp3")
    print("Finished audio processing!")
    return {"message": result["text"]}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
