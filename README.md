<div align="center">
  <img src="https://github.com/alivx/Ego-View-Digital-Signage/blob/master/Media/header.png">
</div>

Revealjs as Digital Signage (RDS) (beta testing)
=========

Free Digital Signage for Everyone. Start using this tool right now. `Revealjs as Digital Signage (RDS)` is an easy tool to create Digital Signage.


# To DO
1. Add flask to serve the output file.
2. Add remote API for control the presentation via API.
3. Add more option to `generate.py`
4. Simplify the configuration.
5. add raspberry pi gpio as a presentation control.
6. Remove static jinja2 variable from the template.

# config.yaml
Presentation behaviour can be fine-tuned using a wide array of configuration options

# generate.py
run command to render the template

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




Author Information
------------------

The role was originally developed by [Ali Saleh Baker](https://www.linkedin.com/in/alivx/).