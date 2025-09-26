import requests

# Replace these with your actual eBay API credentials
EBAY_APP_ID = "YOUR_APP_ID"

# Example: Finding API endpoint
FINDING_API_URL = "https://svcs.ebay.com/services/search/FindingService/v1"

headers = {
    "X-EBAY-SOA-SECURITY-APPNAME": EBAY_APP_ID,
    "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
    "X-EBAY-SOA-REQUEST-DATA-FORMAT": "JSON",
    "Content-Type": "application/json"
}

params = {
    "keywords": "laptop",
    "paginationInput.entriesPerPage": 2,
    "outputSelector": "SellerInfo"
}

response = requests.get(FINDING_API_URL, headers=headers, params=params)

print("Status Code:", response.status_code)
print("Response:", response.text)
