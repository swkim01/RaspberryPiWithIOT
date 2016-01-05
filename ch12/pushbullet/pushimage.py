from pushbullet import PushBullet

api_key = "q3U8S546S0D8tHJb8PrCzHaKABoHbnZy"

pb = PushBullet(api_key)
with open("gem1.png", "rb") as pic:
    file_data = pb.upload_file(pic, "gem1.png")

push = pb.push_file(**file_data)
