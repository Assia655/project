// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

// Importation des contrats ERC-20 depuis OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CarbonToken is ERC20 {

    // Propriétaire du contrat
    address private _owner;

    // Mapping pour suivre les crédits carbone d'un utilisateur
    mapping(address => uint256) private _carbonCredits;

    // Event pour la création de nouveaux crédits carbone
    event Mint(address indexed to, uint256 amount);
    
    // Event pour la destruction de crédits carbone
    event Burn(address indexed from, uint256 amount);

    // Modificateur pour restreindre l'accès à certaines fonctions
    modifier onlyOwner() {
        require(msg.sender == _owner, "Seul le proprietaire peut executer cette fonction");
        _;
    }

    // Constructeur de CarbonToken
    constructor() ERC20("CarbonToken", "CTK") {
        _owner = msg.sender;  // Définir le déployeur comme propriétaire
    }

    // Fonction pour créer des crédits carbone pour un utilisateur
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        _carbonCredits[to] += amount;
        emit Mint(to, amount);
    }

    // Fonction pour transférer des crédits carbone d'un utilisateur à un autre
    function transferCarbon(address to, uint256 amount) external returns (bool) {
        require(_carbonCredits[msg.sender] >= amount, "Pas assez de credits carbone");
        _carbonCredits[msg.sender] -= amount;
        _carbonCredits[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // Fonction pour brûler des crédits carbone (utilisation ou compensation)
    function burn(address from, uint256 amount) external onlyOwner {
        require(_carbonCredits[from] >= amount, "Pas assez de credits carbone");
        _carbonCredits[from] -= amount;
        _burn(from, amount);
        emit Burn(from, amount);
    }

    // Fonction pour vérifier les crédits carbone d'un utilisateur
    function balanceOfCarbon(address user) external view returns (uint256) {
        return _carbonCredits[user];
    }

    // Fonction pour obtenir l'adresse du propriétaire
    function owner() external view returns (address) {
        return _owner;
    }
}
