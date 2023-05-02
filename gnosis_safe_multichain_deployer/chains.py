ethereum_chain = {
    "chain_id": 1,
    "network": "ethereum",
    "rpc": "https://rpc.ankr.com/eth",
    "proxy_factory": "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2",
    "etherscan_endpoint": "https://api.etherscan.io/api"
}


optimism_chain = {
    "chain_id": 10,
    "network": "optimism",
    "rpc": "https://rpc.ankr.com/optimism",
    "proxy_factory": "0xC22834581EbC8527d974F8a1c97E1bEA4EF910BC",
    "etherscan_endpoint": "https://api-optimistic.etherscan.io/api"
}

binance_smart_chain = {
    "chain_id": 56,
    "network": "binance smart chain",
    "rpc": "https://rpc.ankr.com/bsc",
    "proxy_factory": "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2",
    "etherscan_endpoint": "https://api.bscscan.com/api"
}


gnosis_chain = {
    "chain_id": 100,
    "network": "gnosis",
    "rpc": "https://rpc.gnosischain.com",
    "proxy_factory": "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2",
    "etherscan_endpoint": "https://api.gnosisscan.io/api"
}

polygon_chain = {
    "chain_id": 137,
    "network": "polygon",
    "rpc": "https://rpc.ankr.com/polygon",
    "proxy_factory": "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2",
    "etherscan_endpoint": "https://api.polygonscan.com/api"
}


arbitrum_chain = {
    "chain_id": 42161,
    "network": "arbitrum",
    "rpc": "https://rpc.ankr.com/arbitrum",
    "proxy_factory": "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2",
    "etherscan_endpoint": "https://api.arbiscan.io/api"

}

avalanche_chain = {
    "chain_id": 43114,
    "network": "avalanche",
    "rpc": "https://rpc.ankr.com/avalanche",
    "proxy_factory": "0xC22834581EbC8527d974F8a1c97E1bEA4EF910BC",
    "etherscan_endpoint": "https://api.snowtrace.io/api"
}


supported_chains = {
    ethereum_chain["chain_id"]: ethereum_chain,
    optimism_chain["chain_id"]: optimism_chain,
    binance_smart_chain["chain_id"]: binance_smart_chain,
    gnosis_chain["chain_id"]: gnosis_chain,
    polygon_chain["chain_id"]: polygon_chain,
    arbitrum_chain["chain_id"]: arbitrum_chain,
    avalanche_chain["chain_id"]: avalanche_chain,
}
