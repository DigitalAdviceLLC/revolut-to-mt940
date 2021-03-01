import argparse

from revolut import RevolutCsvReader
from mt940 import Mt940Writer


def main():
    parser = argparse.ArgumentParser(
        prog='oddity-revolut-to-mt940',
        description='Convert Revolut CSV-files to MT940 format.')

    #REPLACE IBAN IN THE FOLLOWING LINE
    args.account_iban = 'REPLACE_REAL_IBAN_HERE'
    
    args.input_file = 'input.csv'
    args.output_file = 'output.mt940'
    
    reader = RevolutCsvReader(args.input_file)

    with Mt940Writer(args.output_file, args.account_iban) as writer:
        transactions = reader.get_all_transactions()
        for transaction in transactions:
            writer.write_transaction(transaction)

        print('Wrote {} transactions to file: {}.'.format(len(transactions), args.output_file))


if __name__ == "__main__":
    main()
