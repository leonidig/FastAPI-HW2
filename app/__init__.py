import asyncio
from fastapi import FastAPI


app = FastAPI(debug=True)

from . import routes


def main() -> None:
    asyncio.run(app)