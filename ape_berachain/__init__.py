from ape import plugins
from ape.api.networks import LOCAL_NETWORK_NAME, ForkedNetworkAPI, NetworkAPI, create_network_type
from ape_node import Node
from ape_test import LocalProvider

from .ecosystem import NETWORKS, Berachain, BerachainConfig


@plugins.register(plugins.Config)
def config_class():
    return BerachainConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Berachain


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "berachain", network_name, create_network_type(*network_params)
        yield "berachain", f"{network_name}-fork", ForkedNetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "berachain", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "berachain", network_name, Node

    yield "berachain", LOCAL_NETWORK_NAME, LocalProvider