# Define the import file and remove list
import_file = "allow_list.txt"

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Read the `allow_list`
with open(import_file, "r") as file:

  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Iterate through the `remove_list`
for element in remove_list:

    # Use the `.remove()` method to remove elements from `ip_addresses`
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert `ip_addresses` to a string so that it can be written into the text file
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:

    # Rewrite the file replacing its content with `ip_addresses`
    file.write(ip_addresses)

# Print the IP addresses to the console
print(ip_addresses)