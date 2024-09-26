def main():
    # 預設匯率
    exchange_rates = {
        'USD': 0.032,  # 美元
        'EUR': 0.027,  # 歐元
        'JPY': 3.5     # 日圓
    }

    # 提示使用者輸入台幣金額
    try:
        twd_amount = float(input("請輸入台幣金額: "))
    except ValueError:
        print("請輸入有效的數字")
        return

    # 提示使用者選擇幣別
    print("請選擇幣別:")
    print("1. 美元 (USD)")
    print("2. 歐元 (EUR)")
    print("3. 日圓 (JPY)")
    choice = input("請輸入選擇 (1/2/3): ")

    # 根據選擇的幣別計算兌換金額
    if choice == '1':
        currency = 'USD'
    elif choice == '2':
        currency = 'EUR'
    elif choice == '3':
        currency = 'JPY'
    else:
        print("無效的選擇")
        return

    # 計算兌換金額
    exchange_amount = twd_amount * exchange_rates[currency]
    print(f"兌換後的金額為: {exchange_amount:.2f} {currency}")

if __name__ == "__main__":
    main()