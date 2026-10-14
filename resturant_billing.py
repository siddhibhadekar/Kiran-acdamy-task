
def calculateFoodGST(a, b):
    total = a + b
    return total + (total * 5 / 100)


def calculateDrinksGST(c, d):
    total = c + d
    return total + (total * 10 / 100)


def calculateDessertGST(e):
    return e + (e * 8 / 100)


def totalBill(a, b, c, d, e):
    food = calculateFoodGST(a, b)
    drinks = calculateDrinksGST(c, d)
    dessert = calculateDessertGST(e)

    return food + drinks + dessert


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 10 / 100
    final_amount = total - discount

    print(f"Total after GST = {total:.2f}")
    print(f"Discount = {discount:.2f}")
    print(f"Final payable amount = {final_amount:.2f}")

    return final_amount


# main program
calculateDiscountedBill(200, 150, 100, 50, 100)
