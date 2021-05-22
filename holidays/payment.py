import razorpay
client = razorpay.Client(
    auth=("rzp_test_ohASjZactVTRw1", "KZYl8XfZRRCREYkAXo8gxs6e"))


def payment_transaction(request, amount, currency):
    order_amount = amount
    order_currency = currency
    order_receipt = 'order_rcptid_11'
    response = client.order.create(amount=order_amount,
                                   currency=order_currency, receipt=order_receipt)
    return response
