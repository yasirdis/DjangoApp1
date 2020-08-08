# DjangoApp1
DRF 3.11.0/Python 3.8.3 /Django 3.0.3 Frame work

1.	Programming Language used Python 3.8.3 with Django 3.0.3 Frame work.
2.	Django Rest Framework is used in order to build API.
3.	Project Name is “usersActivityPeriod” and Application name is “app”.
4.	Inside app/model.py two models (Members and Activity_periods) are created in order to store data. A foreign key (member) is used in Activity_periods model to refer member instance. 
5.	Inside app/management/commands a script (populate_db.py) is written for custom management command to populate the database with some dummy data. By typing command 
python manage.py populate_db
you will populate database by fake data. Keep in mind this command will store only one member with two activity periods at one time. To store more users you need to run this command again and again.
6.	Inside app/serializers.py models are serialized in order to convert required models data in JSON format.
7.	Inside app/views.py APIView based call is created that receives request from user and data in the form of JSON to user.
Follow these steps to run this project:
1.	Go to directory usersActivityPeriod.
2.	 Run this command “python manage.py populate_db” to populate database by dummy data.
By running at one time only one random member will get stored with two activity period records. If you want more than one members you need to run this command again and again.
3.	Next run this command “python manage.py runserver” in order to run server.
4.	Super User Username is “root” and Password is “Password”
5.	In last step user can enter this  http://127.0.0.1:8000/members/ to send request and receive data in the form of JSON as shown in example below:
[
    {
        "id": "Sm8jZ8ITu",
        "real_name": "Lisa Anderson MD",
        "tz": "America/Santo_Domingo",
        "activity_periods": [
            {
                "start_time": "2005-01-05 06:48:32PM",
                "end_time": "2005-01-05 07:10:35AM"
            },
            {
                "start_time": "1995-09-15 11:36:13AM",
                "end_time": "1995-09-15 00:46:00PM"
            }
        ]
    },
    {
        "id": "Qhe8avCHk",
        "real_name": "Vanessa Johnson",
        "tz": "Asia/Qyzylorda",
        "activity_periods": [
            {
                "start_time": "2017-09-23 00:37:31PM",
                "end_time": "2017-09-23 01:27:28AM"
            },
            {
                "start_time": "1997-01-15 09:05:57PM",
                "end_time": "1997-01-15 09:58:36PM"
            }
        ]
    },
    {
        "id": "bNTVLbyk9",
        "real_name": "Robert Hughes",
        "tz": "Africa/Harare",
        "activity_periods": [
            {
                "start_time": "1999-11-25 08:29:27PM",
                "end_time": "1999-11-25 14:43:48AM"
            },
            {
                "start_time": "1987-02-18 07:11:57PM",
                "end_time": "1987-02-18 14:15:27AM"
            }
        ]
    }
]



	
	
