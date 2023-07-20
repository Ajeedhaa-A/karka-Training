consumer_data={"consumer_name":"user","eb_reading":[1100,1200,1350,1650,2050]}
def cal_bill(consumer_data):
    for cons in consumer_data:
            con=cons['eb_reading']
            print(con)
consumer_data()