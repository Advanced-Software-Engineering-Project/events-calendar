# Component 1: Rating

Dated: Nov. 30, 2016

### Info
* Files: 
```
events/script.js,
events/rate.js, 
events/index.html, 
events/sty.css
```
* Reader: Shanqing
* Recorder: Priscilla

### How it works
* Starrr object shows the rating. 
* Javascript: when it detects the change in the starrr (user rates)
* Open source library on github (rate.js)
* Using jQuery to append glyphicon using some logic
* “Date-rating” default rating of event that we get from backend. 
* When user enter event page, they can see the rating there
* On “hover”, it changes the color and applies to the stars before
* On “click”, it sets the rating

### Additional problems
* Right now, it is showing user rating until we refresh. How do we indicate that they have rated it? After users rate a group, should the rating for that be displaying the rating by the user? Or the average rating

* (Fixed) Backend should detect when it has always been rated. We should not allow users to rate things again
