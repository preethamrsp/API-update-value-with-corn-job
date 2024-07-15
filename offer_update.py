import requests
import json
import random
import time

while(True):

        API_ORIGIN = 'http://api.mobtions.affise.com'
        API_KEY = '66e5fbbbf53ff9491aacf714f464e33c'  # enter your affise key

        random_values = json.load(open('random_values.json'))


        def get_random_values(collection_name: str):
            values = random_values.get(collection_name)
            if values:
                return random.choice(values)


        def update_offer(offer_id):
            api_url = f"{API_ORIGIN}/3.0/admin/offer/{offer_id}"
            radom_value1 = get_random_values('collection1')
            tracking_url = f"https://inter-nswitch.nasmob.com/click?nsw_camp_id=6409&nsw_media_id=668&clickid={{clickid}}&nsw_event_id={{goal}}&nsw_sub_media_id={{pid}}_{{sub2}}&nsw_bundle={radom_value1}&nsw_google_aid={{sub3}}&nsw_idfa={{sub4}}"

            
            # here you can add more field & values if required
            # here for example, Its updating only tracking url
            payload = {
                "url": tracking_url
            }
            
            print(tracking_url)
            headers = {
                'API-Key': API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            response = requests.post(api_url, headers=headers, data=payload)
            print(response)

        def update_offer1(offer_id):
            api_url = f"{API_ORIGIN}/3.0/admin/offer/{offer_id}"
            radom_value1 = get_random_values('collection1')
            tracking_url = f"https://inter-nswitch.nasmob.com/click?nsw_camp_id=6236&nsw_media_id=617&clickid={{clickid}}&nsw_event_id={{goal}}&nsw_sub_media_id={{pid}}_{{sub2}}&nsw_bundle={radom_value1}&nsw_google_aid={{sub3}}&nsw_idfa={{sub4}}"
            
            
            # here you can add more field & values if required
            # here for example, Its updating only tracking url
            payload = {
                "url": tracking_url
            }
            
            print(tracking_url)
            headers = {
                'API-Key': API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            response = requests.post(api_url, headers=headers, data=payload)
            print(response)
            
        def update_offer2(offer_id):
            api_url = f"{API_ORIGIN}/3.0/admin/offer/{offer_id}"
            radom_value1 = get_random_values('collection1')
            tracking_url = f"https://inter-nswitch.nasmob.com/click?nsw_camp_id=6411&nsw_media_id=617&clickid={{clickid}}&nsw_event_id={{goal}}&nsw_sub_media_id={{pid}}_{{sub2}}&nsw_bundle={radom_value1}&nsw_google_aid={{sub3}}&nsw_idfa={{sub4}}"
            
            
            # here you can add more field & values if required
            # here for example, Its updating only tracking url
            payload = {
                "url": tracking_url
            }
            
            print(tracking_url)
            headers = {
                'API-Key': API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            response = requests.post(api_url, headers=headers, data=payload)
            print(response)

        def update_offer3(offer_id):
            api_url = f"{API_ORIGIN}/3.0/admin/offer/{offer_id}"
            radom_value1 = get_random_values('collection1')
            tracking_url = f"http://inter-nswitch.nasmob.com/click?nsw_camp_id=6396&nsw_media_id=617&clickid={{clickid}}&nsw_event_id={{goal}}&nsw_sub_media_id={{pid}}_{{sub2}}&nsw_bundle={radom_value1}&nsw_google_aid={{sub3}}&nsw_idfa={{sub4}}"
            
            
            # here you can add more field & values if required
            # here for example, Its updating only tracking url
            payload = {
                "url": tracking_url
            }
            
            print(tracking_url)
            headers = {
                'API-Key': API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            response = requests.post(api_url, headers=headers, data=payload)
            print(response)

        def update_offer4(offer_id):
            api_url = f"{API_ORIGIN}/3.0/admin/offer/{offer_id}"
            radom_value1 = get_random_values('collection1')
            tracking_url = f"https://inter-nswitch.nasmob.com/click?nsw_camp_id=6403&nsw_media_id=617&clickid={{clickid}}&nsw_event_id={{goal}}&nsw_sub_media_id={{pid}}_{{sub2}}&nsw_bundle={radom_value1}&nsw_google_aid={{sub3}}&nsw_idfa={{sub4}}"
            
            
            # here you can add more field & values if required
            # here for example, Its updating only tracking url
            payload = {
                "url": tracking_url
            }
            
            print(tracking_url)
            headers = {
                'API-Key': API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            response = requests.post(api_url, headers=headers, data=payload)
            print(response)


        def main():
            update_offer(1261206)
            update_offer1(1259064)
            update_offer2(1261210) 
            update_offer3(1251367)
            update_offer4(1261209)
             # 1234 is your sample offer id at affise platform


        if __name__ == '__main__':
            main()

        time.sleep(300)





