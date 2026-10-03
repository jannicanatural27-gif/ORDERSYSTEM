import sys
from calculations import calculate_totals
from display import clear_screen, print_menu, print_receipt
from menu_data import MENU


def main():
  clear_screen()
  print("=" * 45)
  print("      WELCOME TO BYTES & BITES FAST FOOD     ")
  print("=" * 45)
  print_menu()

  while True:
    choice = input("\nPlace an order? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
      break
    elif choice in ["no", "n"]:
      sys.exit()

  order_items = []
  while True:
    code = input("Enter Item Code (1-6): ").strip()
    if code not in MENU:
      print("Invalid code!")
      continue

    qty = int(input(f"Enter quantity for {MENU[code]['name']}: "))
    order_items.append({
        "name": MENU[code]["name"],
        "price": MENU[code]["price"],
        "quantity": qty,
    })

    if input("Add another item? (yes/no): ").strip().lower() in ["no", "n"]:
      break

  subtotal, discount, final_total = calculate_totals(order_items)
  print_receipt(order_items, subtotal, discount, final_total)


if __name__ == "__main__":
  main()