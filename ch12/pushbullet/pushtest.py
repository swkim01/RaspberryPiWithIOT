from pushbullet import PushBullet

api_key = "<API KEY>"

pb = PushBullet(api_key)
push = pb.push_note("Hello", "World")

#pushes = pb.get_pushes()
#print pushes
