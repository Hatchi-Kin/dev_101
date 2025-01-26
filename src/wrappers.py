from .utils import validate_and_execute_query


def get_all_books(query):
    return validate_and_execute_query(query, "get_all_books")


def get_all_authors(query):
    return validate_and_execute_query(query, "get_all_authors")


def get_all_authors_in_descending_order(query):
    return validate_and_execute_query(query, "get_all_authors_in_descending_order")


def get_all_authors_by_alphabetical_descending_order(query):
    return validate_and_execute_query(
        query, "get_all_authors_by_alphabetical_descending_order"
    )


def get_only_the_first_4_books_alphabetically(query):
    return validate_and_execute_query(
        query, "get_only_the_first_4_books_alphabetically"
    )


def get_books_with_id_inferior_to_5(query):
    return validate_and_execute_query(query, "get_books_with_id_inferior_to_5")


def get_books_with_ids_3_4_5_and_6(query):
    return validate_and_execute_query(query, "get_books_with_ids_3_4_5_and_6")


def get_only_books_and_authors_id_with_le_in_name_of_book(query):
    return validate_and_execute_query(
        query, "get_only_books_and_authors_id_with_le_in_name_of_book"
    )


def get_books_with_authors_using_join(query):
    return validate_and_execute_query(query, "get_books_with_authors_using_join")


def get_authors_that_have_more_than_3_books_available(query):
    return validate_and_execute_query(
        query, "get_authors_that_have_more_than_3_books_available"
    )


def create_new_author(query):
    return validate_and_execute_query(query, "create_new_author")


def create_new_book(query):
    return validate_and_execute_query(query, "create_new_book")


def get_book_by_rowling(query):
    return validate_and_execute_query(query, "get_book_by_rowling")


def update_book_title(query):
    return validate_and_execute_query(query, "update_book_title")


def delete_rowling_book(query):
    return validate_and_execute_query(query, "delete_rowling_book")


def delete_rowling_author(query):
    return validate_and_execute_query(query, "delete_rowling_author")
