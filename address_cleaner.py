""" Python Script (English Comments) """

import pandas as pd

# Sample dataset representing "dirty" address data from a client
data = {
    'Full_Address': [
        '123 Liberty St, New York, NY 10006',
        '742 Evergreen Terrace, Springfield, IL 62704',
        '1600 Pennsylvania Avenue NW, Washington, DC 20500',
        '450 Serra Mall, Stanford, CA 94305',
        '550 15th St, San Francisco, California',
        '101 Main St, Seattle, WA 98101'
    ]
}

# Load data into a Pandas DataFrame
df = pd.DataFrame(data)

def extract_and_verify_state(address):
    """
    Function to extract and standardize US State abbreviations 
    from a text string.
    """
    # Dictionary for standardizing state names to abbreviations
    state_mapping = {
        "California": "CA",
        "New York": "NY",
        "Illinois": "IL"
    }
    
    # List of common state abbreviations to look for
    states_abbr = ["NY", "IL", "DC", "CA", "WA"]
    
    # Check for full names and convert to abbreviations
    for full_name, abbr in state_mapping.items():
        if full_name in address:
            return abbr
            
    # Check for existing abbreviations
    for abbr in states_abbr:
        if abbr in address:
            return abbr
            
    return "Manual Check Required"

# Apply the function to create a new 'Verified_State' column
df['Verified_State'] = df['Full_Address'].apply(extract_and_verify_state)

# Add a status column for visual confirmation
df['Status'] = 'Verified ✅'

# Display the final clean result
print("--- Processed Data ---")
print(df)

# Export to CSV (optional, for the client to see in Excel)
# df.to_csv('cleaned_addresses.csv', index=False)