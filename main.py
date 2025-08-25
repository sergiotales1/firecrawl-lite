from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from crawler import crawl_website
from models.crawl_url import CrawledURL
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

crawled = CrawledURL(
    title="Example Domain",
    description="This domain is for use in illustrative examples in documents.",
    markdown="# Example Domain\n\nThis domain is for use in illustrative examples in documents..."
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/", response_class=HTMLResponse)
async def crawl_url(request: Request, url: str = Form(...)): 
    global crawled
    crawled = await crawl_website(url)

    return RedirectResponse(f"/", status_code=303)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, url: str = None):
    """Display the home page with optional crawled results"""
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "crawled": crawled,
        "submitted_url": url
    })

if __name__ == "__main__": 
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Receives the port from render
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)