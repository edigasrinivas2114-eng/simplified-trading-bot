from logger import logger


class BasicBot:
    def __init__(self):
        logger.info("Trading Bot initialized in SAFE MODE")
        print("Trading Bot running in SAFE MODE (no real orders)")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        order = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price,
            "status": "SIMULATED"
        }

        logger.info(f"Order simulated: {order}")
        return order


def main():
    bot = BasicBot()

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY / SELL): ").upper()
    order_type = input("Order type (MARKET / LIMIT): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Limit price: "))

    order = bot.place_order(symbol, side, order_type, quantity, price)

    print("\n✅ Order Result")
    for k, v in order.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
