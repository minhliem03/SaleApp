def load_categories():
    return [{
        'id': 1,
        'name': 'Di động'
    }, {
        'id': 2,
        'name': 'Laptop'
    }]

def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'Samsung Galaxy Fold5',
        'price': '51.990.000',
        'image': 'https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/a/m/amsung-galaxy-z-fold-5-1tb.png'
    }, {
        'id': 2,
        'name': 'iPhone 15 Pro Max',
        'price': '46.990.000',
        'image': 'https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-256gb_1.png'
    }, {
        'id': 3,
        'name': 'OPPO Find N3 5G',
        'price': '44.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/302953/oppo-find-n3-vang-dong-thumb-600x600.jpg'
    }, {
        'id': 4,
        'name': 'iPhone 15 Plus',
        'price': '34.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/281570/iphone-15-hong-thumb-1-600x600.jpg'
    }, {
        'id': 5,
        'name': 'OPPO Find X5 Pro 5G',
        'price': '32.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/250622/oppo-find-x5-pro-trang-thumb-1-600x600.jpg'
    }, {
        'id': 6,
        'name': 'ASUS ROG Phone 7 Ultimate',
        'price': '29.990.000',
        'image': 'https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/_/1_365-doc-quyuen.jpg'
    }, {
        'id': 7,
        'name': 'Samsung Galaxy Z Flip5',
        'price': '25.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/299250/samsung-galaxy-z-flip5-xanh-mint-thumb-600x600.jpg'
    }, {
        'id': 8,
        'name': 'Nubia Red Magic 6 Pro',
        'price': '19.990.000',
        'image': 'https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/_/s_4_1.png'
    }, {
        'id': 9,
        'name': 'Xiaomi 13T Pro 5G',
        'price': '15.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/309816/xiaomi-13t-xanh-thumb-1-600x600.jpg'
    }, {
        'id': 10,
        'name': 'Realme 11 Pro+ 5G',
        'price': '14.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/309821/realme-11-pro-plus-5g-thumb-600x600.jpeg'
    }, {
        'id': 11,
        'name': 'Realme 10',
        'price': '6.390.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/42/292672/realme-10-thumb-1-600x600.jpg'
    }]
    #     'id': 4,
    #     'name': 'Xiaomi 13T Pro 5G',
    #     'price': '15.990.000',
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/309816/xiaomi-13t-xanh-thumb-1-600x600.jpg'
    # },  {
    #     'id': 5,
    #     'name': 'Realme 11 Pro+ 5G',
    #     'price': '14.990.000',
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/309821/realme-11-pro-plus-5g-thumb-600x600.jpeg'
    # },   {
    #     'id': 6,
    #     'name': 'Realme 10',
    #     'price': '6.390.000',
    #     'image': 'https://cdn.tgdd.vn/Products/Images/42/292672/realme-10-thumb-1-600x600.jpg'
    # }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products