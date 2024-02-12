import re

api_response = 

#regex expression for IP addresses
ip_address_pattern = r'"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"'
ip_addresses = re.findall(ip_address_pattern, api_response)

print("IP Addresses:", ip_addresses)

