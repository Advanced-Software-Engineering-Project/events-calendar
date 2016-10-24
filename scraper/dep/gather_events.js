// ?id=https://www.facebook.com/columbiamed/

var express       = require('express');
var fs            = require('fs');
var request       = require('request');
var app           = express();
var http          = require('http');

var querystring   = require('querystring');
var FormData = require('form-data');



var theOptions = {
  url: 'https://www.facebook.com/api/graphqlbatch/',
  //method: 'GET',
  headers: {
    'Content-Length': 2442,
    'Expect': '100-continue',
    'origin': 'https://www.facebook.com',
    'dnt': 1,
    'accept-language': 'en-US,en;q=0.8,fr;q=0.6',
    //'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'referer': 'https://www.facebook.com/search/pages/?q=columbia%20university',
    'authority': 'www.facebook.com',
    'cookie': 'datr=BDkcV-_7haIIZuILU78LRnRZ; lu=gA_fuLGahnhyh5T1RNNto-NQ; sb=HDkcV5s1DOEUEczamFuEXyGO; _ga=GA1.2.1585845431.1474032856; c_user=1084380721; xs=36%3AnyontbA6y-SPIQ%3A2%3A1461467421%3A6482; fr=0Lo9YceHsP4DsufUw.AWWIsGvEyhRZHCXCujYI8lWTmew.BXHDkd.5j.FgE.0.0.BYDNqE.AWVrtTZW; csm=2; s=Aa5kCyc1qRdxOObx.BXb_GY; p=-2; act=1477238930381%2F7; presence=EDvF3EtimeF1477238933EuserFA21084380721A2EstateFDt2F_5b_5dElm2FnullEuct2F1477237355BEtrFA2loadA2EtwF202900783EatF1477238932826G477238933241CEchFDp_5f1084380721F3CC'
  }
};


var options = {
  hostname: 'facebook.com',
  port: 443,
  path: '/api/graphqlbatch/',
  method: 'GET',
  rejectUnauthorized: false,
  headers: theOptions.headers
};


