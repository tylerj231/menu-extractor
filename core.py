import json

import pdfplumber

from anthropic import (
    Anthropic,
    APITimeoutError,
    APIConnectionError,
    BadRequestError,
    NotFoundError,
)

from logger import logger
from settings import settings
from models import Menu
from utils import SYSTEM_PROMPT

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)


def read_file(filename: str) -> str:
    """
    Read a pdf file and return its content.
    :return:
    """
    with pdfplumber.open(filename) as pdf:
        text = " "
        for page in pdf.pages:
            text = text + page.extract_text()
    return text


def parse_extracted_text_from_file(
    text: str, claude_model: str = settings.DEFAULT_CLAUDE_MODEL
) -> dict | None:
    """
    Parse a text into a validated Menu model converted to dict using Anthropic API.
    :param claude_model:
    :param text:
    :return:
    """
    try:
        response = client.messages.parse(
            model=claude_model,
            system=SYSTEM_PROMPT,
            max_tokens=10000,
            messages=[
                {
                    "role": "user",
                    "content": text,
                }
            ],
            output_format=Menu,
        )
        return Menu.model_validate(response.parsed_output).model_dump()
    except (
        APIConnectionError,
        APITimeoutError,
        BadRequestError,
        NotFoundError,
    ) as error:
        logger.exception(error)


def parse_to_json(menu_dict: dict) -> None:
    """
    Parse a menu model into a JSON file.
    :param menu_dict:
    :return:
    """
    with open("result.json", "w") as file:
        json.dump(menu_dict, file, indent=4)
