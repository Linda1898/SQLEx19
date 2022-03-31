-- CHECK IF A BOOK IS ON LOAN - example = book_id 1
use library3;
select book_title, on_loan, reserved from books where book_id = 1;

-- BORROW A BOOK - example = user_id 2 borrowing book_id 1 and unreserving it
insert into loans (user_id, branch_id, book_id,  date_loaned)  values (2, 1, 1, "2022-05-02");
update books set on_loan = "yes" where book_id = 1;
update books set reserved = "NO" where book_id = 1;





