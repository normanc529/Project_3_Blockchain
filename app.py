import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))   #ganache IP from env file
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI

# Cache the contract on load
@st.cache(allow_output_mutation=True)              

# Define the load_contract function
def load_contract():
    # Load solidity contract ABI
    with open(Path('./abi.json')) as f: 
        solidity_contract_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=solidity_contract_abi
    )
    # Return the contract from the function
    return contract
# Load the contract
contract = load_contract()

################################################################################
accounts = w3.eth.accounts
account = accounts[0]
################################################################################
st.markdown("## ORDERS PAGE")

address = st.selectbox("Select Order Account", options =accounts)

customerName = st.text_input("Your Name/Company Name")
productType = st.text_input("What Product are you Buying?")
initialProductAmount = st.text_input("How Many are you Buying?")
tokenURI = st.text_input("Enter the URI of the Order")

if st.button("Register Order"):
    tx_hash = contract.functions.registerOrder(
        address,
        customerName,
        productType,
        int(initialProductAmount),
        tokenURI
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.markdown("---")

# ################################################################################
# #place_order = st.text

# print(contract.functions.getInfo()).call())  #calls the getInfo function in solidity contract 

# tx_hash = contract.functions.setInfo('''setInfo parameters here''').transact()

# web3.eth.waitForTransactionReceipt(tx_hash)