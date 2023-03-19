import pandas


class ProductTrackManager:

    def __init__(self):
        try:
            df = pandas.read_csv("product_track.csv")
        except FileNotFoundError:
            df = pandas.DataFrame({
                "email": [],
                "url": [],
                "price": []
            })
            df.to_csv("product_track.csv")
        finally:
            self.data_frame = df

    def get_track_requests(self):
        return self.data_frame.to_dict("records")

    def create_track_request(self):
        user_email = input("What is your email? ")
        user_url = input("Which product do you want to keep track on Tiki? Please provide url: ")
        user_price = float(input("How much is your desire price? "))
        new_df = pandas.DataFrame({
            "email": [user_email],
            "url": [user_url],
            "price": [user_price]
        })
        self.data_frame = pandas.concat([self.data_frame, new_df], ignore_index=False)
        self.data_frame.to_csv("product_track.csv")

