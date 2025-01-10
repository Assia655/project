Blockchain_service/
├── app/
│   ├── __init__.py
│   ├── main.py                # Point d'entrée
│   ├── config.py              # Configurations pour la blockchain et la base de données
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py         # Gestion des sessions DB
│   │   ├── models.py          # Modèles pour les enregistrements blockchain
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── web3_provider.py   # Connexion à la blockchain
│   │   ├── contracts_loader.py # Chargement des ABI des contrats
│   │   └── transaction_helper.py # Gestion des interactions avec la blockchain
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── blockchain.py      
│   ├── services/
│   │   ├── __init__.py
│   │   ├── blockchain.py      # Services d'interaction avec la blockchain
│   │   └── wallet_sync.py     # Synchronisation deswallets
│   └── api/
│       ├── __init__.py
│       └── routes.py          
├── requirements.txt          
├── Dockerfile                 
└── README.md                  
