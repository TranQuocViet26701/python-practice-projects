from product_track_manager import ProductTrackManager
from notification_manager import NotificationManager


track_manager = ProductTrackManager()
while input("Do you want to create new request? (True/False): ") == "True":
    track_manager.create_track_request()

notification_manager = NotificationManager(track_manager.get_track_requests())
notification_manager.send_notification()


