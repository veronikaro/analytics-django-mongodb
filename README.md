
This project holds code of a simple reporting Django application. In this project, the following tools are used:
* [Django](https://www.djangoproject.com/) - a Python web framework
* [MongoDB database](https://www.mongodb.com/)
* [Flexmonster Pivot Table & Charts](https://www.flexmonster.com/?r=gt_dj_m) - a front-end library for data visualization
* [The MongoDB connector by Flexmonster](https://www.flexmonster.com/doc/mongodb-connector/?r=gt_dj_m)

To successfully run the project, do the following:

* Download / clone this GitHub sample
* Download [the MongoDB connector](https://github.com/flexmonster/pivot-mongo) and set it up by following the instructions from the [guide](https://www.flexmonster.com/doc/how-to-connect-to-mongodb/?r=gt_dj_m). 
* In `django_reporting_project/dashboard/templates/your_report.html`, specify the name of the MongoDB collection to which to connect from the pivot table.
* Run the MongoDB connector
* Run the Django development server:
`python manage.py runserver`
* Open `http://127.0.0.1:8000/report/` and choose the report on the navigation bar.

More details can be found in the freeCodeCamp tutorial. 

