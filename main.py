from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from reddit_scraper import get_top_reddit_post
from caption_generator import generate_caption
from image_generator import generate_image

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/meme")
async def create_meme():
    try:
        post_title = get_top_reddit_post()
        caption = generate_caption(post_title)
        image_url = generate_image(caption)
        return {"caption": caption, "image_url": image_url}
    except Exception as e:
        return {"error": str(e)}
