-- check if a book is on loan
use books;
select book_id from on_loan;

-- borrow a book, need to know book_id and replace it in the last line (where id = book_id)
use loan;
insert into loan (user_id,	branch_id,	book_id,  date_loaned)  values ( 1, 1, 1, 2022-03-29);
use books;
update loan set on_loan = "YES" where id = book_id;



