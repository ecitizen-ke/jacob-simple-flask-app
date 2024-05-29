from flask import jsonify

def view_products(myapp):
     @myapp.route("/products")
     def view_products():
             product_list = [{"fruits":["Apple","Guava","Mango"]},{"beverages":["Water","Soda"]}]
        
             return jsonify(product_list)