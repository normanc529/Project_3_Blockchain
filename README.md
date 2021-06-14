# From Farm to Blockchain to Table
![image](https://user-images.githubusercontent.com/75395061/119927305-0cdad180-bf2e-11eb-8169-51794458f3ad.png)


## Overview of Project
goals/purpose of project
what we are trying to solve/improve

This project uses Smart Contracts created to track and verify orders for Supply Chain Management. The intent is to improve transparency through easily verifiable records on immutable blockchain technology that will match up with company ledgers/invoices for a smoother experience. 

Orders are created as tokenized ERC721 standardized NFT tokens that can be tracked and passed onto the next in line in the supply chain which are manageable through barcodes generated along each step. These in turn give all parties access to tracking the update of information every time it is updated.

Example video on a run through of the front end Heroku deployed website on harvestblocks.com can be found in the resources folder!

Please navigate to https://github.com/Sprutton/harvestblocks to view the repository for our front end code. This code was used to build the Django Harvestblocks site we used for our marketplace portion of the project.

## Technologies Used
Solidity

Web3

Python

Streamlit

Ganache

Django

Heroku

## How to use
note: When deploying Solidity contract through Remix IDE, use HTTP connection instead of HTTPS!

Hook up .env file with pinata API key, pinata secret API key, IP address of Ganache Test Network, and address to the smart contract from Solidity
![image](https://user-images.githubusercontent.com/75395061/121796832-d90bd700-cbd0-11eb-99be-37969ec84f51.png)


Connect to Ganache Test Network 
![image](https://user-images.githubusercontent.com/75395061/121796711-0dcb5e80-cbd0-11eb-8f72-5df5df7e8fd9.png)


Link up Solidity contract to Ganache Test Network with Metamask (Google Chrome Plug-in)
![image](https://user-images.githubusercontent.com/75395061/121796734-34899500-cbd0-11eb-90f0-552080286d10.png)


Compile Solidity contract through Remix IDE with version ^0.5.17+
![image](https://user-images.githubusercontent.com/75395061/121796691-ed030900-cbcf-11eb-88c6-918a563070c2.png)


Deploy Solidity contract to the injected Web3 connection created through Ganache/Metamask
![image](https://user-images.githubusercontent.com/75395061/121796775-774b6d00-cbd0-11eb-8d7d-66776f5f34c7.png)


Run app.ipfs.py through streamlit to test frontend capabilities of initiating the smart contract in a user friendly format
Order info is  to be filled in here, and uploaded image is intended for barcode retrieved from heroku/barcode generating section
The jpg in the image below is a placeholder for the barcode
![image](https://user-images.githubusercontent.com/75395061/121796865-1d977280-cbd1-11eb-86de-7c1fcef429a5.png)


Orders can be Appended in the section below
![image](https://user-images.githubusercontent.com/75395061/121796893-66e7c200-cbd1-11eb-95e9-8750e36ba49c.png)


Appended history of Orders can be viewed 
![image](https://user-images.githubusercontent.com/75395061/121796908-87b01780-cbd1-11eb-810b-5083c54d863a.png)
![image](https://user-images.githubusercontent.com/75395061/121796922-ad3d2100-cbd1-11eb-878c-5a38f7bfd0b7.png)


Pinata pins of the appended orders can be found on the site as well
![image](https://user-images.githubusercontent.com/75395061/121796957-e9708180-cbd1-11eb-8783-12d648d59259.png)
![image](https://user-images.githubusercontent.com/75395061/121796970-f9886100-cbd1-11eb-8e2c-a458e48a0a03.png)


## Contributors
Norman Chen - normanc529@gmail.com

Sam Prutton - samprutton@gmail.com

Peter St.Geme - pstgeme@udel.edu

Wynham Guillemot - wynhamg@gmail.com
