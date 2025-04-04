# Sales Buddy - Terminal-based Sales Assistant

A terminal-based AI sales assistant that helps account managers query customer and deal information using AWS Bedrock.

## Overview

Sales Buddy is a terminal application that allows account managers to:
- Query their assigned customer accounts
- View deal information
- Get insights about customer pain points
- Receive AI-powered recommendations for service offerings

## Setup

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure AWS credentials:
Create `.env` file in the backend directory: 
```

5. Run the application:
```bash
python src/main.py
```

## Project Structure

## Features

- Random account manager assignment per session
- Access control (managers can only see their assigned accounts)
- AI-powered responses using AWS Bedrock
- Deal and account analytics
- Service recommendations

## Sample Questions

You can ask questions like:
1. "What is my highest value deal?"
2. "Which account has the most potential for cloud migration?"
3. "What services should I pitch to TechCorp Solutions?"
4. "Show me all my accounts and their pain points"
5. "What is my total deal value across all accounts?"

## Dependencies

Required Python packages:
- boto3
- python-dotenv
- tabulate

## Security Notes

- Never commit the `.env` file
- Each account manager can only access their assigned accounts
- AWS credentials should have minimum required permissions

## Usage

1. Start the application:
```bash
python src/main.py
```

2. You'll be randomly assigned an account manager role
3. Ask questions about your accounts and deals
4. Type 'exit' to quit the application

## Data Structure

The application uses:
- Account Managers: Sales representatives with assigned accounts
- Accounts: Customer companies with details and pain points
- Deals: Sales opportunities with values and status