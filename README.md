# Minimal Docker + Streamlit App

![](./src/demo.gif)

Welcome to the Minimal Docker + Streamlit App repository! This application serves as an example of how to create a lightweight, containerized Streamlit application. Our project leverages the Gapminder dataset to visually explore the relationship between a country's GDP per capita and life expectancy over time. This use case serves as a perfect demonstration of Streamlit's powerful capability to convert Python scripts into shareable web apps.

Practical Use Case: Data visualization applications like this are incredibly powerful tools in the world of data science and analytics. They enable users to gain a quick and in-depth understanding of the underlying patterns and trends in data. The app we've created here can be used by researchers, analysts, students or anyone interested in exploring socio-economic trends globally. Additionally, the Docker + Streamlit combination provides an efficient way to develop, deploy, and scale Python-based data applications, ensuring consistency across different environments.

---

## Setup

### Environment

1. Install Docker:
   Docker is used to create, deploy, and run applications by using containers. Install Docker from the official site [here](https://www.docker.com/products/docker-desktop).

2. Install Visual Studio Code:
   Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux, and macOS. Install VSCode from the official site [here](https://code.visualstudio.com/download).

3. Install VSCode Extensions:
   - Docker: Makes it easier to create, manage, and debug containerized applications. Install the Docker VSCode extension [here](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker).
   - Dev Containers: Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's full feature set. Install the Dev Containers VSCode extension [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

4. Clone the repository:
```bash
git clone https://github.com/jsulopzs/docker-streamlit-plotly-app.git
```

5. Navigate into the project directory:
```bash
cd docker-streamlit-plotly-app
```

6. Open the project in VSCode:
```bash
code .
```

Your development environment is now set up and you're ready to start using the Minimal Docker + Streamlit App. See the [Usage](#usage) section below to learn how to run the app.

### Launch App

Once you have installed Docker, VSCode and necessary extensions, follow these steps to launch the container:

1. Open the command palette in VSCode. This can be achieved by:
   - On macOS: Pressing `CMD` + `SHIFT` + `P`
   - On Windows: Pressing `CONTROL` + `SHIFT` + `P`

2. Type `Dev Containers: Rebuild and Reopen in Container` in the command palette and hit `ENTER`. This will start the process of building your Docker container based on the specifications in your `devcontainer.json` and `Dockerfile`. 

3. VSCode will then rebuild and launch your Docker container. This process can take a few minutes the first time, as Docker needs to download and install all required dependencies in the Dockerfile. Subsequent launches will be significantly faster.

4. Once the build completes, your VSCode window will reload and connect to the running Docker container. You can confirm this by checking the bottom-left corner of the VSCode window, which should indicate that you're connected to a development container.

---

Your development environment is now set up and you're ready to start using the Minimal Docker + Streamlit App. See the [Usage](#usage) section below to learn how to run the app.


---

## Usage

With the terminal still open in VSCode (You can open it by navigating to Terminal -> New Terminal in the menu, or by using the shortcut `CONTROL`+ `` ` `` ), install the necessary Python dependencies:

```bash
streamlit run app/app_simple.py
```

Create a new terminal and open the other app of the project:

```bash
streamlit run app/app_sidebar.py
```

---

We hope you find this project useful. If you have any questions or if there's anything else we can assist you with, please feel free to open an issue.

---

## Directory Structure

```
Minimal Docker + Streamlit App
│
├── app
│   ├── app_sidebar.py
│   ├── app_simple.py
│   └── requirements.txt
│
├── data
│   └── gampinder.xlsx
│
├── notebooks
│   └── 01_EDA.ipynb
│
└── devcontainer
    ├── Dockerfile
    └── devcontainer.json
```

## Repository Files & Folders Explanation

### `/app`

This is where the application code is located.

* `app_sidebar.py` - This script holds the logic for the sidebar functionality of the application, which allows the user to select different parameters for the data visualization.
* `app_simple.py` - This script is the core of the Streamlit application. It contains the main logic for data loading, processing, and visualization.
* `requirements.txt` - This file lists all of the Python dependencies that are required to run the app.

### `/data`

This folder contains datasets used by the application.

* `gampinder.xlsx` - This is the Gapminder data file that the application uses. It contains historical data on life expectancy, population, and GDP per capita for various countries.

### `/notebooks`

This folder contains Jupyter notebooks.

* `01_EDA.ipynb` - This Jupyter notebook is used for initial exploratory data analysis on the Gapminder dataset.

### `/devcontainer`

This directory contains a Docker configuration file for setting up a development environment.

* `Dockerfile` - This file defines the Docker image used for the Visual Studio Code Remote - Containers extension.
* `devcontainer.json` - This file defines how the dev container should behave.
