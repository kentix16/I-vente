import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


#l=[input() for _ in range((int(input())))]
emails = ["user@gmail.com", "invalid-email", "test@yahoo.fr"]
valid_emails = "@" in email for email in emails
print(valid_emails)