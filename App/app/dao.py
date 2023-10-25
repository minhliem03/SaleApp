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
        'name': 'iPhone 15',
        'price': 30000000,
        'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png'
    }, {
        'id': 2,
        'name': 'Galaxy ZFold 5',
        'price': 50000000,
        'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png'
    },  {
        'id': 3,
        'name': 'Oppo Reno 6',
        'price': 15000000,
        'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png'
    },  {
        'id': 4,
        'name': 'Google Pixel 3',
        'price': 70000000,
        'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png'
    },  {
        'id': 5,
        'name': 'Galaxy S23 Ultra',
        'price': 35000000,
        'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png'
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products


