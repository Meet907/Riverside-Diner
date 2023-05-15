# use the function "sqlQuery(query)" to run a query, it will return a array of rows for each resultrow
# Ex.
# login = sqlQuery("SELECT * From Login") Returns
#[(1, 'Adam', 'Spencer', '12345@gmail.com', '12345', 123456789), (2, 'John', 'Smith', 'johnsmith@gmail.com', 'johnsmith', 2147483647), (6, 'meet', 'D', '1212@gmail.com', '1212', 911),
# (7, 'hey', 'me', '22me@gmail.com', '22', 23232232), (14, 'Test2', 'Testing2', 'test2@gmail.com', 'qwerty', 1234567890), (15, 'Keval', 'Barvaliya', 'kevalbarvaliya007@gmail.com', 'Ke
# val1234', 2147483647), (16, 'kajf', 'wsf', 'aw@13gmail.com', '0000', 3565745)]
#Note row 1 is (1, 'Adam', 'Spencer', '12345@gmail.com', '12345', 123456789)
#so login[0][0] would be 1
#login[0][1] would be "Adam"
#login[0][2] would be "Spencer"
#login[1][3] would be "johnsmith@gmail.com"
#Etc.
#login[arrayindex][rowindex] gives various values
#this implementation is the same for any table you query from
#the amount of indicies in each array is the mount of rows
#the amount of indicies in each row is the same as the amount of columns in each row