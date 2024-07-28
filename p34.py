#WAF to convert USD to INR

usd = float(input("Enter amount in Dollar: "))

def usd_to_inr(usd):
    return usd*83

print("Amount in Rupees :", round(usd_to_inr(usd),2))