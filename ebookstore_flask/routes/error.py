from flask import Blueprint, render_template

error = Blueprint('error', __name__)
@error.app_errorhandler(404)
def not_found_error(error):
   return render_template(
      "user/error.html",
      error_code=404,
      error_message="Oops! Page Not Found",
      error_description="The page you are looking for does not exist."
   ), 404

@error.app_errorhandler(403)
def forbidden_error(error):
   return render_template(
      "user/error.html",
      error_code=403,
      error_message="Oops! Access Denied",
      error_description="You do not have permission to access this page."
   ), 403