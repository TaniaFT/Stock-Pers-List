# StudioHop

For use with a NOTHS storefront

stocklist.py is, as the name suggests, a stocklist generator, which ignores products that aren't kept in the warehouse whilst writing a sorted stocklist of the rest. Separating into general, socks, gloves, and foil scarves, it saves hand writing a list for hundreds of orders.

perslist.py imports perslistClasses.py to create a list of personalisations, split based on product personalisation method (such as printed A6/A5 inserts, embroidery, felting, etc). 

Once this is proven working and able to pull in the required data, the aim is to amend to export as a CSV for use from a spreadsheet, rather than the txt file currently generated.
