import re


def add_new_item(df, item: list):
    """
    Function for adding a record to purchase dataframe
    :param df: pandas dataframe
    :param item: list of values
    :return: pandas dataframe
    """
    df.loc[len(df.index)] = item
    df.reset_index(drop=True, inplace=True)
    df.to_csv(r'purchase.csv', index=False)
    return df


def show_for_date(df, input_date: str):
    """
    Function returns records from dataframe of purchases on a specific date
    :param df: pandas dataframe
    :param input_date: string with date YYYY-MM-DD format
    :return: pandas dataframe with records for the date
    """
    return df.loc[df.Date == input_date]


def show_by_category(df, category: str):
    """
    Function shows records of purchases by chosen category
    :param df: pandas dataframe
    :param category: string with category of purchase
    :return: dataframe with records of entered category if category is exists or None
    """
    if category in df.Category.unique():
        return df.loc[df.Category == category]


def min_to_max(df):
    """
    Function returns asc sorted dataframe by cost of purchases.
    :param df: pandas dataframe
    :return: asc sorted dataframe
    """
    return df.sort_values(by=["Cost"], ascending=True)


def del_item(df, item: int):
    """
    Function deletes a record in dataframe by index
    :param df: pandas dataframe
    :param item: int index of purchase's record in dataframe
    :return: return new dataframe if index of record exists or None
    """
    try:
        df.drop(index=int(item), inplace=True)
    except ValueError or KeyError:
        return None
    except KeyError:
        return None
    df.reset_index(drop=True, inplace=True)
    df.to_csv(r'purchase.csv', index=False)
    return df


def show_message(output, df=None):
    """
    Interface function for messaging to the user

    >>> show_message("del", None)
    You've entered a wrong number
    """
    match output:
        case "hi":
            print("Hello")
        case "del":
            if df is None:
                print("You've entered a wrong number")
            else:
                print("The record was successfully deleted")
        case "bye":
            print("Bye-Bye!")
        case "add_item":
            print("Fill the form to ADD the purchase")
        case "category":
            if df is not None:
                print(df)
            else:
                print("Sorry, No such category")
        case "which_category":
            print(f'Which category do you want to show by?\n\tCategories: {" | ".join(df.Category.unique())}')
        case "wrong":
            print("\nWrong number, try only 1,2,3,4,5,6 or 7 for exit the program\n")
        case "show_all":
            print(df)
        case "min_to_max":
            print(min_to_max(df))
        case "date":
            if df.empty:
                print("\t\tSorry, No such date")
            else:
                print(f'\n{df}')
        case "exception":
            print('File "purchase.csv" not found in the root directory of application')
        case "wrong_date":
            print("This is not a date or wrong format. You need YYYY-MM-DD")
        case "wrong_cost":
            print("This is not a number. You should enter the integer number.")
        case "menu":
            print(f'\n\t1. Add\n'
                  f'\t2. Show all\n'
                  f'\t3. Show for date\n'
                  f'\t4. Show by category\n'
                  f'\t5. Show by min->max\n'
                  f'\t6. Delete\n'
                  f'\t7. Exit\n')


def input_actions(enter):
    """
    Interface function for input data from the user
    """
    match enter:
        case "press_enter":
            return input("\nPress Enter to exit main menu")
        case "menu_item":
            menu_item = input("\tWhat would you like to do? ").strip()
            return menu_item
        case "del_item":
            return input("\n\tEnter the ID of line, which you want to DELETE: ").strip()
        case "add_date":
            date = input("Date (YYYY-MM-DD): ").strip()
            if check_input(date, "check_date"):
                return date
            else:
                return None
        case "add_cost":
            cost = input("Enter cost: ").strip()
            if check_input(cost, "check_cost"):
                return cost
            else:
                return None
        case "add_category":
            return input("Enter category: ").title().strip()
        case "add_product":
            return input("Enter product: ").title().strip()
        case "show_date":
            return input("\tEnter the date (YYYY-MM-DD):").strip()
        case "category":
            return input("\t\tEnter the category:").title().strip()


def check_input(field, key=None):
    """
    Function for checking input using RegEx
    >>> check_input('2021-01-30', 'check_date')
    True
    >>> check_input('56',"check_cost")
    True
    """
    if key == "check_date":
        match = re.fullmatch(r'([12][0-9][0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][1-9]|3[0-1])', field)
        if match:
            return True
    elif key == "check_cost":
        match = re.fullmatch(r'\d+', field)
        if match:
            return True
    else:
        return False
