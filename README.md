# Crispy Feed
<hr>
Crispy Feed is a news thread, similar to a site we have in sweden called flashback where you literally can post anything that might be an interesting topic or information etc.
The idea is to be able to have an own user to log in with an interact with others but also post stuff that is on your mind
<hr>

![image](https://user-images.githubusercontent.com/95358346/179372630-a64777b4-8f30-4285-8359-b1fdd8030aca.png)

## Features
- Navigation bar 
Existing on both the Feed page and also the post details page.
It will also change weather you are an authenticaded user or if you are just visting the page as a guest.
You will be able to post something via the button in the navbar if you are logged in.
As a guest you will be able to register a new account.
As a logged in user you will be able to also logout if you wish.

![image](https://user-images.githubusercontent.com/95358346/179365781-ea4734a3-fa09-48a4-b377-622a111971ba.png)

## The Feed 
Here you can easily see what others have posted and click on each post, to view them in more detail.

The Feed is made with bootstrap, very basic and clean design with some box shadowing to make each post pop out a bit more.
I have included some fav icons as i thought it made the whole image of the page more pleasent.

![image](https://user-images.githubusercontent.com/95358346/179365851-b5cc2305-c902-4b3b-ac09-e00e71b6691d.png)

## Post details page
This page allows the user to interact with the feed, they can comment and also view the full content of the post.
If you are the author of a post you will be able to both edit and delete the post.

![image](https://user-images.githubusercontent.com/95358346/179366048-426daacd-e64f-43e9-866e-5401e94ed161.png)

## Login and register pages
This allows the user to login to their existing account or if they do not have one they can go on to register an new account in order to be a part 
of the community

![image](https://user-images.githubusercontent.com/95358346/179366191-a414c279-80dc-4915-bc6d-568cb054f856.png)
![image](https://user-images.githubusercontent.com/95358346/179366201-1a4e8e2d-dac4-474e-9ab9-b23fec2cfe5e.png)

## Footer 
The footer is more here for good looking reasons than funcionality.
It allows users to visit The Crispy Feeds social media accounts and navigate back to the homescreen.

!![image](https://user-images.githubusercontent.com/95358346/179366336-9eeb25d5-5e83-40c8-a5bc-ebda10824891.png)

## Future goals 
The implementations i can think of would be:
Allow users to follow a thread more in depth, where you could start a thread and people could participate in a more
natural way.
post pictures and videos would be another, to have more of a dynamic page.
Upvote and downvote things could also be one.
Finally creating a whole community with something of value you get when you sign up
to get more people to join, and then have discrete adds on the page.
I would also want people to be able to follow one and another to make friends and tie up the community better.


# Deployment
- The site was deployed to heroku


# Technology 

## Languages
- Html
- Css
- Python

## Frameworks
- Django
- Bootstrap

## Tools
- Heroku
- Github
- Postgres


## Model Tables:

### Post Model
| POST         |           |     |   |   |
|--------------|-----------|-----|---|---|
| author       | User      | FK  |   |   |
| title        | CharField |     |   |   |
| content      | TextField |     |   |   |
| created_date | DateTime  |     |   |   |
| updated_date | DateTime  |     |   |   |
| likes        | User      | M2M |   |   |

### Comment Model

| COMMENT      |      |     |   |   |
|--------------|------|-----|---|---|
| post         | Post | FK  |   |   |
| author       | User | FK  |   |   |
| content      |      |     |   |   |
| created_date |      |     |   |   |
| updated_date |      |     |   |   |
| likes        | User | M2M |   |   |


# Testing
## Manual Testing
All of the crud functionality and user stories are tested and are working properly, i have tested that manually.
at first i ran in to some trouble with the edit_post page (U in Crud), i did a mistake in my views that caused everything to load
properly but did not make the POST correctly to the database.
so to fix this it was simply to add this line of code ![image](https://user-images.githubusercontent.com/95358346/179372290-28782006-3947-478f-86c5-6c39a48c4c55.png)

Another thing that was tested was the ability to log in and log out, this was something that did not work at first due to me
commiting a simple mistake, i missed the URL ![image](https://user-images.githubusercontent.com/95358346/179372217-c17551b6-7f2f-41cb-8863-fb3b5be7e2ac.png) at the end so it would not work as expected, after rewriting a whole bunch of other things i finally found this when 
i was going through allauth documentation.

# Credits

## Media
The only media i have used is a bit of fav icons for the logo and also the example posts on the site is from https://www.lipsum.com/ 

## Content 
Code institute
Dennis ivy
Microsoft developer

I can not say that i have taken any code from them but i surely did learn some important logic from the channels that are listed abow.



