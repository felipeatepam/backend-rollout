"""Example of fastapi main file."""

import os
from typing import Union

from fastapi import FastAPI

host = os.getenv("HOSTNAME", "unknown")
app = FastAPI()


@app.get("/")
def read_root():
    """Returns Hello World."""
    return {"Hello": "World"}


@app.get("/api/hello")
def hello():
    """Returns Kubernetes World."""
    return f"Hello, KubeRocketCI v2 from {host}"


@app.get("/items/{item_id}")
def read_item(item_id: int, item_count: Union[str, None] = None):
    """Returns numbers of items."""
    return {"item_id": item_id, "q": item_count}
