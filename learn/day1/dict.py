id_db = {
    12:{
        'name':'libai',
        'age':12
    },
    13: {
        'name': 'libai',
        'age': 12
    }
}
print(id_db)
print(id_db[12])
id_db[12]['name']="zhangsan"
id_db[12]['sex']="m"
del  id_db[12]['sex'] #删除1
id_db[12].pop('name') #删除2
print(id_db.get(13)) #获取 这样 key 不存在 输入 none，防止报错，建议这样使用
print(id_db[12])
id2 = {12:{'fei':'d'}}
id_db.update(id2)
print(id_db)
print(id_db.keys())
print(id_db.values())
12 in id_db # 3.0
print(id_db.setdefault(162,56)) #有就取出啦，没有就设置