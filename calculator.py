def calculate_profit(
    selling_price: float,
    material_cost: float,
    shipping_charged_to_buyer: float,
    actual_shipping_cost: float,
    include_offsite_ads: bool = False,
    listing_fee: float = 0.20
) -> dict:

    # Etsy fees
    transaction_fee = (selling_price + shipping_charged_to_buyer) * 0.065
    payment_processing_fee = (selling_price + shipping_charged_to_buyer) * 0.03 + 0.25
    offsite_ads_fee = selling_price * 0.15 if include_offsite_ads else 0.0

    total_etsy_fees = listing_fee + transaction_fee + payment_processing_fee + offsite_ads_fee

    # Total costs
    total_costs = material_cost + actual_shipping_cost + total_etsy_fees

    # Profit
    net_profit = selling_price - total_costs
    profit_margin = (net_profit / selling_price) * 100 if selling_price > 0 else 0

    # Break-even: what price covers all costs (assuming ~30% margin target)
    # Break-even = total_costs / (1 - etsy_fee_rate)
    etsy_fee_rate = 0.065 + 0.03  # approx combined rate
    break_even_price = (material_cost + actual_shipping_cost + listing_fee + 0.25) / (1 - etsy_fee_rate)

    return {
        "transaction_fee": round(transaction_fee, 2),
        "payment_processing_fee": round(payment_processing_fee, 2),
        "offsite_ads_fee": round(offsite_ads_fee, 2),
        "total_etsy_fees": round(total_etsy_fees, 2),
        "total_costs": round(total_costs, 2),
        "net_profit": round(net_profit, 2),
        "profit_margin": round(profit_margin, 1),
        "break_even_price": round(break_even_price, 2),
    }


def calculate_monthly(result: dict, selling_price: float, units_per_month: int) -> dict:
    return {
        "monthly_revenue": round(selling_price * units_per_month, 2),
        "monthly_fees": round(result["total_etsy_fees"] * units_per_month, 2),
        "monthly_profit": round(result["net_profit"] * units_per_month, 2),
    }

result = calculate_profit(10.44, 5, 5, 4)
print("Per sale:", result)

monthly = calculate_monthly(result, 10.44, 20)
print("Monthly:", monthly)    