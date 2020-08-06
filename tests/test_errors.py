
def test_error_handler(client):
    rv = client.get('/asd1as16')
    assert b'File Not Found' in rv.data