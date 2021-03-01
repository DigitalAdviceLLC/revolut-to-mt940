# Convert Revolut export file to MT940 format

1. Clone this repo or download the fiels and unzip, place the revolut export csv inside this folder and name it as input.csv
2. edit main.py file with any text editor, go to 
    ```args.account_iban = 'REPLACE_REAL_IBAN_HERE' ```
    and put your real IBAN, save the file
3. go to terminal/command prompt, locate/navigate to this unzipped folder, makesure you have python ready using ```python -V``` and ```python3 -V``` commands, you should see a version number if all good with Python setup 
4. run this command ```python3 main.py```
5. Done - you will have a new output.mt940 file created in the same folder

## WARNING

* the original library https://github.com/gerwin3/revolut-to-mt940/blob/master/revolut.py is using Description column of CSV as Name, and Reference column of CSV as Description into mt940, this library also doing the same, kindly check with import systems with this before generating real reports
