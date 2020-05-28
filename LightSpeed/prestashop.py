import requests

def get(ps):
    url = rf"{ps['base']}{ps['ressource']}?ws_key={ps['ws_key']}&output_format={ps['format']}&display=full&filter[{ps['search_field']}]{ps['search_operator']}[{ps['search_value']}]{ps['search_option']}"
    r = requests.get(url)
    r = r.json()
    return r


def get_customer(order_id):
    ps = {}
    ps['base'] = 'https://www.boutiquechapman.com/api/'
    ps['ws_key'] = 'SD9CMBSQDMLLE2CJ3Q8BL1V99GBXA9P3'
    ps['format'] = 'JSON'
    ps['ressource'] = 'customers'
    ps['search_field'] = 'id'
    ps['search_value'] = order_id
    ps['search_option'] = ''
    ps['search_operator'] = '='
    customer = get(ps)
    return customer['customers'][0]


def get_address(address_id):
    ps = {}
    ps['base'] = 'https://www.boutiquechapman.com/api/'
    ps['ws_key'] = 'SD9CMBSQDMLLE2CJ3Q8BL1V99GBXA9P3'
    ps['format'] = 'JSON'
    ps['ressource'] = 'addresses'
    ps['search_field'] = 'id'
    ps['search_value'] = address_id
    ps['search_option'] = ''
    ps['search_operator'] = '='
    address = get(ps)
    return address['addresses'][0]


def get_order():
    ps = {}
    ps['base'] = 'https://www.boutiquechapman.com/api/'
    ps['ws_key'] = 'SD9CMBSQDMLLE2CJ3Q8BL1V99GBXA9P3'
    ps['format'] = 'JSON'
    ps['ressource'] = 'orders'
    ps['search_field'] = 'display=full&filter[date_add]=>[2020-05-25 00:00:00]&date=1'
    ps['search_field'] = 'date_add'
    ps['search_operator'] = '=>'
    ps['search_value'] = '2020-05-24 00:00:00'
    ps['search_option'] = '&date=1'
    orders = get(ps)
    return orders['orders']


def get_order_rows(order):
    return order['associations']['order_rows']


def get_order_data():
    orders = get_order()

    items = []

    for order in orders:


        customer = get_customer(order['id_customer'])
        address = get_address(order['id_address_delivery'])

        item = {}

        item['id'] = order['id']
        item['date'] = order['invoice_date']
        item['total'] = order['total_paid']
        item['customer_firstname'] = customer['firstname']
        item['customer_lastname'] = customer['lastname']

        item['address'] =  address['address1']
        item['email'] = customer['email']

        item['items'] = []


        order_rows = get_order_rows(order)
        for row in order_rows:
            itemDetail = {}

            itemDetail['id'] = row['product_id']
            itemDetail['ref'] = row['product_ean13']
            itemDetail['name'] = row['product_name']
            itemDetail['price'] = row['unit_price_tax_excl']
            itemDetail['qty'] = row['product_quantity']

            item['items'].append(itemDetail)

        items.append(item)

    return items



