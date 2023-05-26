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
    
    
    def get_api_setting(self):
        with open('config/config.toml', 'rb') as toml_file:    
            config = tomllib.load(toml_file)
            self.apikey = config.get('news_api')['apikey']
            self.apiurl = config.get('news_api')['url']
            return self
    
    
    def email_setting(self):
        with open('config/config.toml', 'rb') as toml_file:    
            config = tomllib.load(toml_file)
            self.email_backend = config.get('email_setting')['email_backend']
            self.email_host = config.get('email_setting')['email_host']
            self.email_port = config.get('email_setting')['email_port']
            self.email_host_user = config.get('email_setting')['email_host_user']
            self.email_host_password = config.get('email_setting')['email_host_password']
            self.email_use_tls = config.get('email_setting')['email_use_tls']
            self.subject = config.get('email_setting')['subject']
            self.message = config.get('email_setting')['message']
            self.from_email = config.get('email_setting')['from_email']
            self.recipient_list = config.get('email_setting')['recipient_list']
            return self