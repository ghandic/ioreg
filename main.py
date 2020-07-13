from utils import IOReg

if __name__ == "__main__":
    info = IOReg.to_dict(options=["-rlk", "BatteryPercent"])
    for product in info:
        print(f"Product '{product['Product']}' has {product['BatteryPercent']}% charge")
