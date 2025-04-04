import json
import random
from typing import List, Optional
from models import Deal, Account, AccountManager

class DataManager:
    def __init__(self, data_file: str):
        with open(data_file, 'r') as f:
            self.data = json.load(f)
        
        self.account_managers = [AccountManager(**am) for am in self.data['account_managers']]
        self.accounts = [Account(**acc) for acc in self.data['accounts']]
        self.deals = [Deal(**deal) for deal in self.data['deals']]

    def get_random_account_manager(self) -> AccountManager:
        return random.choice(self.account_managers)

    def get_manager_accounts(self, manager_id: str) -> List[Account]:
        manager = next((am for am in self.account_managers if am.id == manager_id), None)
        if not manager:
            return []
        return [acc for acc in self.accounts if acc.id in manager.accounts]

    def get_account_deals(self, account_id: str) -> List[Deal]:
        return [deal for deal in self.deals if deal.account_id == account_id]

    def get_manager_total_deals(self, manager_id: str) -> float:
        manager_accounts = self.get_manager_accounts(manager_id)
        account_ids = [acc.id for acc in manager_accounts]
        return sum(deal.value for deal in self.deals if deal.account_id in account_ids) 