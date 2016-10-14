import psycopg2
import urlparse
from flask import Flask
app = Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://lijoleyfufklmt:thhCUh_hMA8bN2gUwmvmefYdNL@ec2-54-235-254-199.compute-1.amazonaws.com:5432/dfopjhaf40r7qr")

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()

@app.route('/')
def hello():
    return "This is iSsalto. Welcome. Made by iSsaltantes."

@app.route('/ocorrencias/u=<username>')
def getOcorrencias(username):
    try:
        cur.execute("""SELECT * from Usuario where Username='{}';""".format(username))
    except:
        return "Failed to fetch from table."

    rows = cur.fetchall()
    if len(rows) != 1:
        return "Error: no such username."

    user = rows[0]

    #TODO: create class for user.
    searchRadius = user[2]
    posXUser = user[3]
    posYUser = user[4]

    cur.execute("""SELECT * from Ocorrencia where LocalizacaoX >= {} AND LocalizacaoX <= {} AND LocalizacaoY >= {} AND LocalizacaoY <= {}""".format(posXUser - searchRadius, posXUser + searchRadius, posYUser - searchRadius, posYUser + searchRadius))
    rows = cur.fetchall()
    result = "Ocorrencias:\n"
    for row in rows:
        result = result + "Id: " + str(row[0]) + ", Username: " + str(row[1]) + ", Tipo: " + str(row[2]) + ", Data: " + str(row[3]) + ", PosX: " + str(row[4]) + ", PosY: " + str(row[5]) + ", Descricao: " + str(row[6]) + "\n"
    return result

if __name__ == '__main__':
    app.run()







