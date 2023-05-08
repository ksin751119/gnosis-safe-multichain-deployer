import unittest
from unittest.mock import MagicMock, patch
from .cli import get_creation_transaction_hash
from .cli import get_dst_chain_ids
from .cli import verify_proxy_factory_address
from .chains import supported_chains


class TestCLI(unittest.TestCase):
    def test_get_creation_transaction_hash(self):
        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "status": "1",
                "result": [{"txHash": "0x123"}],
            }
            mock_get.return_value = mock_response

            endpoint = "https://fake.endpoint"
            safe_address = "0xABC"
            api_key = "fake_api_key"
            result = get_creation_transaction_hash(
                endpoint, safe_address, api_key
            )
            self.assertEqual(result, "0x123")

    def test_get_dst_chain_ids(self):
        value = "1,10,137"
        result = get_dst_chain_ids(value)
        self.assertEqual(result, [1, 2, 3])

    def test_verify_proxy_factory_address(self):
        src_chain_id = 1
        dst_chain_ids = [137, 42161]
        tx_to = supported_chains[src_chain_id]["proxy_factory"].lower()

        # This should not raise any exceptions
        verify_proxy_factory_address(src_chain_id, dst_chain_ids, tx_to)

        with self.assertRaises(Exception):
            wrong_tx_to = "0x123"
            verify_proxy_factory_address(
                src_chain_id, dst_chain_ids, wrong_tx_to
            )


if __name__ == "__main__":
    unittest.main()
