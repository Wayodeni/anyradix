# anyradix
A simple gui program to translate numbers between radixes from 1 to 36.

**Files description:**
any_radix_backend.py  - contains gui logic class Translator.
any_radix_form.ui  - gui form in qt-designer format.
any_radix_frontend.py  - gui form translated to python.
main.py  - file that binds frontend and backend together. To open a gui start it.

**Installation:**

 1. clone git repository `git clone https://github.com/Wayodeni/anyradix.git`
 2. change working directory to repo root `cd anyradix`
 3. make a virtual environment 
windows: 
`python -m venv venv`
linux: 
`python3 -m venv venv`
 4. activate it  
windows:
`venv\Scripts\activate.bat`
linux:
 `source venv/bin/activate`
 5. install requirements `pip install -r requirements.txt`
 6. start main.py `python main.py`
