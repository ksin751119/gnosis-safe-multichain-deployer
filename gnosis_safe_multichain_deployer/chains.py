gnosis_chain = {
    "chain_id": 100,
    "network": "gnosis",
    "rpc": "https://rpc.gnosischain.com",
    "proxy_factory": "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2",
    "etherscan_endpoint": "https://api.gnosisscan.io/api"
}

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
}


arbitrum_chain = {
    "chain_id": 42161,
    "network": "arbitrum",
    "rpc": "https://rpc.ankr.com/arbitrum",
}
polygon_chain = {
    "chain_id": 137,
    "network": "polygon",
    "rpc": "https://rpc.ankr.com/polygon",
    "etherscan_endpoint": "https://api.polygonscan.com/api"

}


supported_chains = {
    gnosis_chain["chain_id"]: gnosis_chain,
    ethereum_chain["chain_id"]: ethereum_chain,
    optimism_chain["chain_id"]: optimism_chain,
    arbitrum_chain["chain_id"]: arbitrum_chain,
    polygon_chain["chain_id"]: polygon_chain,
}
