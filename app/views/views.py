from flask import jsonify
from flask.ext.restful import Resource, abort
from app.models.models import Motherboard, Cpu, Gpu, Case, Hdd, Psu, Memory

__author__ = 'darryl'


class ComponentsApi(Resource):
    product_types = {
        "cpu": Cpu,
        "gpu": Gpu,
        "case": Case,
        "hdd": Hdd,
        "psu": Psu,
        "mem": Memory,
        "mobo": Motherboard
    }

    def get(self, key=None, product_type=None):
        # This will be used by the scraper, to check for existing products
        # And the webapp
        if not product_type:
            abort(404)

        productcollection = self.product_types[product_type]

        if key:
            products = productcollection.objects.get_or_404(_id=key)
        else:
            products = productcollection.objects.all()
        if not products:
            abort(404)

        res = {}
        for product in products:
            res[product._id] = {
                'name': product.name,
                'price': str(product.price),
            }
        return jsonify(res)

