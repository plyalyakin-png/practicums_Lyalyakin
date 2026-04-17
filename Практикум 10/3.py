def cost(start_cost, discount_card, holiday):
    """
    Receive the cost of the goods,
    information about the day and the availability of the discount card,
    return final price.
    """
    end_discount = 0

    if start_cost > 30000:
        end_discount = 10
    elif start_cost > 20000:
        end_discount = 7
    elif start_cost > 15000:
        end_discount = 5
    elif start_cost > 5000:
        end_discount = 3

    if discount_card:
        end_discount += 5

    if holiday:
        end_discount += 3

    end_discount = min(end_discount, 15)

    end_cost = round(start_cost * (1 - end_discount / 100), 2)
    return end_cost
print(cost(25704, False, False))