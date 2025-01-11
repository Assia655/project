// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

// Interface ERC-20 pour l'interopérabilité avec des tokens ERC-20 comme l'USDT ou autres tokens
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CarbonPayment {
    // Propriétaire du contrat
    address private _owner;

    // Mapping pour suivre le solde des crédits carbone des utilisateurs
    mapping(address => uint256) private carbonBalances;

    // Event pour le paiement de crédits carbone
    event CarbonCreditsPurchased(address indexed buyer, uint256 amount, uint256 paymentAmount);
    
    // Event pour la conversion et la création de crédits carbone
    event CarbonCreditsMinted(address indexed user, uint256 fiatAmount, uint256 carbonCredits);

    // Modificateur pour s'assurer que seul le propriétaire peut exécuter certaines fonctions
    modifier onlyOwner() {
        require(msg.sender == _owner, "Seul le proprietaire peut executer cette fonction");
        _;
    }

    // Constructeur pour initialiser le propriétaire
    constructor() {
        _owner = msg.sender; // Le déployeur devient le propriétaire
    }

    // Fonction pour effectuer un paiement en ETH pour acheter des crédits carbone
    function payForCarbonCredits(address to, uint256 amount) external payable {
        require(msg.value > 0, "Le montant du paiement doit etre positif");
        require(amount > 0, "Le montant des credits carbone doit etre positif");

        // Enregistrer le paiement en ETH
        carbonBalances[to] += amount;

        // Émettre l'événement
        emit CarbonCreditsPurchased(to, amount, msg.value);
    }

    // Fonction pour convertir un montant fiat en ETH (approximatif via un taux fixe) et créer des crédits carbone
    function convertAndMint(address user, uint256 fiatAmount) external onlyOwner {
        require(fiatAmount > 0, "Le montant fiat doit etre positif");

        // Conversion approximative 1 ETH = 1000 crédits carbone pour simplifier l'exemple
        uint256 carbonCredits = fiatAmount * 1000; // Le taux de conversion peut être ajusté
        carbonBalances[user] += carbonCredits;

        // Émettre l'événement de création de crédits carbone
        emit CarbonCreditsMinted(user, fiatAmount, carbonCredits);
    }

    // Fonction pour obtenir le solde de crédits carbone d'un utilisateur
    function getCarbonBalance(address user) external view returns (uint256) {
        return carbonBalances[user];
    }

    // Fonction pour récupérer l'adresse du propriétaire
    function owner() external view returns (address) {
        return _owner;
    }

    // Fonction pour transférer la propriété à une autre adresse
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Le nouvel proprietaire ne peut pas etre l'adresse zero");
        _owner = newOwner;
    }

    // Fonction de retrait des fonds par le propriétaire (en ETH)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Solde insuffisant");
        payable(_owner).transfer(amount);
    }
}
