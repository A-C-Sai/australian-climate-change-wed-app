# GUIDE TO PROJECT

## 1. Create a project folder & virtual environment

- Hopefully you go anaconda distribution installed
- Create a project folder
- Open terminal and navigate to your project folder and then type the command below to create a virtual environment. You give you virtual environment any name but best if it doesn't have any spaces. If it does, you can enclose it in quotation marks. Make sure you provide the python version installed on your device.

```bash
    conda create -p my_venv python=3.12 -y
```

- Once created you will automatically be prompted to actived the newly created virtual environment, code to do so will also be provided.

```bash
    conda activate Desktop/projects/my_venv
```

- Once activated you should see you the path to your virtual environment for each prompt. If not you can re-run the conda activate command. You can also verify the creation of the virtual environment using the below command. "\*" indicated the environment you are currently working in.

```bash
    conda env list
```

- now you can open from vscode

```bash
    code .
```

---

## 2. Installing project requirements

- `requirements.txt` contains all the libraries used for this project, install them using the following command in your vscode terminal, MAKE SURE YOUR VIRTAL ENVIRONMENT IS ACTIVATED!.

```bash
    pip3 install -r requirements.txt
```

---

## 3. File Structure

- Below is the expected initial file structure, please only create the folders mentioned. If not mentioned it means these files/ folders will be created during the execution of the project.

```
PROJECT FOLDER
|   app.py
|   requirements.txt
|   README.md
|
|-------- datasets
|            |      climate.db (created automatically during project execution)
|            |      schema.sql
|            |
|            |-------- original (please create this folder)
|            |
|            |
|            |
|            |-------- final_datasets (please create this folder)
|
|
|
|------- notebooks
|
|
|
|------- static
|            |
|            |------ css
|            |------- js
|            |------- imgs
|
|
|
|------- templates
|
|
|
|------- <you_virtual_environment_folder>
```

---

# 4. Where to begin?

- Iavigate to the notebooks folder and execute each notebook in order to prepare data and create the database.

- `app.py` is the brains of the web application

- In terminal type the following command to load and start using the web application. Click the link shown and the application should open in your browser.

```bash
    python3 app.py
```
