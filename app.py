from flask import Flask

from genre.views import genre_blp
from main.views import main_blp, main_blp_exception_prefix
from rating.views import rating_blp

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Регистрация блюпринта main
app.register_blueprint(main_blp)
# Регистрация блюпринта main исключения (для чего он указано в main.views)
app.register_blueprint(main_blp_exception_prefix)
# Регистрация блюпринта rating
app.register_blueprint(rating_blp)
# Регистрация блюпринта genre
app.register_blueprint(genre_blp)

if __name__ == '__main__':
    app.run()
