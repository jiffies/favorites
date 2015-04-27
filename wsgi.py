from favorites import create_app
import os

env = os.environ.get('FAVORITES_ENV', 'prod')
app = create_app('favorites.config_%s.%sConfig' % (env,env.capitalize()), env=env)
