import argparse
import sys


def farmer_market(order_lst):
    """Calculating total price and than subtracting the discounted price to get actual price"""
    price_dict = {"CH1": 3.11, "AP1": 6.00, "CF1": 11.23, "MK1": 4.75, "OM1": 3.69}
    prod_dict = {"CH1": 0, "AP1": 0, "CF1": 0, "MK1": 0, "OM1": 0}
    for obj in order_lst:
        if obj == "CH1":
            prod_dict["CH1"] += 1
        if obj == "AP1":
            prod_dict["AP1"] += 1
        if obj == "CF1":
            prod_dict["CF1"] += 1
        if obj == "MK1":
            prod_dict["MK1"] += 1
        if obj == "OM1":
            prod_dict["OM1"] += 1
    total_price_without_discount_with_product_name = {}
    total_price_without_discount = 0
    discount_price = 0
    for key, value in prod_dict.items():
        for key1, value1 in price_dict.items():
            if key == key1:
                total_price_without_discount_with_product_name[key] = prod_dict[key] * price_dict[key]
                total_price_without_discount += prod_dict[key] * price_dict[key]
    if prod_dict["CH1"] and prod_dict["MK1"] != 0:
        price_of_one_milk = price_dict["MK1"]
        total_price_without_discount = total_price_without_discount - price_of_one_milk
        discount_price = total_price_without_discount

    if prod_dict["AP1"] >= 3:
        total_price_without_discount = total_price_without_discount - prod_dict["AP1"] * 1.50
        discount_price = total_price_without_discount
    if prod_dict["CF1"] > 1:
        quo = prod_dict["CF1"] / 2
        price_of_coffee = quo * price_dict["CF1"]
        total_price_without_discount = total_price_without_discount - price_of_coffee
        discount_price = round(total_price_without_discount, 2)
    if prod_dict["OM1"]:
        price_of_apple = 0.5 * price_dict["AP1"]
        total_price_without_discount = total_price_without_discount - price_of_apple
        discount_price = round(total_price_without_discount, 2)

    if discount_price:
        return discount_price
    else:
        return total_price_without_discount


# def unit_test():
#"""For testing"""
#     order_list = [['CF1', 'CF1', 'CF1', 'AP1'], ['CH1', 'AP1', 'AP1', 'AP1', 'MK1'], ['CH1', 'AP1'],
#                   ['CH1', 'AP1', 'CF1', 'MK1'], ['MK1', 'AP1'], ["AP1", "AP1", "CH1", "AP1"], ['CF1', 'CF1'],
#                   ["AP1", 'OM1', "OM1"]]
#     for test_obj in order_list:
#         p = farmer_market(test_obj)
#         print(p)
# unit_test()


def main():
    """For Taking Arguments from command line and to print help message"""
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('-h',
                        '--help',
                        action='help',
                        help='show this help message and exit'
                        )
    parser.add_argument('-i',
                        '--input',
                        help='input items in this format i.e. CH1,AP1,AP1,AP1,MK1',
                        type=str,
                        )
    args = parser.parse_args()
    if args.input is None:
        parser.error(
            "--input ____[input required]")
        sys.exit(1)
    input_list = args.input.split(",")
    output = farmer_market(input_list)
    print(output)


if __name__ == "__main__":
    main()
