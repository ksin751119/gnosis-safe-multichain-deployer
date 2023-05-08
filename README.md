[![Experimental](https://img.shields.io/badge/status-experimental-orange)](https://github.com/your-username/your-repository)



# Gnosis Safe Multichain Deployer
The Gnosis Safe Multichain is a tool that allows you to deploy the same Safe Vault address to multiple chains. For example, you can deploy the same Safe Vault address from Ethereum to Gnosis chains.


# Benefits
By using the Gnosis Safe Multichain, you can save time and effort in deploying multiple Safe Vaults to different chains. This also provides greater convenience and flexibility in managing your assets across different chains.


# How It Works
1. Make sure the factory address is the same for both the source chain and the destination chain.
2. To get creation transaction data, use the etherscan API.
3. Send the same transaction data to the destination chain and interact with the same factory address.


# Limitations
It's important to note that the Gnosis Safe Multichain tool has some limitations. For example, it may not work with all chains or may require additional setup steps for certain chains.

**Support Chains**


| CHAIN                | CHAIN ID | FACTORY |
| -------------------- | -------- | ------- |
| Ethereum             | 1        | 0xa6b71e26c5e0845f74c812102ca7114b6a896ab2 |
| Binance Smart Chain  | 56       | 0xa6b71e26c5e0845f74c812102ca7114b6a896ab2 |
| Gnosis               | 100      | 0xa6b71e26c5e0845f74c812102ca7114b6a896ab2 |
| Polygon              | 1137     | 0xa6b71e26c5e0845f74c812102ca7114b6a896ab2 |
| Arbitrum             | 42161    | 0xa6b71e26c5e0845f74c812102ca7114b6a896ab2 |
| Optimism             | 10       | 0xC22834581EbC8527d974F8a1c97E1bEA4EF910BC |
| Avalanche            | 43114    | 0xC22834581EbC8527d974F8a1c97E1bEA4EF910BC |


## Usage

To utilize the Gnosis Safe Multichain Deployer, follow these steps:

1. Install the required dependencies by executing the following command:

```bash
$ pip install -r requirements.txt
$ python setup.py install
```

2. Run the Gnosis Safe Multichain Deployer using one of the following commands:

```bash

$ gnosis-safe-multichain-deployer --src-chain-id <SRC_CHAIN_ID> --dst-chain-ids <DST_CHAIN_1>,<DST_CHAIN_2> --address <SAFE_ADDRESS> --api-key <ETHERSCAN_API_KEY> --private-key <DEPLOYER_PRIVATE_KEY>
```

Replace the following placeholders with appropriate values:

- **<SRC_CHAIN_ID>**: Source chain ID
- **<DST_CHAIN_1,DST_CHAIN_2>**: Comma-separated destination chain IDs
- **<SAFE_ADDRESS>**: Safe Vault address
- **<ETHERSCAN_API_KEY>**: Etherscan API key
- **<DEPLOYER_PRIVATE_KEY>**: Deployer's private key

Example command:
```bash
$ gnosis-safe-multichain-deployer --src-chain-id 1 --dst-chain-ids 56,137,42161 --address 0x64bD0FD02B00E0d2762C415923AB6C2E71C3e13B --api-key <ETHERSCAN_API_KEY> --private-key <DEPLOYER_PRIVATE_KEY>

```

# Demo Video
[![示例影片](https://i9.ytimg.com/vi_webp/J0CH8WQGbWM/mq1.webp?sqp=CNSK4qIG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYACtAWKAgwIABABGD8gWyhyMA8=&rs=AOn4CLDLd9w8TjbcLHoSTR4aUSrC2vVPxQ)](https://youtu.be/J0CH8WQGbWM)




# Conclusion
Overall, the Gnosis Safe Multichain is a useful tool for anyone who wants to deploy the same Safe Vault address to multiple chains. With its compatibility with various chains and potential time savings, it's definitely worth considering for anyone managing assets across different chains.
