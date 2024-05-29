from flask import jsonify

def view_users(myapp):
    @myapp.route("/users")
    def get_users():
        credentials = [{"username" : "admin","password" : "2345"}]
        return jsonify(credentials)
    

