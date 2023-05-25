import tomllib
config_filepath = 'config/config.toml'

class MyConfigClass:
    def __init__(self):
        # Initialize any required resources or dependencies here
        pass
    
    
    def get_database(self):
        with open('config/config.toml', 'rb') as toml_file:    
            config = tomllib.load(toml_file)
            self.engine = config.get('database')['engine']
            self.name = config.get('database')['name']
            self.user = config.get('database')['user']
            self.password = config.get('database')['password']
            self.host = config.get('database')['host']
            self.port = config.get('database')['port']
            return self
        
        
    def get_setting(self):
        with open('config/config.toml', 'rb') as toml_file:    
            config = tomllib.load(toml_file)
            self.image_size = config.get('image_validation')['image_size']
            self.image_formats = config.get('image_validation')['image_formats']
            self.image_size_error = config.get('image_validation')['image_size_error']
            self.image_format_error = config.get('image_validation')['image_format_error']
            return self
    
    
    def get_apisetting(self):
        with open('config/config.toml', 'rb') as toml_file:    
            config = tomllib.load(toml_file)
            self.apikey = config.get('newsapi')['apikey']
            self.apiurl = config.get('newsapi')['url']
            return self