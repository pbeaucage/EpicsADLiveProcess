EpicsADLiveProcess

A web-based engine for realtime input and processing of images taken with the EPICS AreaDetector package.

Peter Beaucage, NIST peter.beaucage@nist.gov






Setup
=========

Dependencies: pyepics, flask, numpy, pillow, bokeh, matplotlib.  Any recent python3 will work.


Install dependencies

Configure areadetector parameters in AreaDetectorLive.py (default kwargs to constructor at the top, at a minimum EPICS IOC address)

Configure reduction parameters in EpicsADLiveProcessDaemon.py (detector type, poni parameters, mask, etc)

Use
==========


Start the app with python flaskapp.py

Navigate a web browser to localhost:5050

The UI is bare-bones, see defined routes and routines in FlaskApp.py for details.



