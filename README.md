# Columbia Events Calendar


Synopsis

  There are many groups on Facebook that are associated with Columbia University, which makes it difficult for a user to search through all of the available events to find one that they might be interested in. Our hypothesis is that a unified event calendar of all Columbia events would make it easier for students, faculty and staff to find such events, based on key search terms, or a specific date and time. 
  The Columbia Events Calendar will be focused around a visual calendar of events aggregated from the Facebook API along with facebook groups within the Columbia University community. This program will allow users to quickly view and obtain details about an event’s location, date, time, and hosts. Additionally, it will provide users with the ability to search and filter through events by date, location, and organization/host. A user will also be able to leave ratings on past events that are tied to their profile. These events’ ratings will be used to calculate an average rating for the group that they were posted by, which will give users a better suggestion of the groups and events which they might want to attend in the future. 

Technology
Frontend: SASS, React, Bootstrap
Backend: Postgres, Python, Flask

User Stories

Title: Create User / Login
Description: As a new user, I want to create an account to use the application. As an existing user, I want to log into my existing account. 

Title: Create User / Login - Error Cases
Description: As a new user, I want to be informed of the reasons for my being unable to register and/or login, due to missing or invalid account status or credentials. 

Title: Browse Event
Description: As a user, I want to browse the public events that are happening in the Columbia University community.

Title: Filter Event
Description: As a user, I want to filter the type of events happening on campus. This means that I can filter events based on dates, times, and organization hosting the event.

Title: Search Event
Description: As a user, I want to search the event based on the name of the event and the organization hosting the event.

Title: Rate Event/Groups1
Description: As a user, I can rate any of the events. Each hosting group will have a rating based on the rating of the events they have held in the past.

Title: Favorite Event
Description: As a user, I can add events to my favorite list by clicking a little star button.
