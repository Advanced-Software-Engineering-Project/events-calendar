import requests

import json
from pprint import pprint

headers = {
    'origin': 'https://www.facebook.com',
    'dnt': '1',
    'accept-language': 'en-US,en;q=0.8,fr;q=0.6',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json',
    'referer': 'https://www.facebook.com/search/pages/?q=columbia%20university',
    'authority': 'www.facebook.com',
    'cookie': 'datr=BDkcV-_7haIIZuILU78LRnRZ; lu=gA_fuLGahnhyh5T1RNNto-NQ; sb=HDkcV5s1DOEUEczamFuEXyGO; _ga=GA1.2.1585845431.1474032856; c_user=1084380721; xs=36%3AnyontbA6y-SPIQ%3A2%3A1461467421%3A6482; fr=0Lo9YceHsP4DsufUw.AWVM-hBkd4PFMegojhFrkmo2Ilo.BXHDkd.5j.FgE.0.0.BYDQTR.AWUHXs3d; csm=2; s=Aa5kCyc1qRdxOObx.BXb_GY; p=-2; presence=EDvF3EtimeF1477249597EuserFA21084380721A2EstateFDt2F_5b_5dElm2FnullEuct2F1477237355BEtrFA2loadA2EtwF639981519EatF1477249594990G477249597755CEchFDp_5f1084380721F70CC; act=1477249602135%2F13',
}

data = {
  '__user': '1084380721',
  '__a': '1',
  '__dyn': 'aKhoFeyfyGmaomgDDx2IGAyq85oR6yUmyVbGAEG8UNFLOaA6em5-rmi9GaxuifhKagDyAueCG6UO9CCK5VJ0wyKbQubyR88x2axvh98CVpfLKtojKeCAzV-EiGtAxu6oHDh8Ku6rCAzq_hep5zA5Kuifz8gAWAgO8gaqxm49GADh8zyogx6eyUF0BglBVoGr_g-pbggKmEiyqxqXHAyAdGl7G',
  '__af': 'o',
  '__req': '5i',
  '__be': '-1',
  '__pc': 'EXP1:DEFAULT',
  'fb_dtsg': 'AQFGAYJ8QYEf:AQH6FD38_Gpz',
  'ttstamp': '265817071658974568189691025865817254706851569571112122',
  '__rev': '2638327',
  '__srp_t': '1477244424',
  'av': '1084380721',
  'batch_name': 'TimelineEventsCalendarApp_react_PageRelayQL',
  'method': 'GET',
  'queries': '{"q4":{"priority":0,"q":"Query TimelineEventsCalendarApp_react_PageRelayQL {node(655078074554911) {@F6}} QueryFragment F0 : Page {id,name,url,is_owned} QueryFragment F1 : Node {id,__typename} QueryFragment F2 : Event {id,name,url} QueryFragment F3 : Event {id,viewer_watch_status,connection_style,event_viewer_capability {is_viewer_admin,can_viewer_edit,can_viewer_join,can_viewer_promote}} QueryFragment F4 : Event {id,viewer_guest_status,event_buy_ticket_url,connection_style,event_viewer_capability {is_viewer_admin,is_viewer_admin.enable_business_permissions(false) as _is_viewer_admin1hS8xA,can_viewer_edit,can_viewer_share,can_viewer_join},event_creator {id,__typename},is_canceled,@F3} QueryFragment F5 : Event {id,time_range {start},is_event_draft,scheduled_publish_timestamp,start_time_sentence.format(SHORT_TIME_LABEL) as _start_time_sentenceiczKr,suggested_event_context_sentence.show_category(false) as _suggested_event_context_sentence2eg3eg {text},event_place {contextual_name,city {contextual_name,id},__typename,@F0,@F1},event_viewer_capability {is_viewer_admin},is_canceled,@F2,@F4} QueryFragment F6 : Page {id,all_owned_events.past(true).allowed_states(CANCELED,DRAFT,SCHEDULED_DRAFT_FOR_PUBLICATION,PUBLISHED).filter_out_canceled_events_if_not_connected(true).after(1044297612297917).first(10) as _all_owned_events3RFdY2 {edges {is_hidden_on_profile_calendar,is_added_to_profile_calendar,node {id,time_range {start},@F5},cursor},page_info {has_next_page,has_previous_page}}}","query_params":{}}}',
  'response_format': 'json',
  'scheduler': 'phased'
}


events = []
i = 0
with open('pages_with_ids.json') as data_file:
    pages_data = json.load(data_file)

    # For every Columbia Page:
    for page in pages_data:
        page['node_id'] ='655078074554911'
        data['queries'] = '{"q4":{"priority":0,"q":"Query TimelineEventsCalendarApp_react_PageRelayQL {node(' + page['node_id'] + ') {@F6}} QueryFragment F0 : Page {id,name,url,is_owned} QueryFragment F1 : Node {id,__typename} QueryFragment F2 : Event {id,name,url} QueryFragment F3 : Event {id,viewer_watch_status,connection_style,event_viewer_capability {is_viewer_admin,can_viewer_edit,can_viewer_join,can_viewer_promote}} QueryFragment F4 : Event {id,viewer_guest_status,event_buy_ticket_url,connection_style,event_viewer_capability {is_viewer_admin,is_viewer_admin.enable_business_permissions(false) as _is_viewer_admin1hS8xA,can_viewer_edit,can_viewer_share,can_viewer_join},event_creator {id,__typename},is_canceled,@F3} QueryFragment F5 : Event {id,time_range {start},is_event_draft,scheduled_publish_timestamp,start_time_sentence.format(SHORT_TIME_LABEL) as _start_time_sentenceiczKr,suggested_event_context_sentence.show_category(false) as _suggested_event_context_sentence2eg3eg {text},event_place {contextual_name,city {contextual_name,id},__typename,@F0,@F1},event_viewer_capability {is_viewer_admin},is_canceled,@F2,@F4} QueryFragment F6 : Page {id,all_owned_events.past(true).allowed_states(CANCELED,DRAFT,SCHEDULED_DRAFT_FOR_PUBLICATION,PUBLISHED).filter_out_canceled_events_if_not_connected(true).after(1044297612297917).first(10) as _all_owned_events3RFdY2 {edges {is_hidden_on_profile_calendar,is_added_to_profile_calendar,node {id,time_range {start},@F5},cursor},page_info {has_next_page,has_previous_page}}}","query_params":{}}}'

        pprint(page['node_id'])
        pprint(page['url'])

        response = requests.post('https://www.facebook.com/api/graphqlbatch/', headers=headers, data=data)
        if response.content:
            if len(response.content.split('\n')[0]) > 5:
                print(response.content.split('\n')[0])
                json_data = json.loads(response.content.split('\n')[0])
        else:
            continue

        if 'http' not in page['node_id']:
            pertinent_data = json_data['q4']['response'][page['node_id']]['_all_owned_events3RFdY2']['edges']
        else:
            continue

        # Add all that Page's events:
        for d in pertinent_data:
            event = {}
            event['id'] = d['node']['id']
            event['datetime'] = d['node']['time_range']['start']
            event['title'] = d['node']['name']
            event['location'] = d['node']['event_place']['name']
            event['url'] = d['node']['url']

            events.append(event)

        i = i + 1
        if i % 10 == 0:
            print('done with ' + str(i) + ' pages')
            print('events count: ' + str(len(events)))

        break


with open('events_data.txt', 'w') as outfile:
    json.dump(events, outfile)