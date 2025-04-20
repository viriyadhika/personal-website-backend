import argparse

from app.crawler.crawler_module.main_consumer import MainConsumer
from app.crawler.crawler_module import main_producer
from app.crawler.crawler_module.crawler import ptime
from app.crawler.crawler_module.refresh import auto_refresh

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run task", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("command", help='Either "producer", "consumer"')
    argument = vars(parser.parse_args())

    print(f"Running command with {argument}")

    try:
        command = argument["command"]
        if command == "producer":
            main_producer.run("Singapore", "Software Engineer")
        if command == "consumer":
            MainConsumer().run()
        if command == "refresh":
            auto_refresh()
        if command == "ptime":
            ptime.crawl_ptime()
    except KeyboardInterrupt:
        pass
