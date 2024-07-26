# SDSS spectra with peak detection

This development is powered by CONICET-Argentina, Universidad de Mendoza-Argentina and Universidad Tecnológica Narional Regional Mendoza-Argentina.

<Img src="logos/logo_conicet.png" width="108"> <Img src="logos/ibio.jpeg" width="70"> <Img src="logos/logo_um.png" width="70"> <Img src="logos/logoUTN-comprimido.jpg" width="118">

This work was born from sonoUno desktop, maintains its principles, and uses some of its libraries.

## Description



# sonoUno-notebook

This repository contains data, in audio and graphic format, on celestial bodies. Detailed descriptions have been made in Jupyther Notebook.

## How to run the project locally

### Linux

1. Check if pip is installed on your Linux operating system. If not, follow these steps:

    • Update packages:
    ``` sudo apt-get update ```

    • Install pip:
    ``` sudo apt-get install python3-pip ```

2. install the virtual environment (if you don't have it):

    ``` sudo apt install python3-venv ```

3. Create a virtual environment (preferably from your computer's desktop):

    • command to create it:
    ``` python3 -m venv my_env ```

    • command to enter:
    ``` source my_env/bin/activate ```

4. Install inside the virtual environment: Jupyter Notebook

    ``` pip install notebook ```

5. Run Jupyter Notebook from the console:

    ``` jupyter notebook ```

6. The browser opens automatically, if not it uses the default IP 

    ``` 127.0.0.1:8888 ``` or ``` localhost:8888 ```

### Windows

1. We need to have python installed. If you don't have it, you can download the installer at:

    https://www.python.org/downloads/release/python-3123/

2. You need to install pip on windows operating system (you can also install it from python installer)

Another way to install pip on Windows is the following:

We enter the address: 

https://bootstrap.pypa.io/get-pip.py

We save the file get-pip.py . Then, we open the Windows consola (CMD) and we position ourselves in the directory where we save the .py fila. Finally, we execute:

```python get-pip.py```

3. Create a virtual environment (preferably from your computer's desktop):

    • Open CMD and go to the folder where you want to create the virtual environment

    • command to create it:
    ``` python -m venv my_env ```

    • command to enter:
    ``` my_env\Scripts\activate ```

4. Install inside the virtual environment: Jupyter Notebook

    ``` pip install notebook ```

5. Run Jupyter Notebook from the console:

    ``` jupyter notebook ```

6. The browser opens automatically, if not it uses the default IP 

    ```127.0.0.1:8888``` or ```localhost:8888```

### For both operating systems

Go to the notebook folder to run the desired file, from Jupyter Notebook

• In order to run stars.ipynb you need to have the following libraries installed in your virtual environment:

**Numpy**: ```pip install numpy```

**PyGame**: ```pip install pygame```

**Matplotlib**: ```pip install matplotlib```

**Pandas**: ```pip install pandas```

• In order to run SDSS.ipynb you need to have the following libraries installed in your virtual environment:

**Numpy**: ```pip install numpy```

**Matplotlib**: ```pip install matplotlib```

**Pandas**: ```pip install pandas```

# How to contribute to the software 

All help is welcomed and needed!
If you want to contribute contact us at sonounoteam@gmail.com

# Report issues or problems with the software

All people could report a problem opening an issue here on GitHub or contact us by email: sonounoteam@gmail.com
