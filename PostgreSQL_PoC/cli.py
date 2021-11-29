import db


# Download & setup postgresql db
# run postgresql db/local server
# 'pip install psycopg2' or 'conda install psycopg2'
# Update 'db_config.py' to your db name/db user
# create test table and populate it with data - in my case I used 'accounts' table
    #see 'test_data.png'
# test different db commands using db.interact(...)





def print_tuples(rows):
    for row in rows:
        for field in row:
            print(field, end='\t')
        print()




# CLI Info›

def main(): 

    print("Simple command line interface")
    choice = input("Would you like to see all accounts? 'y' or 'n''\n")

    if choice == 'y':
        output = db.interact("SELECT * FROM accounts;")
        print_tuples(output)


main()