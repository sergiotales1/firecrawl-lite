import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from models.crawl_url import CrawledURL
from utils import log_system_usage, monitor_resources

async def crawl_website(url: str) -> CrawledURL:
    stop_event = asyncio.Event()
    monitor_task = asyncio.create_task(monitor_resources(stop_event, interval=0.5))
    try:
        browser_config = BrowserConfig(
        headless=True,
        verbose=True,  
    )
        async with AsyncWebCrawler(config=browser_config) as crawler:
            crawler_config = CrawlerRunConfig(
                verbose=True,  
            )
            log_system_usage()

            result = await crawler.arun(
                url=url,
                config=crawler_config
            )
            
            # Extract title from metadata or use a default
            title = "No title"
            if result.metadata and 'title' in result.metadata:
                title = result.metadata['title']
            elif hasattr(result, 'title') and result.title:
                title = result.title
                
            # Extract description from metadata
            description = "No description available"
            if result.metadata["description"]:
                description = result.metadata['description']
            
            markdown_content = result.markdown if result.markdown else "No content extracted"
            
            return CrawledURL(
                title=title,
                description=description or "",
                markdown=markdown_content, 
                url=url
            )
            
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}")
        return CrawledURL(
            title="Error",
            description=f"Failed to crawl URL: {str(e)}",
            markdown="",
            url=url
        )
    
    finally:
        stop_event.set()
        await monitor_task