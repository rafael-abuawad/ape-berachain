from typing import ClassVar, Dict, Tuple, cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    # "mainnet": (0,0 ),
    "bartio": (80084, 80084),
}


class BerachainConfig(BaseEthereumConfig):
    NETWORKS: ClassVar[Dict[str, Tuple[int, int]]] = NETWORKS
    # mainnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)
    bartio: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)


class Berachain(Ethereum):
    fee_token_symbol: str = "BERA"

    @property
    def config(self) -> BerachainConfig:  # type: ignore[override]
        cfg = self.config_manager.get_config("berachain")
        return cast(BerachainConfig, cfg)