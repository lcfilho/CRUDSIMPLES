from controller import db_insert, db_update, db_select, db_delete
from pprint import pprint

# db_insert('1','francisco', '1223456789', 'frasdn@gmail.com')
# db_insert('2','marina', '1223456789', 'rgrng@gmail.com')
#db_insert('3','carvalho', '1223456789', 'rgensadr@gmail.com')
# db_insert('4','caravardinianoi', '1223456789', 'hdsdsaasrnd@gmail.com')
# db_insert('5','caren', '1223456789', 'rdgnd@gmail.com')
#db_insert('6','maicon', '1223456789', 'rgdng@gmail.com')
#db_insert('7','paula', '1223456789', 'ergnf@gmail.com')
#db_insert('8','railan', '1223456789', 'ganng@gmail.com')


# db_update('122345678', '1')
# db_update('000000000', '2')
# db_update('999999999', '3')
# db_update('222222222', '4')
# db_update('333333333', '5')
#db_update('444444444', '1')
#db_update('555555555', '7')

# db_delete('4')



# db_select('1','1223456789')

pprint(db_select('4', 'id'))