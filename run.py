from flask import Flask,jsonify
from app.users import view_users
from app.products import view_products

app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>hello World</h2>"

view_users(app)
view_products(app)
# @app.route("/users")
# def users():
    # credentials = [
    #     {"username" : "admin",
    #     "password" : "2345"}
        
    # ]
    
    # return jsonify(credentials)

# @app.route("/products")
# def products():
#     product_list = [
#         {"fruits":["Apple","Guava","Mango"]},
#         {"beverages":["Water","Soda"]}
            
#     ]
#     return jsonify(product_list)

if __name__ == "__main__":
    app.run(debug=True)