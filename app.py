from flask import Flask, request, jsonify
from flask import render_template 

app = Flask(__name__)

@app.route("/")
def frontend():
    return render_template("index.html")
    
@app.route("/")
def home():
    return "Hello, Flask! Welcome to Session 1."

@app.route("/about")
def about():
    return "This is the About page"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}!"

@app.route("/json")
def json_response():
    return {"status": "success", "message": "This is JSON!"}

tasks = []   # cada tarea será un diccionario: {"id": 0, "content": "texto"}

users = []   # cada usuario: {"id": 0, "name": "...", "lastname": "...", "address": {"city": "...", "country": "...", "code": "..."}}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_one_user(user_id):
    if user_id < 0 or user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user": users[user_id]})

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    
    # Validar que exista el objeto
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Validar campos obligatorios
    required_fields = ["name", "lastname", "address"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
    
    # Validar que name y lastname no estén vacíos
    name = data["name"]
    lastname = data["lastname"]
    if not name or name.strip() == "":
        return jsonify({"error": "Name cannot be empty"}), 400
    if not lastname or lastname.strip() == "":
        return jsonify({"error": "Lastname cannot be empty"}), 400
    
    # Validar address (debe ser dict y tener city, country, code)
    address = data["address"]
    if not isinstance(address, dict):
        return jsonify({"error": "Address must be an object"}), 400
    
    required_address = ["city", "country", "code"]
    for field in required_address:
        if field not in address:
            return jsonify({"error": f"Missing address field: {field}"}), 400
    
    city = address.get("city", "")
    country = address.get("country", "")
    code = address.get("code", "")
    if not city or city.strip() == "":
        return jsonify({"error": "City cannot be empty"}), 400
    if not country or country.strip() == "":
        return jsonify({"error": "Country cannot be empty"}), 400
    if not code or code.strip() == "":
        return jsonify({"error": "Postal code cannot be empty"}), 400
    
    # Crear usuario
    user = {
        "id": len(users),
        "name": name.strip(),
        "lastname": lastname.strip(),
        "address": {
            "city": city.strip(),
            "country": country.strip(),
            "code": code.strip()
        }
    }
    users.append(user)
    return jsonify({"message": "User created", "user": user}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id < 0 or user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Actualizar name
    if "name" in data:
        new_name = data["name"]
        if not new_name or new_name.strip() == "":
            return jsonify({"error": "Name cannot be empty"}), 400
        users[user_id]["name"] = new_name.strip()
    
    # Actualizar lastname
    if "lastname" in data:
        new_lastname = data["lastname"]
        if not new_lastname or new_lastname.strip() == "":
            return jsonify({"error": "Lastname cannot be empty"}), 400
        users[user_id]["lastname"] = new_lastname.strip()
    
    # Actualizar address (puede venir parcial o completo)
    if "address" in data:
        addr = data["address"]
        if not isinstance(addr, dict):
            return jsonify({"error": "Address must be an object"}), 400
        
        # Actualizar city
        if "city" in addr:
            new_city = addr["city"]
            if not new_city or new_city.strip() == "":
                return jsonify({"error": "City cannot be empty"}), 400
            users[user_id]["address"]["city"] = new_city.strip()
        
        # Actualizar country
        if "country" in addr:
            new_country = addr["country"]
            if not new_country or new_country.strip() == "":
                return jsonify({"error": "Country cannot be empty"}), 400
            users[user_id]["address"]["country"] = new_country.strip()
        
        # Actualizar code
        if "code" in addr:
            new_code = addr["code"]
            if not new_code or new_code.strip() == "":
                return jsonify({"error": "Postal code cannot be empty"}), 400
            users[user_id]["address"]["code"] = new_code.strip()
    
    return jsonify({"message": "User updated", "user": users[user_id]})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id < 0 or user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    removed = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": removed})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    
    # Validación: ¿existe el campo content?
    if not data or "content" not in data:
        return jsonify({"error": "Content field is required"}), 400
    
    content = data.get("content", "")
    
    # Validación: ¿el contenido está vacío o son solo espacios?
    if not content or content.strip() == "":
        return jsonify({"error": "Content cannot be empty"}), 400
    
    # Si pasa validaciones, creamos la tarea
    task = {
        "id": len(tasks),
        "content": content.strip(),  # guardamos sin espacios extra
        "done": False
    }
    tasks.append(task)
    return jsonify({"message": "Task added!", "task": task}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if task_id < 0 or task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404
    
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Validar content si viene en la petición
    if "content" in data:
        new_content = data["content"]
        if not new_content or new_content.strip() == "":
            return jsonify({"error": "Content cannot be empty"}), 400
        tasks[task_id]["content"] = new_content.strip()
    
    # Actualizar done si viene
    if "done" in data:
        # Aseguramos que done sea booleano
        if isinstance(data["done"], bool):
            tasks[task_id]["done"] = data["done"]
        else:
            return jsonify({"error": "done must be a boolean"}), 400
    
    return jsonify({"message": "Task updated!", "task": tasks[task_id]})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404
    removed = tasks.pop(task_id)
    return jsonify({"message": "Task deleted!", "task": removed})

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_one_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": tasks[task_id]})


if __name__ == "__main__":
    app.run(debug=True)