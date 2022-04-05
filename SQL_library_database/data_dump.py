# import sqlalchemy
# print(sqlalchemy.__version__)
#
# from sqlalchemy import create_engine
# from sqlalchemy import text
# engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
#
# with engine.connect() as conn:
#     conn.execute(
#         text(
#             "INSERT INTO books (book_id, dewy_decimal_number, isbn, book_title, author, genre, year_published, branch_id, copy_number, on_loan, reserved) VALUES (:book_id, :dewy_decimal_number, :isbn, :book_title, :author, :genre, :year_published, :branch_id, :copy_number, :on_loan, :reserved)"),
#         [{'book_id': 5, 'dewy_decimal_number': 538, 'isbn': 1226085,
#           'book_title': 'The Standard Book of Spells Grade 2', 'author': 'Miranda Goshawk', 'genre': 'Charms',
#           'year_published': 1962, 'branch_id': 2, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#           }, {'book_id': 6, 'dewy_decimal_number': 810, 'isbn': 2394430,
#               'book_title': 'The Standard Book of Spells Grade 3', 'author': 'Miranda Goshawk', 'genre': 'Charms',
#               'year_published': 1963, 'branch_id': 3, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#               }, {'book_id': 7, 'dewy_decimal_number': 133, 'isbn': 9170729,
#                   'book_title': 'The Standard Book of Spells Grade 4', 'author': 'Miranda Goshawk', 'genre': 'Charms',
#                   'year_published': 1965, 'branch_id': 1, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#                   }, {'book_id': 8, 'dewy_decimal_number': 549, 'isbn': 4446224,
#                       'book_title': 'The Standard Book of Spells Grade 5', 'author': 'Miranda Goshawk',
#                       'genre': 'Charms', 'year_published': 1967, 'branch_id': 1, 'copy_number': 1, 'on_loan': 'no',
#                       'reserved': 'no'
#                       }, {'book_id': 9, 'dewy_decimal_number': 853, 'isbn': 3541395,
#                           'book_title': 'The Standard Book of Spells Grade 6', 'author': 'Miranda Goshawk',
#                           'genre': 'Charms', 'year_published': 1968, 'branch_id': 3, 'copy_number': 1, 'on_loan': 'no',
#                           'reserved': 'no'
#                           },
#          {'book_id': 10, 'dewy_decimal_number': 708, 'isbn': 4965829, 'book_title': 'Achievements in Charming',
#           'author': 'Unknown', 'genre': 'Charms', 'year_published': 1967, 'branch_id': 3, 'copy_number': 1,
#           'on_loan': 'no', 'reserved': 'no'
#           }, {'book_id': 11, 'dewy_decimal_number': 156, 'isbn': 7436907,
#               'book_title': 'An Anthology of Eighteenth Century Charms', 'author': 'Unknown', 'genre': 'Charms',
#               'year_published': 1968, 'branch_id': 2, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#               },
#          {'book_id': 12, 'dewy_decimal_number': 702, 'isbn': 2848599, 'book_title': 'A Guide to Medieval Sorcery',
#           'author': 'Unknown', 'genre': 'Charms', 'year_published': 1977, 'branch_id': 1, 'copy_number': 1,
#           'on_loan': 'no', 'reserved': 'no'
#           }, {'book_id': 13, 'dewy_decimal_number': 919, 'isbn': 6180597,
#               'book_title': 'The Invisible Book of Invisibility', 'author': 'Unknown', 'genre': 'Charms',
#               'year_published': 1983, 'branch_id': 1, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#               },
#          {'book_id': 14, 'dewy_decimal_number': 637, 'isbn': 6257545, 'book_title': 'Madcap Magic for Wacky Warlocks',
#           'author': 'Unknown', 'genre': 'Charms', 'year_published': 1963, 'branch_id': 3, 'copy_number': 1,
#           'on_loan': 'no', 'reserved': 'no'
#           }, {'book_id': 15, 'dewy_decimal_number': 145, 'isbn': 8234206, 'book_title': 'Magical Theory',
#               'author': 'Adalbert Waffling', 'genre': 'Charms', 'year_published': 1987, 'branch_id': 3,
#               'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#               }, {'book_id': 16, 'dewy_decimal_number': 900, 'isbn': 6018849,
#                   'book_title': 'Olde and Forgotten Bewitchments and Charmes', 'author': 'Unknown', 'genre': 'Charms',
#                   'year_published': 1988, 'branch_id': 2, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#                   }, {'book_id': 17, 'dewy_decimal_number': 546, 'isbn': 1462515,
#                       'book_title': 'Powers You Never Knew You Had and What to Do with Them Now You’ve Wised Up',
#                       'author': 'Unknown', 'genre': 'Charms', 'year_published': 1964, 'branch_id': 1, 'copy_number': 1,
#                       'on_loan': 'no', 'reserved': 'no'},
#          {'book_id': 18, 'dewy_decimal_number': 304, 'isbn': 1226846, 'book_title': 'Quintessence: A Quest.',
#           'author': 'Unknown', 'genre': 'Charms', 'year_published': 1989, 'branch_id': 2, 'copy_number': 1,
#           'on_loan': 'no', 'reserved': 'no'
#           }, {'book_id': 19, 'dewy_decimal_number': 676, 'isbn': 3036493, 'book_title': 'Saucy Tricks for Tricky Sorts',
#               'author': 'Unknown', 'genre': 'Charms', 'year_published': 1981, 'branch_id': 1, 'copy_number': 1,
#               'on_loan': 'no', 'reserved': 'no'
#               }, {'book_id': 20, 'dewy_decimal_number': 185, 'isbn': 1316380,
#                   'book_title': 'A Study Into the Possibility of Reversing the Actual and Metaphysical Effects of Natural Death, with Particular Regard to the Reintegration of Essence and Matter',
#                   'author': 'Bertrand de Pensées-Profundes', 'genre': 'Charms', 'year_published': 1971, 'branch_id': 3,
#                   'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#                   }, {'book_id': 21, 'dewy_decimal_number': 155, 'isbn': 1846054,
#                       'book_title': 'Weird Wizarding Dilemmas and Their Solutions', 'author': 'Unknown',
#                       'genre': 'Charms', 'year_published': 1977, 'branch_id': 2, 'copy_number': 1, 'on_loan': 'no',
#                       'reserved': 'no'
#                       }, {'book_id': 22, 'dewy_decimal_number': 199, 'isbn': 2214414,
#                           'book_title': 'Where There’s a Wand There’s a Way', 'author': 'Unknown', 'genre': 'Charms',
#                           'year_published': 1989, 'branch_id': 3, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#                           }, {'book_id': 23, 'dewy_decimal_number': 154, 'isbn': 9962847,
#                               'book_title': 'The Dark Forces: A Guide to Self-Protection', 'author': 'Quentin Trimble',
#                               'genre': 'Defence against the dark arts; & dark arts', 'year_published': 1972,
#                               'branch_id': 3, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#                               }, {'book_id': 24, 'dewy_decimal_number': 178, 'isbn': 8726723,
#                                   'book_title': 'Basic Hexes for the Busy and Vexed', 'author': 'Unknown',
#                                   'genre': 'Defence against the dark arts; & dark arts', 'year_published': 1952,
#                                   'branch_id': 3, 'copy_number': 1, 'on_loan': 'no', 'reserved': 'no'
#                                   }]
#     )
#     conn.commit()
#
#
#
#
list1 = []
list2 = []
list3 = []
list3.append(list1)
list3.append(list2)
print(len(list3))
