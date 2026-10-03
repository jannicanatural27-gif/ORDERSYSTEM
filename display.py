import os
from menu_data import MENU


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def print_menu():
  print("\n----------------- OUR MENU -----------------")
  print(f"{'Code':<6} {'Item Name':<22} {'Price':>10}")
  print("-" * 45)
  for code, item in MENU.items():
    print(f"[{code}]    {item['name']:<22} ${item['price']:>7.2f}")
  print("-" * 45)


def print_receipt(order_items, subtotal, discount, final_total):
  clear_screen()
  print("=" * 45)
  print("              BYTES & BITES                 ")
  print("=" * 45)
  print(f"{'QTY':<4} {'ITEM':<20} {'PRICE':>8} {'TOTAL':>9}")
  print("-" * 45)

  for item in order_items:
    print(
        f"{item['quantity']:<4} {item['name']:<20} ${item['price']:>7.2f}"
        f" ${item['total']:>8.2f}"
    )

  print("-" * 45)
  print(f"{'Subtotal:':<32} ${subtotal:>9.2f}")
  if discount > 0:
    print(
        f"{'Discount (10% off >$20):':<32}"
        f" -${(subtotal * discount):>8.2f}"
    )
  print(f"{'TOTAL:':<32} ${final_total:>9.2f}")
  print("=" * 45 + "\n")