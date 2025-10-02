1. Open a folder where you want to create your project.
2. Open terminal in VS Code (Ctrl + `).
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install FastAPI and Uvicorn and pydantic:
   ```
   pip install fastapi uvicorn pydantic
   ```


6. (Optional) Test the installation by creating a simple FastAPI app:
   - Create a file named `main.py` with the following content:
     ```python
     from fastapi import FastAPI

     app = FastAPI()

     @app.get("/")
     def read_root():
         return {"Hello": "World"}
         
     ```
   - Run the app using Uvicorn:
     ```
     uvicorn main:app --reload
     ```
   - Open your browser and navigate to `http://localhost:8000/docs` to see the interactive API documentation.