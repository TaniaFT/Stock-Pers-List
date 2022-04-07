# NOTHS Stocklist + Personalisation List

For use with NOTHS storefront

stocklist.py is, as the name suggests, a stocklist generator, which ignores products that aren't kept in the warehouse whilst writing a sorted stocklist of the rest. Separating into general, socks, gloves, and foil scarves, it saves hand writing a list for hundreds of orders.

![Screenshot 2022-04-07 at 11 45 42](https://user-images.githubusercontent.com/103183077/162182184-d50b20f3-a071-4f52-a548-496fce6dfadf.png)


perslist.py imports perslistClasses.py to create a list of personalisations, split based on product personalisation method (such as printed A6/A5 inserts, embroidery, felting, etc). 

![Screenshot 2022-04-07 at 11 48 56](https://user-images.githubusercontent.com/103183077/162182692-ab4463b7-820c-4853-a714-d498d49db52c.png)


These can both be adapted based on products that they are skipping, duplicating or returning errors on.


# How to Use

If not already installed, download PyCharm (community edition) from JetBrains.

METHOD 1 - Download repository as a ZIP, and extract. When opening PyCharm, select 'Open' and select the whole extracted folder. 

![Screenshot 2022-04-07 at 11 17 27](https://user-images.githubusercontent.com/103183077/162177439-aee9db04-07ec-48fb-955f-589185ad3ee7.png)


METHOD 2 - open PyCharm and select 'Get from VCS' at top. Use the green Clone button in GitHub to get a HTTPS or SSH link. 

![Screenshot 2022-04-07 at 11 55 41](https://user-images.githubusercontent.com/103183077/162183800-a201e71f-1f00-452c-b23d-7f912d607535.png)


Follow the process as suggested, logging into GitHub SHKikiyo to continue, the program should prompt everything needed for setup.


A VENV will be needed (Pycharm will prompt setup, try to choose Python 3 or above when creating) to run, this is a one off when setting up the project.

![Screenshot 2022-04-07 at 11 11 07](https://user-images.githubusercontent.com/103183077/162176342-c5a7dd08-ae2b-4cb4-9d06-8244712b61c7.png)


Both stocklist.py and perslist.py may require requirements.txt be opened in PyCharm and any installations approved before they can run, this is a one off when setting up the project.

Right click on any  Create a config.py file in the same folder with your api key (can find on NOTHS CMS) as string variable api_key - this is imported by both stocklist.py and perslist.py. 

![Screenshot 2022-04-07 at 11 12 08](https://user-images.githubusercontent.com/103183077/162176531-f144be31-e0ab-443a-9343-95a7f62a5cfa.png)

If you used method 2, make sure NOT to select Add (simply click Cancel) to adding this to GitHub, as you do not want the API key available to view on GitHub.

![Screenshot 2022-04-07 at 11 13 11](https://user-images.githubusercontent.com/103183077/162176721-8e1a39ab-e70d-4525-881d-be02a273696a.png)

This file should have the following content, including quote marks around the api key:

    api_key = 'api-key-from-NOTHS'

Once this is all saved, you should be good to go! 


Simply select your chosen file, then press the play button to run and generate stocklist and personalisation list

![Screenshot 2022-04-07 at 11 23 10](https://user-images.githubusercontent.com/103183077/162178405-dc113752-340f-4a80-b955-9c343dd91b8d.png)



# ERRORS

If you get an error and the perslist does not generate, press the bug button (beside play) and it will present you with a list of info at the bottom - see the line with 'item' 

![Screenshot 2022-04-07 at 11 54 02](https://user-images.githubusercontent.com/103183077/162183515-4c16f2cb-8c61-42cd-a0eb-4f4e604f8b1e.png)

Copy and paste a line from the block of ignored products, and add the name of the product causing the error. You may have multiple items, so repeat as needed. 

![Screenshot 2022-04-07 at 11 38 38](https://user-images.githubusercontent.com/103183077/162180954-3e3a5a3f-2aaf-4b46-bcee-71351c116055.png)

Note - you may also want to go to the product on NOTHS and check that the settings are correct, and at least 2 options are available on the product (colour and gift box for example). This should avoid the error in future, so you can remove your new line from the list. 