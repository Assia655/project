// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract CarbonAccount {

    // Propriétaire du contrat
    address private _owner;

    // Struct pour stocker les informations d'un utilisateur
    struct User {
        address walletAddress;
        uint256 totalCarbonCredits;
    }

    // Mapping pour lier un utilisateur à ses informations
    mapping(address => User) private users;

    // Event pour l'enregistrement d'un utilisateur
    event UserRegistered(address indexed user, address walletAddress);
    
    // Event pour l'association du portefeuille avec un utilisateur
    event WalletLinked(address indexed user, address walletAddress);

    // Event pour l'ajout de crédits carbone à un utilisateur
    event CarbonCreditsAdded(address indexed user, uint256 amount);

    // Modificateur pour vérifier que l'appelant est le propriétaire
    modifier onlyOwner() {
        require(msg.sender == _owner, "Seul le proprietaire peut executer cette fonction");
        _;
    }

    // Constructeur de CarbonAccount
    constructor() {
        _owner = msg.sender; // Définir l'adresse qui déploie le contrat comme propriétaire
    }

    // Fonction pour enregistrer un utilisateur et initialiser son portefeuille de crédits carbone
    function registerUser(address user) external onlyOwner {
        require(users[user].walletAddress == address(0), "L'utilisateur est deja enregistre");

        // Initialiser les crédits carbone à 0 et l'adresse du portefeuille à zéro
        users[user] = User({
            walletAddress: address(0),
            totalCarbonCredits: 0
        });

        // Émettre l'événement UserRegistered
        emit UserRegistered(user, address(0));  // Émission de l'événement avec adresse du portefeuille à zéro
    }

    // Fonction pour associer un portefeuille Ethereum à un utilisateur
    function linkWallet(address user, address walletAddress) external onlyOwner {
        require(users[user].walletAddress == address(0), "Portefeuille deja lie");

        // Associer le portefeuille à l'utilisateur
        users[user].walletAddress = walletAddress;

        emit WalletLinked(user, walletAddress);
    }

    // Fonction pour obtenir les détails d'un utilisateur
    function getUserDetails(address user) external view returns (address walletAddress, uint256 totalCarbonCredits) {
        require(users[user].walletAddress != address(0), "Utilisateur non trouve");

        // Retourner l'adresse du portefeuille et le nombre de crédits carbone
        return (users[user].walletAddress, users[user].totalCarbonCredits);
    }

    // Fonction pour créditer des crédits carbone à un utilisateur
    function creditCarbon(address user, uint256 amount) external onlyOwner {
        require(users[user].walletAddress != address(0), "Utilisateur non enregistre");

        // Ajouter les crédits carbone à l'utilisateur
        users[user].totalCarbonCredits += amount;

        // Emission de l'événement
        emit CarbonCreditsAdded(user, amount);
    }

    // Fonction pour vérifier les crédits carbone d'un utilisateur
    function getUserCarbonBalance(address user) external view returns (uint256) {
        return users[user].totalCarbonCredits;
    }

    // Fonction pour obtenir l'adresse du propriétaire
    function owner() external view returns (address) {
        return _owner;
    }

    // Fonction pour transférer la propriété à une autre adresse
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Le nouvel proprietaire ne peut pas etre l'adresse zero");
        _owner = newOwner;
    }
}
