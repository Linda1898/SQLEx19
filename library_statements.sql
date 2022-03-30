-- CHECK IF A BOOK IS ON LOAN
use books;
select book_id from on_loan;

-- BORROW A BOOK, need to know book_id and replace it in the last line (where id = book_id)
-- use loan;
-- insert into loan (user_id,	branch_id,	book_id,  date_loaned)  values ( user_id, branch_id, book_id, 00-00-00);
-- use books;
-- update loan set on_loan = "YES" where id = book_id;



