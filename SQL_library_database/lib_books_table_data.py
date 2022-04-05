import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)

with engine.connect() as conn:
    conn.execute(
        text(
            "INSERT INTO books (book_id, dewy_decimal_number, isbn, book_title, author, genre, year_published, branch_id, copy_number, on_loan, reserved) VALUES (:book_id, :dewy_decimal_number, :isbn, :book_title, :author, :genre, :year_published, :branch_id, :copy_number, :on_loan, :reserved)"),
        [{'book_id':4, 'dewy_decimal_number':393.333,'isbn':'st7689899', 'book_title':'The Standard Book of Spells Grade 1','author':'Miranda Goshawk', 'genre':'Charms', 'year_published':1961,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':5, 'dewy_decimal_number':190.410,'isbn':'ts1226085', 'book_title':'The Standard Book of Spells Grade 2','author':'Miranda Goshawk', 'genre':'Charms', 'year_published':1962,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':6, 'dewy_decimal_number':475.663,'isbn':'er2394430', 'book_title':'The Standard Book of Spells Grade 3','author':'Miranda Goshawk', 'genre':'Charms', 'year_published':1963,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':7, 'dewy_decimal_number':594.218,'isbn':'ns9170729', 'book_title':'The Standard Book of Spells Grade 4','author':'Miranda Goshawk', 'genre':'Charms', 'year_published':1965,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':8, 'dewy_decimal_number':906.249,'isbn':'ay4446224', 'book_title':'The Standard Book of Spells Grade 5','author':'Miranda Goshawk', 'genre':'Charms', 'year_published':1967,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':9, 'dewy_decimal_number':533.946,'isbn':'on3541395', 'book_title':'The Standard Book of Spells Grade 6','author':'Miranda Goshawk', 'genre':'Charms', 'year_published':1968,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':10, 'dewy_decimal_number':294.306,'isbn':'ed4965829', 'book_title':'Achievements in Charming','author':'Unknown', 'genre':'Charms', 'year_published':1967,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':11, 'dewy_decimal_number':939.637,'isbn':'ee7436907', 'book_title':'An Anthology of Eighteenth Century Charms','author':'Unknown', 'genre':'Charms', 'year_published':1968,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':12, 'dewy_decimal_number':241.186,'isbn':'ls2848599', 'book_title':'A Guide to Medieval Sorcery','author':'Unknown', 'genre':'Charms', 'year_published':1977,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':13, 'dewy_decimal_number':868.984,'isbn':'gs6180597', 'book_title':'The Invisible Book of Invisibility','author':'Unknown', 'genre':'Charms', 'year_published':1983,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':14, 'dewy_decimal_number':324.796,'isbn':'ks6257545', 'book_title':'Madcap Magic for Wacky Warlocks','author':'Unknown', 'genre':'Charms', 'year_published':1963,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':15, 'dewy_decimal_number':622.553,'isbn':'ry8234206', 'book_title':'Magical Theory','author':'Adalbert Waffling', 'genre':'Charms', 'year_published':1987,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':16, 'dewy_decimal_number':776.200,'isbn':'es6018849', 'book_title':'Olde and Forgotten Bewitchments and Charmes','author':'Unknown', 'genre':'Charms', 'year_published':1988,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':17, 'dewy_decimal_number':130.991,'isbn':'Up1462515', 'book_title':'Powers You Never Knew You Had and What to Do with Them Now You’ve Wised Up','author':'Unknown', 'genre':'Charms', 'year_published':1964,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':18, 'dewy_decimal_number':373.189,'isbn':'st1226846', 'book_title':'Quintessence: A Quest','author':'Unknown', 'genre':'Charms', 'year_published':1989,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':19, 'dewy_decimal_number':288.442,'isbn':'ts3036493', 'book_title':'Saucy Tricks for Tricky Sorts','author':'Unknown', 'genre':'Charms', 'year_published':1981,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':20, 'dewy_decimal_number':331.247,'isbn':'er1316380', 'book_title':'A Study Into the Possibility of Reversing the Actual and Metaphysical Effects of Natural Death, with Particular Regard to the Reintegration of Essence and Matter','author':'Bertrand de Pensées-Profundes', 'genre':'Charms', 'year_published':1971,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':21, 'dewy_decimal_number':911.417,'isbn':'ns1846054', 'book_title':'Weird Wizarding Dilemmas and Their Solutions','author':'Unknown', 'genre':'Charms', 'year_published':1977,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':22, 'dewy_decimal_number':395.808,'isbn':'ay2214414', 'book_title':'Where There’s a Wand There’s a Way','author':'Unknown', 'genre':'Charms', 'year_published':1989,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':23, 'dewy_decimal_number':181.327,'isbn':'on9962847', 'book_title':'The Dark Forces: A Guide to Self-Protection','author':'Quentin Trimble', 'genre':'DADA', 'year_published':1972,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':24, 'dewy_decimal_number':207.734,'isbn':'ed8726723', 'book_title':'Basic Hexes for the Busy and Vexed','author':'Unknown', 'genre':'DADA', 'year_published':1952,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':25, 'dewy_decimal_number':751.725,'isbn':'ee7756655', 'book_title':'Break with a Banshee','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1992,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':26, 'dewy_decimal_number':697.431,'isbn':'ls7251383', 'book_title':'Gadding with Ghouls','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1993,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':27, 'dewy_decimal_number':218.706,'isbn':'gs6447539', 'book_title':'Holidays with Hags','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1994,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':28, 'dewy_decimal_number':913.955,'isbn':'ls2092560', 'book_title':'Travels with Trolls','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1996,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':29, 'dewy_decimal_number':225.236,'isbn':'es7323838', 'book_title':'Voyages with Vampires','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1996,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':30, 'dewy_decimal_number':614.735,'isbn':'es6591810', 'book_title':'Wanderings with Werewolves','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1997,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':31, 'dewy_decimal_number':868.327,'isbn':'ti8929855', 'book_title':'Year with the Yeti','author':'Gilderoy Lockhart', 'genre':'DADA', 'year_published':1992,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':32, 'dewy_decimal_number':860.510,'isbn':'ns6157133', 'book_title':'A Compendium of Common Curses and Their Counter-Actions','author':'Unknown', 'genre':'DADA', 'year_published':1966,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':33, 'dewy_decimal_number':381.133,'isbn':'ss4629337', 'book_title':'Con,fronting the Faceless','author':'Unknown', 'genre':'DADA', 'year_published':1961,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':34, 'dewy_decimal_number':971.248,'isbn':'re6116628', 'book_title':'Curses and Counter-Curses: Bewitch Your Friends and Befuddle Your Enemies with the Latest Revenges: Hair Loss; Jelly Legs; Tongue-Tying and Much, Much More','author':'Vindictus Viridian', 'genre':'DADA', 'year_published':1974,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':35, 'dewy_decimal_number':161.993,'isbn':'ed6259048', 'book_title':'The Dark Arts Outsmarted','author':'Unknown', 'genre':'DADA', 'year_published':1950,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':36, 'dewy_decimal_number':667.632,'isbn':'ry1130754', 'book_title':'Defensive Magical Theory','author':'Wilbert Slinkhard', 'genre':'DADA', 'year_published':1981,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':37, 'dewy_decimal_number':272.805,'isbn':'ed2431441', 'book_title':'Jinxes for the Jinxed','author':'Unknown', 'genre':'DADA', 'year_published':1954,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':38, 'dewy_decimal_number':882.956,'isbn':'le5373177', 'book_title':'Magick Moste Evile','author':'Unknown', 'genre':'DADA', 'year_published':1956,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':39, 'dewy_decimal_number':165.385,'isbn':'ts4384437', 'book_title':'Practical Defensive Magic and its Use Against the Dark Arts','author':'Unknown', 'genre':'DADA', 'year_published':1989,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':40, 'dewy_decimal_number':818.230,'isbn':'rt2237469', 'book_title':'Secrets of the Darkest Art','author':'Unknown', 'genre':'DADA', 'year_published':1963,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':41, 'dewy_decimal_number':971.429,'isbn':'rk3376257', 'book_title':'Self-Defensive Spellwork','author':'Unknown', 'genre':'DADA', 'year_published':1968,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':42, 'dewy_decimal_number':486.986,'isbn':'er3137047', 'book_title':'Sonnets of a Sorcerer','author':'Unknown', 'genre':'DADA', 'year_published':1979,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':43, 'dewy_decimal_number':675.713,'isbn':'gi2557590', 'book_title':'One Thousand Magical Herbs and Fungi','author':'Phyllida Spore', 'genre':'Herbology', 'year_published':1952,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':44, 'dewy_decimal_number':389.288,'isbn':'ls4258385', 'book_title':'Encyclopaedia of Toadstools','author':'Unknown', 'genre':'Herbology', 'year_published':1962,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':45, 'dewy_decimal_number':883.532,'isbn':'ld9474518', 'book_title':'Flesh-Eating Trees of The World','author':'Unknown', 'genre':'Herbology', 'year_published':1978,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':46, 'dewy_decimal_number':885.535,'isbn':'es3452322', 'book_title':'Magical Mediterranean Water Plants and Their Properties','author':'Unknown', 'genre':'Herbology', 'year_published':1963,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':47, 'dewy_decimal_number':152.593,'isbn':'ic4557230', 'book_title':'A History of Magic','author':'Bathilda Bagshot', 'genre':'History of magic', 'year_published':1978,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':48, 'dewy_decimal_number':455.343,'isbn':'ry3189140', 'book_title':'Great Wizarding Events of the Twentieth Century','author':'Unknown', 'genre':'History of magic', 'year_published':1984,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':49, 'dewy_decimal_number':322.625,'isbn':'ry4768216', 'book_title':'Great Wizards of the Twentieth Century','author':'Unknown', 'genre':'History of magic', 'year_published':1956,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':50, 'dewy_decimal_number':193.411,'isbn':'ry3944924', 'book_title':'Hogwarts: A History','author':'Unknown', 'genre':'History of magic', 'year_published':1979,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':51, 'dewy_decimal_number':980.207,'isbn':'es3203332', 'book_title':'Important Modern Magical Discoveries','author':'Unknown', 'genre':'History of magic', 'year_published':1986,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':52, 'dewy_decimal_number':371.365,'isbn':'ry7411965', 'book_title':'Modern Magical History','author':'Unknown', 'genre':'History of magic', 'year_published':1976,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':53, 'dewy_decimal_number':844.505,'isbn':'gy5427475', 'book_title':'Nature’s Nobility: A Wizarding Genealogy','author':'Unknown', 'genre':'History of magic', 'year_published':1974,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':54, 'dewy_decimal_number':822.697,'isbn':'me8782646', 'book_title':'Notable Magical Names of Our Time','author':'Unknown', 'genre':'History of magic', 'year_published':1973,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':55, 'dewy_decimal_number':406.677,'isbn':'er2446673', 'book_title':'Prefects Who Gained Power','author':'Unknown', 'genre':'History of magic', 'year_published':1970,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':56, 'dewy_decimal_number':683.353,'isbn':'ts2390704', 'book_title':'The Rise and Fall of the Dark Arts','author':'Unknown', 'genre':'History of magic', 'year_published':1981,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':57, 'dewy_decimal_number':262.471,'isbn':'ry5050669', 'book_title':'Sites of Historical Sorcery','author':'Unknown', 'genre':'History of magic', 'year_published':1958,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':58, 'dewy_decimal_number':797.634,'isbn':'ry1049234', 'book_title':'A Study of Recent Developments in Wizardry','author':'Unknown', 'genre':'History of magic', 'year_published':1950,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':59, 'dewy_decimal_number':483.351,'isbn':'ns7965425', 'book_title':'Magical Drafts and Potions','author':'Arsenic Jigger', 'genre':'Potions', 'year_published':1954,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':60, 'dewy_decimal_number':574.673,'isbn':'ng9291937', 'book_title':'Advanced Potion Making','author':'Libatius Borage', 'genre':'Potions', 'year_published':1968,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':61, 'dewy_decimal_number':489.733,'isbn':'ms3716520', 'book_title':'Asiatic Anti-Venoms','author':'Unknown', 'genre':'Potions', 'year_published':1954,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':62, 'dewy_decimal_number':375.397,'isbn':'ns5230865', 'book_title':'Moste Potente Potions','author':'Unknown', 'genre':'Potions', 'year_published':1963,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':63, 'dewy_decimal_number':855.662,'isbn':'on5794189', 'book_title':'A Beginners Guide to Transfiguration','author':'Emeric Switch', 'genre':'Transfiguration', 'year_published':1985,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':64, 'dewy_decimal_number':740.151,'isbn':'on3243907', 'book_title':'Intermediate Transfiguration','author':'Unknown', 'genre':'Transfiguration', 'year_published':1966,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':65, 'dewy_decimal_number':412.627,'isbn':'on9186313', 'book_title':'A Guide to Advanced Transfiguration','author':'Unknown', 'genre':'Transfiguration', 'year_published':1974,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':66, 'dewy_decimal_number':711.870,'isbn':'on2975945', 'book_title':'Theories of Transubstantial Transfiguration','author':'Unknown', 'genre':'Transfiguration', 'year_published':1959,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':67, 'dewy_decimal_number':215.895,'isbn':'sy3399724', 'book_title':'Ancient Runes Made Easy','author':'Unknown', 'genre':'Ancient runes', 'year_published':1963,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':68, 'dewy_decimal_number':399.571,'isbn':'on7108322', 'book_title':'Ancient Rune Translation','author':'Unknown', 'genre':'Ancient runes', 'year_published':1951,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':69, 'dewy_decimal_number':307.376,'isbn':'ms1387306', 'book_title':'Magical Hieroglyphs and Logograms','author':'Unknown', 'genre':'Ancient runes', 'year_published':1977,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':70, 'dewy_decimal_number':165.460,'isbn':'ry7659058', 'book_title':'Spellman’s Syllabary','author':'Unknown', 'genre':'Ancient runes', 'year_published':1977,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':71, 'dewy_decimal_number':129.277,'isbn':'gy8417218', 'book_title':'New Theory of Numerology','author':'Unknown', 'genre':'Arithmancy', 'year_published':1973,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':72, 'dewy_decimal_number':881.877,'isbn':'ca1760745', 'book_title':'Numerology and Grammatica','author':'Unknown', 'genre':'Arithmancy', 'year_published':1969,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':73, 'dewy_decimal_number':947.765,'isbn':'em5371674', 'book_title':'Fantastic Beasts and Where to Find Them','author':'Newt Scamander', 'genre':'Care of magical creatures', 'year_published':1960,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':74, 'dewy_decimal_number':870.482,'isbn':'rs4067097', 'book_title':'The Monster Book of Monsters','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1975,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':75, 'dewy_decimal_number':347.741,'isbn':'it1465067', 'book_title':'Dragon Breeding for Pleasure and Profit','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1958,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':76, 'dewy_decimal_number':814.302,'isbn':'nd2763268', 'book_title':'Dragon Species of Great Britain and Ireland','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1972,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':77, 'dewy_decimal_number':813.258,'isbn':'de1078356', 'book_title':'From Egg to Inferno: A Dragon Keeper’s Guide','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1968,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':78, 'dewy_decimal_number':310.387,'isbn':'ch3873584', 'book_title':'Men Who Love Dragons Too Much','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1954,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':79, 'dewy_decimal_number':647.818,'isbn':'ty9091073', 'book_title':'Fowl or Foul?: A Study of Hippogriff Brutality','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1987,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':80, 'dewy_decimal_number':853.504,'isbn':'gy8362480', 'book_title':'The Handbook of Hippogriff Psychology','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1958,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':81, 'dewy_decimal_number':438.983,'isbn':'es7659326', 'book_title':'Blood Brothers: My Life Amongst the Vampires','author':'Eldred Worple', 'genre':'Care of magical creatures', 'year_published':1986,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':82, 'dewy_decimal_number':459.475,'isbn':'ep3921235', 'book_title':'Dreadful Denizens of the Deep','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1972,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':83, 'dewy_decimal_number':249.170,'isbn':'rt3306162', 'book_title':'Hairy Snout, Human Heart','author':'Unknown', 'genre':'Care of magical creatures', 'year_published':1971,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':84, 'dewy_decimal_number':578.796,'isbn':'ed7984004', 'book_title':'Why I Didn’t Die When the Augrey Cried','author':'Gulliver Pokeby', 'genre':'Care of magical creatures', 'year_published':1980,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':85, 'dewy_decimal_number':376.180,'isbn':'ul4440746', 'book_title':'Broken Balls: When Fortunes Turn Foul','author':'Unknown', 'genre':'Divination', 'year_published':1986,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':86, 'dewy_decimal_number':447.913,'isbn':'ng4720284', 'book_title':'Death Omens: What to Do When You Know the Worst is Coming','author':'Unknown', 'genre':'Divination', 'year_published':1971,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':87, 'dewy_decimal_number':460.846,'isbn':'le1228596', 'book_title':'The Dream Oracle','author':'Inigo Imago', 'genre':'Divination', 'year_published':1956,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':88, 'dewy_decimal_number':840.580,'isbn':'ks8393344', 'book_title':'Predicting the Unpredictable: Insulate Yourself Against Shocks','author':'Unknown', 'genre':'Divination', 'year_published':1962,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':89, 'dewy_decimal_number':359.748,'isbn':'re1423378', 'book_title':'Unfogging the Future','author':'Cassandra Vablatsky', 'genre':'Divination', 'year_published':1958,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':90, 'dewy_decimal_number':869.431,'isbn':'es5805601', 'book_title':'Home Life and Social Habits of British Muggles','author':'Unknown', 'genre':'Muggle studies', 'year_published':1965,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':91, 'dewy_decimal_number':223.824,'isbn':'ce8100807', 'book_title':'Muggles Who Notice','author':'Blenheim Stalk', 'genre':'Muggle studies', 'year_published':1954,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':92, 'dewy_decimal_number':116.656,'isbn':'ow5019401', 'book_title':'The Philosophy of the Mundane: Why the Muggles Prefer Not to Know','author':'Professor Mordicus Egg', 'genre':'Muggle studies', 'year_published':1952,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':93, 'dewy_decimal_number':181.127,'isbn':'es8224637', 'book_title':'Quidditch Through the Ages','author':'Kennilworthy Whisp', 'genre':'Quidditch & flying', 'year_published':1989,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':94, 'dewy_decimal_number':251.828,'isbn':'le4846174', 'book_title':'The Beater’s Bible','author':'Brutus Scrimgeour', 'genre':'Quidditch & flying', 'year_published':1962,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':95, 'dewy_decimal_number':502.595,'isbn':'ch5404727', 'book_title':'Beating the Bludgers: A Study of Defensive Strategies in Quidditch','author':'Kennilworthy Whisp', 'genre':'Quidditch & flying', 'year_published':1983,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':96, 'dewy_decimal_number':129.317,'isbn':'ns9226671', 'book_title':'Flying with the Cannons','author':'Unknown', 'genre':'Quidditch & flying', 'year_published':1952,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':97, 'dewy_decimal_number':155.247,'isbn':'ks4460649', 'book_title':'The Noble Sport of Warlocks','author':'Quintius Umfraville', 'genre':'Quidditch & flying', 'year_published':1966,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':98, 'dewy_decimal_number':953.656,'isbn':'nd6946783', 'book_title':'Quidditch Teams of Britain and Ireland','author':'Unknown', 'genre':'Quidditch & flying', 'year_published':1980,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':99, 'dewy_decimal_number':808.242,'isbn':'an1810341', 'book_title':'The Wonder of Wigtown Wanderers, He Flew Like a Madman','author':'Kennilworthy Whisp', 'genre':'Quidditch & flying', 'year_published':1982,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':100, 'dewy_decimal_number':608.205,'isbn':'re1998208', 'book_title':'Handbook of Do-It-Yourself Broomcare','author':'Unknown', 'genre':'Quidditch & flying', 'year_published':1953,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':101, 'dewy_decimal_number':530.858,'isbn':'Me2246327', 'book_title':'Magical Me','author':'Gilderoy Lockhart', 'genre':'Biography', 'year_published':1998,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':102, 'dewy_decimal_number':429.783,'isbn':'re7601114', 'book_title':'The Life and Lies of Albus Dumbledore','author':'Rita Skeeter', 'genre':'Biography', 'year_published':2004,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':103, 'dewy_decimal_number':737.136,'isbn':'rd7384727', 'book_title':'The Tales of Beedle the Bard','author':'Unknown', 'genre':'Fiction & folklore', 'year_published':1953,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':104, 'dewy_decimal_number':863.855,'isbn':'at1736118', 'book_title':'Grumble the Grubby Goat','author':'Unknown', 'genre':'Fiction & folklore', 'year_published':1985,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':105, 'dewy_decimal_number':813.418,'isbn':'ds8279133', 'book_title':'Hélas, Je Me Suis Transfiguré les Pieds','author':'Malecrit', 'genre':'Fiction & folklore', 'year_published':1979,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':106, 'dewy_decimal_number':271.867,'isbn':'es6902724', 'book_title':'Toadstool Tales','author':'Beatrix Bloxam', 'genre':'Fiction & folklore', 'year_published':1998,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':107, 'dewy_decimal_number':727.404,'isbn':'se3363451', 'book_title':'Charm Your Own Cheese','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1995,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':108, 'dewy_decimal_number':883.788,'isbn':'ng5968958', 'book_title':'Enchantment in Baking','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1997,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':109, 'dewy_decimal_number':755.758,'isbn':'ic3133381', 'book_title':'One Minute Feasts: It’s Magic','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1997,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':110, 'dewy_decimal_number':508.642,'isbn':'ns2591704', 'book_title':'Common Magical Ailments and Afflictions','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1998,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':111, 'dewy_decimal_number':378.470,'isbn':'te1862459', 'book_title':'The Healer’s Helpmate','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1990,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':112, 'dewy_decimal_number':933.551,'isbn':'pe3312495', 'book_title':'An Appraisal of Magical Education in Europe','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1996,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':113, 'dewy_decimal_number':197.450,'isbn':'ts3496538', 'book_title':'Gilderoy Lockhart’s Guide to Household Pests','author':'Gilderoy Lockhart', 'genre':'Household spells & miscellanea', 'year_published':1995,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':114, 'dewy_decimal_number':564.227,'isbn':'it5439763', 'book_title':'The Hairy Heart: A Guide to Wizards Who Won’t Commit','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1990,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':115, 'dewy_decimal_number':463.385,'isbn':'es1199505', 'book_title':'Twelve Fail-Safe Ways to Charm Witches','author':'Unknown', 'genre':'Household spells & miscellanea', 'year_published':1994,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':116, 'dewy_decimal_number':519.434,'isbn':'et5408654', 'book_title':'Daily Prophet','author':'Various', 'genre':'Periodicals', 'year_published':1993,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':117, 'dewy_decimal_number':548.517,'isbn':'et2427225', 'book_title':'Evening Prophet','author':'Various', 'genre':'Periodicals', 'year_published':1994,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':118, 'dewy_decimal_number':265.453,'isbn':'et1050929', 'book_title':'Sunday Prophet','author':'Various', 'genre':'Periodicals', 'year_published':1995,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':119, 'dewy_decimal_number':739.604,'isbn':'le4363632', 'book_title':'The Adventures of Martin Miggs, the Mad Muggle','author':'Various', 'genre':'Periodicals', 'year_published':1996,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':120, 'dewy_decimal_number':820.730,'isbn':'ng1144171', 'book_title':'Challenges in Charming','author':'Various', 'genre':'Periodicals', 'year_published':1997,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':121, 'dewy_decimal_number':837.572,'isbn':'er5055114', 'book_title':'The Practical Potioneer','author':'Various', 'genre':'Periodicals', 'year_published':1994,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':122, 'dewy_decimal_number':957.436,'isbn':'er8455156', 'book_title':'The Quibbler','author':'Various', 'genre':'Periodicals', 'year_published':1997,'branch_id':3, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':123, 'dewy_decimal_number':435.149,'isbn':'ay6299511', 'book_title':'Transfiguration Today','author':'Various', 'genre':'Periodicals', 'year_published':1999,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':124, 'dewy_decimal_number':765.338,'isbn':'ar4580942', 'book_title':'Warlock at War','author':'Various', 'genre':'Periodicals', 'year_published':1993,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':125, 'dewy_decimal_number':406.610,'isbn':'ck3576359', 'book_title':'Which Broomstick','author':'Various', 'genre':'Periodicals', 'year_published':1995,'branch_id':2, 'copy_number':1,'on_loan':'no', 'reserved':'no'
},{'book_id':126, 'dewy_decimal_number':843.828,'isbn':'ly1060002', 'book_title':'Witch Weekly','author':'Various', 'genre':'Periodicals', 'year_published':1999,'branch_id':1, 'copy_number':1,'on_loan':'no', 'reserved':'no'
}]
  )
    conn.commit()



