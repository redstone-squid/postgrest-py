import pytest
from httpx import Headers, QueryParams

from postgrest import AsyncQueryRequestBuilder
from postgrest.utils import AsyncClient


@pytest.fixture
async def query_request_builder():
    async with AsyncClient() as client:
        yield AsyncQueryRequestBuilder(
            client, "/example_table", "GET", Headers(), QueryParams(), {}
        )


def test_constructor(query_request_builder: AsyncQueryRequestBuilder):
    builder = query_request_builder

    assert builder.path == "/example_table"
    assert len(builder.headers) == 0
    assert len(builder.params) == 0
    assert builder.http_method == "GET"
    assert builder.json == None