var body = {
  __user: 1084380721,
  __a: 1,
  __dyn: 'aKieDxaUW2K4XyoS2q3mbGeye4u-CE24xu6oF7zFEf9ErwGz8KEvgS3qiidBxa8xm4E8U8VofFUcU89o-58nyocEC1MCDy8-6EhzEnwBwLCBxC5Uvyo9E8pE',
  __af: 'o',
  __req: '5i',
  __be: -1,
  __pc: 'EXP1%3ADEFAULT',
  fb_dtsg: 'AQHBO3VWbkcw%3AAQHWyaWo65Nj',
  ttstamp: '26581726679518687981079911958658172871219787111545378106',
  __rev: '2638327',
  __srp_t: '1477248448',
  av: 1084380721,
  batch_name: 'TimelineEventsCalendarRoute',
  method: 'GET',
  queries: '%7B%22q0%22%3A%7B%22priority%22%3A0%2C%22q%22%3A%22Query%20TimelineEventsCalendarRoute%20%7Bnode(1446231682259516)%20%7Bid%2C__typename%2C%40F7%7D%7D%20QueryFragment%20F0%20%3A%20Page%20%7Bid%2Cname%2Curl%2Cis_owned%7D%20QueryFragment%20F1%20%3A%20Node%20%7Bid%2C__typename%7D%20QueryFragment%20F2%20%3A%20Event%20%7Bid%2Cname%2Curl%7D%20QueryFragment%20F3%20%3A%20Event%20%7Bid%2Cviewer_watch_status%2Cconnection_style%2Cevent_viewer_capability%20%7Bis_viewer_admin%2Ccan_viewer_edit%2Ccan_viewer_join%2Ccan_viewer_promote%7D%7D%20QueryFragment%20F4%20%3A%20Event%20%7Bid%2Cviewer_guest_status%2Cevent_buy_ticket_url%2Cconnection_style%2Cevent_viewer_capability%20%7Bis_viewer_admin%2Cis_viewer_admin.enable_business_permissions(false)%20as%20_is_viewer_admin1hS8xA%2Ccan_viewer_edit%2Ccan_viewer_share%2Ccan_viewer_join%7D%2Cevent_creator%20%7Bid%2C__typename%7D%2Cis_canceled%2C%40F3%7D%20QueryFragment%20F5%20%3A%20Event%20%7Bid%2Ctime_range%20%7Bstart%7D%2Cis_event_draft%2Cscheduled_publish_timestamp%2Cstart_time_sentence.format(SHORT_TIME_LABEL)%20as%20_start_time_sentenceiczKr%2Csuggested_event_context_sentence.show_category(false)%20as%20_suggested_event_context_sentence2eg3eg%20%7Btext%7D%2Cevent_place%20%7Bcontextual_name%2Ccity%20%7Bcontextual_name%2Cid%7D%2C__typename%2C%40F0%2C%40F1%7D%2Cevent_viewer_capability%20%7Bis_viewer_admin%7D%2Cis_canceled%2C%40F2%2C%40F4%7D%20QueryFragment%20F6%20%3A%20Page%20%7Bid%2Cviewer_profile_permissions%2Cadmin_info%20%7Bis_viewer_business_manager_admin%7D%7D%20QueryFragment%20F7%20%3A%20Page%20%7Bid%2Cname%2Cviewer_profile_permissions%2Call_owned_events.upcoming(true).allowed_states(CANCELED%2CDRAFT%2CSCHEDULED_DRAFT_FOR_PUBLICATION%2CPUBLISHED).filter_out_canceled_events_if_not_connected(true).first(10)%20as%20_all_owned_events12JYfp%20%7Bedges%20%7Bis_hidden_on_profile_calendar%2Cis_added_to_profile_calendar%2Cnode%20%7Bid%2Ctime_range%20%7Bstart%7D%2C%40F5%7D%2Ccursor%7D%2Cpage_info%20%7Bhas_next_page%2Chas_previous_page%7D%7D%2Call_owned_events.past(true).allowed_states(CANCELED%2CDRAFT%2CSCHEDULED_DRAFT_FOR_PUBLICATION%2CPUBLISHED).filter_out_canceled_events_if_not_connected(true).first(10)%20as%20_all_owned_events2fwm0O%20%7Bedges%20%7Bis_hidden_on_profile_calendar%2Cis_added_to_profile_calendar%2Cnode%20%7Bid%2Ctime_range%20%7Bstart%7D%2C%40F5%7D%2Ccursor%7D%2Cpage_info%20%7Bhas_next_page%2Chas_previous_page%7D%7D%2C%40F6%7D%22%2C%22query_params%22%3A%7B%7D%7D%7D',
  response_format: 'json',
  scheduler: 'phased'
};



var pages_data = JSON.parse(fs.readFileSync('pages_with_ids.json', 'utf8'));

var events = [];
var done = 0;
for (var i = 0; i < 1; i++) { //} pages_data.length; i++) {
  doIt(i);
}

