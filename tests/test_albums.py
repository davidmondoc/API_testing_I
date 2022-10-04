from requests.albume.get_album import get_albums


class Albums():
    def test_get_album_exists(self):
        request_response=get_albums('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert request_response.status_code == 200
