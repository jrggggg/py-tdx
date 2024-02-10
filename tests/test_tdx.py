import pytest
from pytdx.tdx import Tdx
import os
from dotenv import load_dotenv
import json

load_dotenv()

conn_info = json.loads(os.environ.get("TDX_SB_CONN"))


@pytest.fixture
def tdx_client():
    return Tdx(
        username=conn_info[0],
        password=conn_info[1],
        hostname=conn_info[2],
        environment=conn_info[3],
        asset_app_id=conn_info[4],
        client_portal_app_id=conn_info[5],
        ticketing_app_id=conn_info[6],
        is_admin=conn_info[7],
    )


def test_get_asset(tdx_client):
    result = tdx_client.get_asset(asset_id=1145451)

    response_test_data = {"ID": 1145451}

    assert result["ID"] == response_test_data["ID"]
