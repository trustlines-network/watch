import requests
import logging
import json
import bernhard
import click
import functools
from tlwatch import util

logger = logging.getLogger(__name__)


def json_rpc_call(url, method, params=None):
    if params is None:
        params = []

    headers = {"content-type": "application/json"}
    payload = {"method": method, "params": params, "jsonrpc": "2.0", "id": 1}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.ok:
        return response.json().get("result")


def get_blockNumber(url):
    response = json_rpc_call(url, "eth_blockNumber")
    return util.decode_hex_encoded_number(response)


def watch_jsonrpc(url):
    try:
        blockNumber = get_blockNumber(url)
        return [
            {
                "service": "jsonrpc.blocknumber",
                "host": url,
                "state": "ok",
                "ttl": 30,
                "metric": blockNumber,
            }
        ]
    except BaseException as e:
        logger.warning("error in watch_etherscan:%s", e)
        return [{"service": "jsonrpc.blocknumber", "host": url, "state": "error"}]


@click.command()
@click.option("--riemann-host", default="localhost", envvar="RIEMANN_HOST")
@click.option("--riemann-port", default=5555, envvar="RIEMANN_PORT")
@click.option("--url", default="http://localhost:8545")
def jsonrpc(riemann_host, riemann_port, url):
    logging.basicConfig(level=logging.INFO)
    logger.info("version %s starting", util.get_version())
    logger.info("watching %s", url)
    util.watch_report_loop(
        lambda: bernhard.Client(riemann_host, riemann_port),
        functools.partial(watch_jsonrpc, url),
        10,
    )