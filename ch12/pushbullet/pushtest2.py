from pushbullet import PushBullet

api_key = "<API KEY>"

pb = PushBullet(api_key)
pushes = pb.get_pushes()
print pushes
latest = pushes[1][0]
if 'TodaysWeather' in latest.get('title'):
    body = latest.get('body')
    if any(x in body for x in ['Sunny', 'Clear']):
        print 'Good'
    elif 'Cloud' in body:
        print 'Not Bad'
    elif any(x in body for x in ['Rain', 'Shower', 'Snow']):
        print 'Bad'
#items = pushes[1]
#for item in items:
    #print item
    #pb.dismiss_push(item.get('iden'))
    #pb.delete_push(item.get('iden'))
