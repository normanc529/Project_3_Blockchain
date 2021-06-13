import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

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
    with open(Path('./Resources/abi_ipfs.json')) as f: 
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
# Helper functions to pin files and json to Pinata
################################################################################


def pin_order(customerName, order_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(order_file.getvalue())

    # Build a token metadata file for the order
    token_json = {
        "name": customerName,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash


def pin_order_report(report_content):
    json_report = convert_data_to_json(report_content)
    report_ipfs_hash = pin_json_to_ipfs(json_report)
    return report_ipfs_hash



################################################################################
accounts = w3.eth.accounts
account = accounts[0]
################################################################################

# this section is for the registering of an initial order onto the chain
# we upload our ipfs file here and save it through the pinata api

st.markdown("## ORDERS PAGE")

address = st.selectbox("Select Order Account", options =accounts)

customerName = st.text_input("Your Name/Company Name")          ###
productType = st.text_input("What Product are you Buying?")
initialProductAmount = st.text_input("How Many are you Buying?")

# upload the barcode jpg/png image here
file = st.file_uploader("Upload Order Barcode", type=["jpg", "jpeg", "png"])

if st.button("Register Order"):



    order_ipfs_hash = pin_order(customerName, file)
    tokenURI = f"ipfs://{order_ipfs_hash}"




    tx_hash = contract.functions.registerOrder(
        address,
        customerName,               ####
        productType,
        int(initialProductAmount),
        tokenURI
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

    st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
    st.markdown(f"[Order IPFS Gateway Link](https://ipfs.io/ipfs/{order_ipfs_hash})")

st.markdown("---")

#################################################################################
# Append to Orders
################################################################################
st.markdown("## Append to Order")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose an Order Token ID", list(range(tokens)))
new_order_value = st.text_input("Enter the new order amount")
order_report_content = st.text_area("Enter details for the Order Report")
if st.button("Append to Order"):

    # Use Pinata to pin an order report for the report URI
    order_report_ipfs_hash =  pin_order_report(order_report_content)
    report_uri = f"ipfs://{order_report_ipfs_hash}"

    # Use the token_id and the report_uri to record the order 
    tx_hash = contract.functions.newOrder(
        token_id,
        int(new_order_value),
        report_uri
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")


################################################################################
# Get Appended Order History
################################################################################
st.markdown("## Get the Appended Order History")
order_token_id = st.number_input("Order ID", value=0, step=1)
if st.button("Get Order Reports"):
    order_filter = contract.events.Order.createFilter(
        fromBlock=0, argument_filters={"token_id": order_token_id}
    )
    reports = order_filter.get_all_entries()
    if reports:
        for report in reports:
            report_dictionary = dict(report)
            st.markdown("### Order Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Pinata IPFS Report URI")
            report_uri = report_dictionary["args"]["reportURI"]
            report_ipfs_hash = report_uri[7:]
            st.markdown(
                f"The report is located at the following URI: "
                f"{report_uri}"
            )
            st.write("You can also view the report URI with the following ipfs gateway link")
            st.markdown(f"[IPFS Gateway Link](https://ipfs.io/ipfs/{report_ipfs_hash})")
            st.markdown("### Appraisal Event Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This order has no new appends")
