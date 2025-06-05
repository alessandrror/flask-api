import os
from pathlib import Path

PROJECT_NAME = "FLASK-API"

LIST_FILES = [
    "Dockerfile",
    ".env",
    ".env.example",
    "app.py",
    "README.md",
    ".editorconfig",
    "requirements.txt",
    # tests folder
    "tests/__init__.py",
    # source folder
    "src/__init__.py",
    # constants folder
    "src/constants/__init__.py",
    # config folder
    "src/config/__init__.py",
    "src/config/config.py",
    "src/config/develpoment.py",
    "src/config/production.py",
    # routes
    "src/routes/__init__.py",
    "src/routes/auth_route.py",
    # middlewares
    "src/middlewares/__init__.py",
    "src/middlewares/auth_middleware.py",
    # controllers
    "src/controllers/__init__.py",
    "src/controllers/auth_controller.py",
    # models
    "src/models/__init__.py",
    "src/models/user_model.py",
    # services
    "src/services/__init__.py",
    "src/services/jwt_service.py",
    "src/services/auth_service.py",
    # schemas
    "src/schemas/__init__.py",
    "src/schemas/auth_schema.py",
    # helpers
    "src/helpers/__init__.py",
    # routes and utils
    "src/utils.py",
]

for file_path in LIST_FILES:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    # make dir
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        print(f"Creating Directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
        print(f"Creating an empty file: {file_path}")
    else:
        print(f"File already exists {file_path}")
