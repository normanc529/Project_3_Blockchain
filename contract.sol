pragma solidity ^0.5.0;

contract ManufacturerRecord {
    
    address     owner = 0x47b05403163c42256BA9CFf51F27cb7250059664; //public key goes here
    bool        isNewAccount = true;                                //checking for repeat creations of this contract
    uint        quantityProduced = 9999;                            //quantity of X item 
    string      manufacturerName = "namehere";                      //name of section of chain producerofrawmaterials/manufacturer/wholesaler/retailer
    string      descriptionOfProduct = "description here";          //description
    
    string messageHere = "";                                        //custom message here
    
    
    function setInfo(

    address newOwner,
    bool newAccountStatus,
    uint newQuantityReceived,
    string memory nextNameInChain,
    string memory newDescriptionOfProduct,
    string memory newMessageHere
    )
    public 
    {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        quantityProduced = newQuantityReceived;
        manufacturerName = nextNameInChain;
        descriptionOfProduct = newDescriptionOfProduct;
        messageHere = newMessageHere;
    }
    
    function getInfo() view public returns(address, bool, uint, string memory, string memory, string memory) //matches number of items below
    {
        return (owner, isNewAccount, quantityProduced, manufacturerName, descriptionOfProduct, messageHere); //matches number of items above
    }
    
}