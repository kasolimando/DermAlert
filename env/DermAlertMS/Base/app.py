from flask import Flask
from DermAlertMS_Infrastructure.Settings.Config import config
from flask_injector import FlaskInjector,singleton
from DermAlertMS_Infrastructure.Database.DermAlertDBContext import DermAlertDBContext
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS.Controllers import PatientController, AdminController, UniversityController,DegreeController, SpecialityController
from DermAlertMS.Controllers import SurveyController, RecommendationController,PersonController

app = Flask(__name__)

app.config.from_object(config['development'])

app.register_blueprint(PatientController.patients, url_prefix='/patients')
app.register_blueprint(AdminController.admin, url_prefix='/admin')
app.register_blueprint(UniversityController.university, url_prefix='/universities')
app.register_blueprint(DegreeController.degrees, url_prefix='/degrees')
app.register_blueprint(SpecialityController.specialities, url_prefix='/specialities')
app.register_blueprint(SurveyController.surveys, url_prefix='/surveys')
app.register_blueprint(RecommendationController.recommendations, url_prefix='/recommendations')
app.register_blueprint(PersonController.people, url_prefix='/people')

def configure(binder):
    binder.bind(IDermAlertDBContext, to=DermAlertDBContext(app),scope=singleton)

if __name__ == '__main__':
    FlaskInjector(app=app, modules=[configure])
    app.run()