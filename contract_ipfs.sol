pragma solidity ^0.5.17;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract OrderToken is ERC721Full {
    constructor() public ERC721Full("OrderToken", "ORDR") { }


    struct OrderInfo {
        string customerName;
        string productType;
        uint256 productAmount;
    }
    
    mapping(uint256 => OrderInfo) public orders;
    
    event Order(uint256 token_id, uint256 productAmount, string reportURI);
    
    function registerOrder(
        address owner,
        string memory customerName,
        string memory productType,
        uint256 initialProductAmount,
        string memory tokenURI
        ) public returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);
        orders[tokenId] = OrderInfo(customerName, productType, initialProductAmount);
        return tokenId;
    }
    
    function newOrder(
        uint256 tokenId,
        uint256 newProductAmount,
        string memory reportURI
    ) public returns (uint256) {
        orders[tokenId].productAmount = newProductAmount;
        emit Order(tokenId, newProductAmount, reportURI);
        return orders[tokenId].productAmount;
    }
 }    