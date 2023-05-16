# canvas_tools
CLI automation tools to make canvas easier to work with

Please be aware that these tools involve caching student data on the machine
where they are being run. Be aware that where ever these scripts are run will
need to be sufficiently secured to void FERPA violations.

To function, you will need to provide a Canvas API key to the tools. BE VERY CAREFUL WITH HOW THIS KEY IS STORED AND TRANSPORTED! Anyone able to copy/access your API key can impersonate you to Canvas. As a teacher, this exposes confidential student data _and_ allows effectively unlimited modification of your assignments/gradebooks/etc.


# Dependencies
## Python3
This project expects a python3 runtime.

## PostgreSQL
Caching is a requirement for most of the tools since the CanvasAPI is really
inefficient for directly answering some questions. The caching layer is provided
by PostgreSQL. Porting to SQLite likely wouldn't be hard.

The Python Postgres driver can be installed via pip:

    pip3 install 'psycopg[binary]'

## Canvas API
This project make use of python canvas API <https://github.com/ucfopen/canvasapi>

The Canvas API can be installed via pip: 

    pip3 install canvasapi

## Canvas
The Canvas API requires the URL for the Canvas instance and a key for authentication. You'll need to generate a Canvas key via the Canvas web interface.
