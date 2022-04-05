# NOTHS Stocklist + Personalisation List

For use with a NOTHS storefront

stocklist.py is, as the name suggests, a stocklist generator, which ignores products that aren't kept in the warehouse whilst writing a sorted stocklist of the rest. Separating into general, socks, gloves, and foil scarves, it saves hand writing a list for hundreds of orders.

perslist.py imports perslistClasses.py to create a list of personalisations, split based on product personalisation method (such as printed A6/A5 inserts, embroidery, felting, etc). 

Once this is proven working and able to pull in the required data, the aim is to amend to export as a CSV for use from a spreadsheet, rather than the txt file currently generated.


# How to Use

Branch to use as needed, stocklist.py is standalone but perslist.py requires perslistClasses.py
Create a config.py file with api key, as variable api_key - this is imported by both stocklist.py and perslist.py

Simply run the main Python files to generate stocklist and personalisation - we use PyCharm.

Currently the options are all set and customised to the company this was made for, however it can easily be adjusted.
