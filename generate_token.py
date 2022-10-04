import requests
from selenium.webdriver.common.by import By
from browser import Browser

class Generate_token(Browser):
    HOST='https://accounts.spotify.com'
    CLIENT_ID='f527f1ce83234cf7bc52c45ce5059072'
    CLIENT_SECRET='13462cbad7cd4472973540fa76c90bc3'
    RESPONSE_TYPE='code'
    REDIR_URI='http://estDavid://callback'
    ENCODED_REDIR_URI='http%3A%2F%2FestDavid%3A%2F%2Fcallback'
    SCOPE='ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private'
    USER_NAME=(By.ID, 'login-username')
    PASSWORD=(By.ID, 'login-password')
    BUTTON=(By.ID, 'login-button')
    AGREE_BUTTON = (By.CLASS_NAME, "jWBSO")
    GRANT_TYPE='authorization_code'


    def create_auth_endpoint(self):
        endpoint=self.HOST+'/authorize?client_id='+self.CLIENT_ID+'&response_type='+self.RESPONSE_TYPE+'&redirect_uri='+self.ENCODED_REDIR_URI+'&scope='+self.SCOPE
        return endpoint

    def load_endpoint(self):
        self.chrome.get(self.create_auth_endpoint())

    def login2spotify(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('david.mondoc@gmail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('9$NW_t@7gRVi=vb')
        self.chrome.find_element(*self.BUTTON).click()

    def authorize_login(self):
        self.chrome.find_element(*self.AGREE_BUTTON).click()

    def get_code(self):
        URL=self.chrome.current_url
        code=URL[URL.index('=')+1:]
        return code

    def get_tkn(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data={'code':self.get_code(),
              'redirect_uri':self.REDIR_URI,
              'client_id':self.CLIENT_ID,
              'client_secret':self.CLIENT_SECRET,
              'grant_type':self.GRANT_TYPE}
        response=requests.post(self.HOST + '/api/token', data=data, headers=header)
        return response.json()['access_token']

    @staticmethod
    def authorization(self):
        self.create_auth_endpoint()
        self.load_endpoint()
        self.login2spotify()
        try:
            self.authorize_login()
            token=self.get_tkn()
        except:
            token=self.get_tkn()
        return f'Bearer {token}'


