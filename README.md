<div align="center">
  <img src="https://github.com/alivx/Ego-View-Digital-Signage/blob/master/Media/header.png">
</div>
[Maintained?](#maintained)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Revealjs as Digital Signage (RDS) (beta testing)
=========

[![Build Status](https://travis-ci.org/alivx/revealjs-digital-signage.svg?branch=master)](https://travis-ci.org/alivx/revealjs-digital-signage)

Free Digital Signage for Everyone. Start using this tool right now. `Revealjs as Digital Signage (RDS)` is an easy tool to create Digital Signage.
This tool use jinja2 template to render it to ready Revealjs html using python.


# To DO
* Add flask to serve the output file.
* Add remote API for control the presentation via API.
* Add more option to `generate.py`
* add raspberry pi gpio as a presentation control.

# config.yaml
Presentation behaviour can be fine-tuned using a wide array of configuration options

Example:
```Bash
htmlOutputFileName: index.html #Final output HTML file
combinedHTMLSlides: mergedHTML.html #Name of combined section
slidesPrefixPathnName: sections/slide*.html #Section html files path and prefix
templateFileName: mainTemplate.html #Main HTML template file
finalOutputDir: output #Output Dir name
transitions: zoom # none, fade, slide, convex, concave, zoom
autoPlayMedia: "true" #null, "true", "false"
hashOneBasedIndex: "true"
```

# generate.py
run command to render the template `python generate.py`

# Media
Store all media that you used inside the slides

# Files
Do not touch those file(revealjs files), if you do not know what you do :)

# sections
Put all your slide in HTML files

---

# How to use
1. Put your slide as HTML in `sections` Dir.
2. Put your media files in Media if exists.
3. change the config files if required.
4. run command `python generate.py`
5. the output file with name `index.html` will appear in the root Dir.


## Using Docker

```Bash
docker container run -ti -v $PWD:/app alivx/rds:latest
```

Check the output Dir for final HTML files, you can find path under config['finalOutputDir']



# Notes:
* you can use print option in the browser to print presentation slides as PDF file.

Author Information
------------------

The role was originally developed by [Ali Saleh Baker](https://www.linkedin.com/in/alivx/).