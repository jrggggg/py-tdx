import pytest
from pytdx.tdx import Tdx
import os
import json
import base64

conn_info_encoded = os.environ.get("TDX_SB_CONN")
conn_info = json.loads(base64.b64decode(conn_info_encoded))


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
    result = tdx_client.get_asset_with_model(asset_id=1145451)
    print(result.owning_customer_name)
    assert result.id == 1145451


def test_get_ticket(tdx_client):
    result = tdx_client.get_ticket(ticket_id=20896274)
    assert result["ID"] == 20896274


def test_get_kb_article(tdx_client):
    result = tdx_client.get_kb_article(kb_article_id=141785)
    assert result["ID"] == 141785
