from libs.openexchange import OpenExchangeClient

USER_CHOICE = """
Enter your choice :
- 'c' to start the converter.
- 'q' to quit.
Your Choice Here : """


def app():
    APP_ID = "3823d6d25f2f4ec5aa471faabbf065fc"

    client = OpenExchangeClient(APP_ID)

    currency_dict = client._get_currencies()
    currency_codes = [currency for currency in currency_dict ]

    from_currency = input("Enter the base currency : ").upper()
    to_currency = input("Enter the currency you wish to convert to : ").upper()

    check1 = from_currency in currency_codes
    check2 = to_currency in currency_codes

    if check1 and check2:
        from_amount = int(input(f"Enter the amount in {from_currency} : "))
        print("\n")
        client.default_rates(from_currency, to_currency)
        print("\n")
        print(f"Converting from {currency_dict[from_currency]} to {currency_dict[to_currency]}.............")
        print("\n")
        client.convert(from_amount, from_currency, to_currency)


    else:
        print("Invalid Currency codes !! Please try again.")


def menu():
    ch = input(USER_CHOICE).lower()

    while ch != 'q':
        app()
        ch = input(USER_CHOICE).lower()
    print("Closing.........")


menu()