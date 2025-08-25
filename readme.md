# Firecrawl-Lite

A lightweight and cost-effective version of [Firecrawl](https://www.firecrawl.dev/) built with **FastAPI** and **crawl4ai**.
This project provides a simple and fast way to crawl websites and generate markdown summaries via a user-friendly frontend.

![Screenshot_6](https://github.com/user-attachments/assets/0ade4bdc-cae1-4430-bc32-8cb7b9265564)

## Features

- **FastAPI backend** serving API endpoints.
- **Frontend integration** for easy interaction.
- **crawl4ai-powered** website crawling and markdown generation.
- Quick deployment and lightweight setup.

<video width="600" controls>
  <source src="https://github.com/user-attachments/assets/e6003739-51b0-4421-8f6f-1e948df0eeaa" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Getting Started

### Prerequisites

- Python 3.9+ (recommended)
- Virtual environment (venv)

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/sergiotales1/firecrawl-lite.git
   cd firecrawl-lite
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**

   ```bash
   python main.py
   ```

The server will start and can be accessed at `http://127.0.0.1:8000/`.

### Running with Docker

To run the app without installing dependencies locally, use the Docker image:

```bash
docker run -p 8000:8000 sergiotales/firecrawl-lite:0.1
```

This will start the container and expose the app at `http://127.0.0.1:8000/`.

## Usage

- Open the frontend in your browser.
- Enter a website URL to crawl.
- Receive a clean markdown summary of the page.

## Project Structure

```
firecrawl-lite/
├── models/            # CrawledURL pydantic model
├── static/            # CSS and Javascript files
├── templates/         # HTML file
├── main.py            # FastAPI entry point
├── crawler.py         # crawl logic
├── utils.py           # Loggers to see app's performance
├── Dockerfile         # Docker
├── requirements.txt   # Project dependencies
└── README.md
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance functionality.

## License

MIT License

