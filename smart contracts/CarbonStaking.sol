// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CarbonStaking {

    // Adresse du propriétaire
    address private _owner;

    // Référence au contrat CarbonToken
    IERC20 public carbonToken;

    struct StakeInfo {
        uint256 stakedAmount;
        uint256 stakingStart;
    }

    // Mapping des informations de staking par utilisateur
    mapping(address => StakeInfo) private stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Modificateur pour les fonctions réservées au propriétaire
    modifier onlyOwner() {
        require(msg.sender == _owner, "Seul le proprietaire peut executer cette fonction");
        _;
    }

    // Constructeur
    constructor(address _carbonToken) {
        require(_carbonToken != address(0), "Adresse du token invalide");
        _owner = msg.sender;
        carbonToken = IERC20(_carbonToken);
    }

    // Fonction pour staker des crédits carbone
    function stake(uint256 amount) external {
        require(amount > 0, "Le montant doit etre superieur a zero");
        require(carbonToken.balanceOf(msg.sender) >= amount, "Solde insuffisant pour staking");

        // Transfert des crédits carbone vers le contrat
        carbonToken.transferFrom(msg.sender, address(this), amount);

        // Mise à jour des informations de staking
        stakes[msg.sender].stakedAmount += amount;
        stakes[msg.sender].stakingStart = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Fonction pour unstaker des crédits carbone
    function unstake(uint256 amount) external {
        require(amount > 0, "Le montant doit etre superieur a zero");
        require(stakes[msg.sender].stakedAmount >= amount, "Montant stake insuffisant");

        // Mise à jour des informations de staking
        stakes[msg.sender].stakedAmount -= amount;

        // Rendre les crédits carbone à l'utilisateur
        carbonToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Fonction pour obtenir le solde staké d'un utilisateur
    function getStakedBalance(address user) external view returns (uint256) {
        return stakes[user].stakedAmount;
    }

    // Fonction pour obtenir l'adresse du propriétaire
    function owner() external view returns (address) {
        return _owner;
    }
}
