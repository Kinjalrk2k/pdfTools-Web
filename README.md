# pdfTools-Web

A web application to merge PDF files.

**_This web application isn't optimized for mobile site_**

Find a CLI version here: [pdfTools](https://github.com/Kinjalrk2k/pdfTools)

Deployed [here](https://pdft00ls.herokuapp.com/)

## Usage

![tutorial](/app/static/screenshots/total.gif)

## Use locally

- Clone this repository and move to it's directory
  ```shell
  git clone https://github.com/Kinjalrk2k/pdfTools-Web.git
  cd pdfTools-Web
  ```
- Creating and activating the virtual envoirnment
  ```shell
  python3 -m venv env
  source env/bin/activate // for macOS/Linux (or when using bash)
  .\env\Scripts\activate  //  for windows
  ```
- Install the dependencies
  - Python
  ```shell
  pip install -r requirements.txt
  ```
  - NPM
  ```shell
  cd app/static
  npm install
  ```
- Make a .env file in the root
  ```
  FLASK_APP=manage.py
  FLASK_ENV=development
  ```
- **[IMPORTANT]**: For local Configuration
  - This local configuration imposes no-time limit to the whole functionality
  - Explore `app/__init__.py` and
    - Replace the line `from config import ProdConfig as CurrentConfig` with `from config import LocalConfig as CurrentConfig`
    - ```shell
      - from config import ProdConfig as CurrentConfig
      + from config import LocalConfig as CurrentConfig
      ```
- Run the server
  ```shell
  flask run
  ```
  Follow the prompt for the URL of the server

## Technologies used

- Backend
  - Flask: Framework
  - PyPDF2: Handling PDF files
- Jinja: Templating
- Frontend
  - Spectrum CSS: Adobe’s design system → Overall design
  - Dropzone: Handling drag-n-drop file upload
  - Dragula: Handling drag to arrange

## References

- [Flask: Lightweight WSGI web application framework](https://flask.palletsprojects.com/en/1.1.x/)
- [pdfTools: A small CLI python script based on PyPDF2 for extracting, merging and doing a lot more on pdf files](https://github.com/Kinjalrk2k/pdfTools)
- [Jinja: Modern and designer-friendly templating language for Python](https://jinja.palletsprojects.com/en/2.11.x/)
- [PyPDF2: A utility to read and write PDFs with Python](https://pythonhosted.org/PyPDF2/)
- [Spectrum CSS: Adobe’s design system](https://opensource.adobe.com/spectrum-css/)
- [DropzoneJS: Open source library that provides drag’n’drop file uploads with image previews](https://www.dropzonejs.com/)
- [Dragula: Drag and drop so simple it hurts](https://github.com/bevacqua/dragula)
