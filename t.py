

from flask import Flask, render_template, request
import pymysql

db = pymysql.connect(host="8.130.54.170", user="root",
                     password="123456", database="db_privacy")
cursor = db.cursor()
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


last_select = ""
last_results = []
last_cursor = 0


@app.route("/select")
def select():
    global last_select
    global last_results
    global last_cursor
    # id name tel qq vx mail adr edu note
    id = request.args.get('id')
    name = request.args.get('name')
    tel = request.args.get('tel')
    qq = request.args.get('qq')
    vx = request.args.get('vx')
    mail = request.args.get('mail')
    adr = request.args.get('adr')
    edu = request.args.get('edu')
    note = request.args.get('note')
    # print(type(id), name, tel, qq, vx, mail, adr, edu, note, sep='|')

    # 模糊匹配
    if id != "":
        id = "id like '%" + id + "%' and "
    if name != "":
        name = "name like '%" + name + "%' and "
    if tel != "":
        tel = "tel like '%" + tel + "%' and "
    if qq != "":
        qq = "qq like '%" + qq + "%' and "
    if vx != "":
        vx = "vx like '%" + vx + "%' and "
    if mail != "":
        mail = "mail like '%" + mail + "%' and "
    if adr != "":
        adr = "adr like '%" + adr + "%' and "
    if edu != "":
        edu = "edu like '%" + edu + "%' and "
    if note != "":
        note = "note like '%" + note + "%' and "

    sql = 'select * from t_privacy where ' + id + \
        name + tel + qq + vx + mail + adr + edu + note
    if sql[-4:] == 'and ':
        sql = sql[:-4] + ';'
    # print(sql)
    if last_select != sql:
        last_select = sql
        cursor.execute(sql)

        results = cursor.fetchall()
        if len(results) == 0:
            return render_template('index.html')
        last_results = results
        last_cursor = 0

    else:
        results = last_results
        last_cursor += 1

    # # 加入分页
    # # 1. 获取总记录数
    # total = len(results)
    # # 2. 每页显示的记录数
    # per_page = 1
    # # 3. 计算总页数
    # total_page = total // per_page
    # if total % per_page != 0:
    #     total_page += 1
    # # 4. 获取当前页码
    # page = request.args.get('page')
    # if page is None:
    #     page = 1
    # else:
    #     page = int(page)
    # # 5. 计算当前页的起始索引
    # start = (page - 1) * per_page
    # # 6. 计算当前页的结束索引
    # end = page * per_page
    # # 7. 获取当前页的数据
    # results = results[start:end]
    # # 8. 生成分页的HTML代码
    # page_html = ''
    # for i in range(1, total_page + 1):
    #     page_html += '<a href="/select?page=%d">%d</a>' % (i, i)
    # print(page_html)
    # return render_template('index.html', results=results, page_html=page_html)

    # for row in results:
    #     # print(row)
    #     id = row[0]
    #     name = row[1]
    #     tel = row[2]
    #     qq = row[3]
    #     vx = row[4]
    #     mail = row[5]
    #     adr = row[6]
    #     edu = row[7]
    #     note = row[8]
    #     break
    id = results[last_cursor][0]
    name = results[last_cursor][1]
    tel = results[last_cursor][2]
    qq = results[last_cursor][3]
    vx = results[last_cursor][4]
    mail = results[last_cursor][5]
    adr = results[last_cursor][6]
    edu = results[last_cursor][7]
    note = results[last_cursor][8]

    return render_template('index.html', idx=id, namex=name, telx=tel, qqx=qq, vxx=vx, mailx=mail, adrx=adr, edux=edu, notex=note)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