function doIt(i) {

  var form = new FormData();
  form.append('__user', '1084380721');
  form.append('__a', 1);
  form.append('__dyn', 'aKieDxaUW2K4XyoS2q3mbGeye4u-CE24xu6oF7zFEf9ErwGz8KEvgS3qiidBxa8xm4E8U8VofFUcU89o-58nyocEC1MCDy8-6EhzEnwBwLCBxC5Uvyo9E8pE');
  form.append('__af', 'o');
  form.append('__req', '5i');
  form.append('__be', -1);
  form.append('__pc', 'EXP1%3ADEFAULT');
  form.append('fb_dtsg', 'AQHBO3VWbkcw%3AAQHWyaWo65Nj');
  form.append('ttstamp', '26581726679518687981079911958658172871219787111545378106');
  form.append('__rev', '2638327');
  form.append('__srp_t', '1477248448');
  form.append('av', '1084380721');
  form.append('batch_name', 'TimelineEventsCalendarRoute');
  form.append('method', 'GET');
  form.append('queries', '%7B%22q0%22%3A%7B%22priority%22%3A0%2C%22q%22%3A%22Query%20TimelineEventsCalendarRoute%20%7Bnode(1446231682259516)%20%7Bid%2C__typename%2C%40F7%7D%7D%20QueryFragment%20F0%20%3A%20Page%20%7Bid%2Cname%2Curl%2Cis_owned%7D%20QueryFragment%20F1%20%3A%20Node%20%7Bid%2C__typename%7D%20QueryFragment%20F2%20%3A%20Event%20%7Bid%2Cname%2Curl%7D%20QueryFragment%20F3%20%3A%20Event%20%7Bid%2Cviewer_watch_status%2Cconnection_style%2Cevent_viewer_capability%20%7Bis_viewer_admin%2Ccan_viewer_edit%2Ccan_viewer_join%2Ccan_viewer_promote%7D%7D%20QueryFragment%20F4%20%3A%20Event%20%7Bid%2Cviewer_guest_status%2Cevent_buy_ticket_url%2Cconnection_style%2Cevent_viewer_capability%20%7Bis_viewer_admin%2Cis_viewer_admin.enable_business_permissions(false)%20as%20_is_viewer_admin1hS8xA%2Ccan_viewer_edit%2Ccan_viewer_share%2Ccan_viewer_join%7D%2Cevent_creator%20%7Bid%2C__typename%7D%2Cis_canceled%2C%40F3%7D%20QueryFragment%20F5%20%3A%20Event%20%7Bid%2Ctime_range%20%7Bstart%7D%2Cis_event_draft%2Cscheduled_publish_timestamp%2Cstart_time_sentence.format(SHORT_TIME_LABEL)%20as%20_start_time_sentenceiczKr%2Csuggested_event_context_sentence.show_category(false)%20as%20_suggested_event_context_sentence2eg3eg%20%7Btext%7D%2Cevent_place%20%7Bcontextual_name%2Ccity%20%7Bcontextual_name%2Cid%7D%2C__typename%2C%40F0%2C%40F1%7D%2Cevent_viewer_capability%20%7Bis_viewer_admin%7D%2Cis_canceled%2C%40F2%2C%40F4%7D%20QueryFragment%20F6%20%3A%20Page%20%7Bid%2Cviewer_profile_permissions%2Cadmin_info%20%7Bis_viewer_business_manager_admin%7D%7D%20QueryFragment%20F7%20%3A%20Page%20%7Bid%2Cname%2Cviewer_profile_permissions%2Call_owned_events.upcoming(true).allowed_states(CANCELED%2CDRAFT%2CSCHEDULED_DRAFT_FOR_PUBLICATION%2CPUBLISHED).filter_out_canceled_events_if_not_connected(true).first(10)%20as%20_all_owned_events12JYfp%20%7Bedges%20%7Bis_hidden_on_profile_calendar%2Cis_added_to_profile_calendar%2Cnode%20%7Bid%2Ctime_range%20%7Bstart%7D%2C%40F5%7D%2Ccursor%7D%2Cpage_info%20%7Bhas_next_page%2Chas_previous_page%7D%7D%2Call_owned_events.past(true).allowed_states(CANCELED%2CDRAFT%2CSCHEDULED_DRAFT_FOR_PUBLICATION%2CPUBLISHED).filter_out_canceled_events_if_not_connected(true).first(10)%20as%20_all_owned_events2fwm0O%20%7Bedges%20%7Bis_hidden_on_profile_calendar%2Cis_added_to_profile_calendar%2Cnode%20%7Bid%2Ctime_range%20%7Bstart%7D%2C%40F5%7D%2Ccursor%7D%2Cpage_info%20%7Bhas_next_page%2Chas_previous_page%7D%7D%2C%40F6%7D%22%2C%22query_params%22%3A%7B%7D%7D%7D');
  form.append('response_format', 'json');
  form.append('scheduler', 'phased');


  var request = http.request({
    method: 'GET',
    host: 'facebook.com',
    path: '/api/graphqlbatch/',
    headers: theOptions.headers
  });


  form.pipe(request);


  form.getLength(function(err, length){

    var r = request.get("http://posttestserver.com/post.php", requestCallback);
    r._form = form;
    r.setHeader('content-length', length);

  });

  request.on('response', function(res) {
    console.log(res);
  });

  return


  console.log('Gathering events for ' + pages_data[0].url + ' with Node_id ' + pages_data[0].node_id);

  body.queries = '%257B%2522q0%2522%253A%257B%2522priority%2522%253A0%252C%2522q%2522%253A%2522Query%2520TimelineEventsCalendarRoute%2520%257Bnode(1446231682259516)%2520%257Bid%252C__typename%252C%2540F7%257D%257D%2520QueryFragment%2520F0%2520%253A%2520Page%2520%257Bid%252Cname%252Curl%252Cis_owned%257D%2520QueryFragment%2520F1%2520%253A%2520Node%2520%257Bid%252C__typename%257D%2520QueryFragment%2520F2%2520%253A%2520Event%2520%257Bid%252Cname%252Curl%257D%2520QueryFragment%2520F3%2520%253A%2520Event%2520%257Bid%252Cviewer_watch_status%252Cconnection_style%252Cevent_viewer_capability%2520%257Bis_viewer_admin%252Ccan_viewer_edit%252Ccan_viewer_join%252Ccan_viewer_promote%257D%257D%2520QueryFragment%2520F4%2520%253A%2520Event%2520%257Bid%252Cviewer_guest_status%252Cevent_buy_ticket_url%252Cconnection_style%252Cevent_viewer_capability%2520%257Bis_viewer_admin%252Cis_viewer_admin.enable_business_permissions(false)%2520as%2520_is_viewer_admin1hS8xA%252Ccan_viewer_edit%252Ccan_viewer_share%252Ccan_viewer_join%257D%252Cevent_creator%2520%257Bid%252C__typename%257D%252Cis_canceled%252C%2540F3%257D%2520QueryFragment%2520F5%2520%253A%2520Event%2520%257Bid%252Ctime_range%2520%257Bstart%257D%252Cis_event_draft%252Cscheduled_publish_timestamp%252Cstart_time_sentence.format(SHORT_TIME_LABEL)%2520as%2520_start_time_sentenceiczKr%252Csuggested_event_context_sentence.show_category(false)%2520as%2520_suggested_event_context_sentence2eg3eg%2520%257Btext%257D%252Cevent_place%2520%257Bcontextual_name%252Ccity%2520%257Bcontextual_name%252Cid%257D%252C__typename%252C%2540F0%252C%2540F1%257D%252Cevent_viewer_capability%2520%257Bis_viewer_admin%257D%252Cis_canceled%252C%2540F2%252C%2540F4%257D%2520QueryFragment%2520F6%2520%253A%2520Page%2520%257Bid%252Cviewer_profile_permissions%252Cadmin_info%2520%257Bis_viewer_business_manager_admin%257D%257D%2520QueryFragment%2520F7%2520%253A%2520Page%2520%257Bid%252Cname%252Cviewer_profile_permissions%252Call_owned_events.upcoming(true).allowed_states(CANCELED%252CDRAFT%252CSCHEDULED_DRAFT_FOR_PUBLICATION%252CPUBLISHED).filter_out_canceled_events_if_not_connected(true).first(10)%2520as%2520_all_owned_events12JYfp%2520%257Bedges%2520%257Bis_hidden_on_profile_calendar%252Cis_added_to_profile_calendar%252Cnode%2520%257Bid%252Ctime_range%2520%257Bstart%257D%252C%2540F5%257D%252Ccursor%257D%252Cpage_info%2520%257Bhas_next_page%252Chas_previous_page%257D%257D%252Call_owned_events.past(true).allowed_states(CANCELED%252CDRAFT%252CSCHEDULED_DRAFT_FOR_PUBLICATION%252CPUBLISHED).filter_out_canceled_events_if_not_connected(true).first(10)%2520as%2520_all_owned_events2fwm0O%2520%257Bedges%2520%257Bis_hidden_on_profile_calendar%252Cis_added_to_profile_calendar%252Cnode%2520%257Bid%252Ctime_range%2520%257Bstart%257D%252C%2540F5%257D%252Ccursor%257D%252Cpage_info%2520%257Bhas_next_page%252Chas_previous_page%257D%257D%252C%2540F6%257D%2522%252C%2522query_params%2522%253A%257B%257D%257D%257D';

  var formDataa = querystring.stringify(body);
  theOptions.form = formDataa;

  request(theOptions, function(error, response, data) {
    console.log('data: ', data);

    if (!error) {
      //var event_data = JSON.parse(data);
      var event_data = data;
      events.push(event_data);

      done = done + 1;
      if (done === pages_data.length - 1) {
        saveEventsData();
      }
    }

  });

}





function saveEventsData() {
  fs.appendFile('events_new.json', JSON.stringify(events, null, 4), function(err){
    console.log('Saved events to events_new.json');
  });
}