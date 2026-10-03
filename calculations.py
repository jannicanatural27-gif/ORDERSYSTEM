def calculate_totals(order_items):
  subtotal = sum(item["price"] * item["quantity"] for item in order_items)
  for item in order_items:
    item["total"] = item["price"] * item["quantity"]

  discount_rate = 0.10 if subtotal >= 20.0 else 0.0
  final_total = subtotal * (1 - discount_rate)
  return subtotal, discount_rate, final_total