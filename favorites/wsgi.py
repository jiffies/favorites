from favorites import create_app
import os

env = os.environ.get('FAVORITES_ENV', 'dev')
app = create_app('favorites.settings.%sConfig' % env.capitalize(), env=env)
