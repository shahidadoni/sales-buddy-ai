import os
from data_manager import DataManager
from bedrock_helper import BedrockHelper
from tabulate import tabulate

def print_welcome_message(manager_name: str):
    print("\n" + "="*50)
    print(f"Welcome to Sales Buddy, {manager_name}!")
    print("="*50)
    print("\nSample questions you can ask:")
    print("1. What is my highest value deal?")
    print("2. Which account has the most potential for cloud migration?")
    print("3. What services should I pitch to TechCorp Solutions?")
    print("4. Show me all my accounts and their pain points")
    print("5. What is my total deal value across all accounts?")
    print("\nType 'exit' to quit")
    print("="*50 + "\n")

def main():
    # Initialize components
    data_manager = DataManager("data/sales_data.json")
    bedrock = BedrockHelper()

    # Assign random account manager for this session
    current_manager = data_manager.get_random_account_manager()
    print_welcome_message(current_manager.name)

    while True:
        try:
            user_input = input("\nWhat would you like to know? > ")
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Sales Buddy. Goodbye!")
                break

            # Get context for the current manager
            manager_accounts = data_manager.get_manager_accounts(current_manager.id)
            context = {
                "current_manager": {
                    "id": current_manager.id,
                    "name": current_manager.name
                },
                "accounts": [
                    {
                        "id": acc.id,
                        "name": acc.name,
                        "industry": acc.industry,
                        "tech_stack": acc.current_tech_stack,
                        "pain_points": acc.pain_points,
                        "deals": [vars(deal) for deal in data_manager.get_account_deals(acc.id)]
                    }
                    for acc in manager_accounts
                ]
            }

            # Get response from Bedrock
            response = bedrock.generate_response(context, user_input)
            print("\nSales Buddy:", response)

        except KeyboardInterrupt:
            print("\nExiting Sales Buddy...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main() 