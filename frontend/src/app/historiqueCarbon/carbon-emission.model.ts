export interface CarbonEmission {
    price: number;
    price_eth: number | null; // Permettre null ici pour ne provoque pas erreur
    date: string;
    change_percent: string;
  }
  
  