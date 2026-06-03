import logging

# Create custom logger and set log level.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create custom console and file handlers and set respective log levels.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.WARNING)

# Create a custom format for log messages.
formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

# Add custom handlers to the logger and set a format for handlers.
logger.addHandler(console_handler)
logger.addHandler(file_handler)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
