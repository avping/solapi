import requests
import json

# Define the RPC endpoint
endpoint = 'https://api.mainnet-beta.solana.com'

# Define the headers for the HTTP request
headers = {"Content-Type": "application/json"}

# Define a method to fetch and print total stake, validator count, block height, slot height, and current epoch
def fetch_solana_details():
    # Fetch stake details
    params_stake = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getStakeActivation",
        "params": ["stake_account_pubkey_here"]  # replace with actual stake account public key
    }
    response_stake = requests.post(endpoint, headers=headers, data=json.dumps(params_stake))
    stake_info = response_stake.json()
    print(f"Total Stake: {stake_info['result']['state']}")

    # Fetch validator details
    params_validators = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getValidators"
    }
    response_validators = requests.post(endpoint, headers=headers, data=json.dumps(params_validators))
    validators_info = response_validators.json()
    print(f"Number of validators: {len(validators_info['result']['current'])}")

    # Fetch epoch info
    params_epoch = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getEpochInfo"
    }
    response_epoch = requests.post(endpoint, headers=headers, data=json.dumps(params_epoch))
    epoch_info = response_epoch.json()
    print(f"Block Height: {epoch_info['result']['blockHeight']}")
    print(f"Slot Height: {epoch_info['result']['slot']}")
    print(f"Current Epoch: {epoch_info['result']['epoch']}")
    print(f"Slot Range: {epoch_info['result']['absoluteSlot']}")
    print(f"Time Remaining in Current Epoch: {epoch_info['result']['slotsInEpoch'] - epoch_info['result']['slotIndex']} slots")

# Call the function
fetch_solana_details()
