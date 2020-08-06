def generate(client):
    return client.post('/tools/hieroglyph/generate', data=dict(stiffness=4), follow_redirects=True)


def test_image_generated(client):
    rv = generate(client)
    assert b'</svg>' in rv.data


def test_files_removed_after_image_generated(client):
    generate(client)
    import os
    if os.path.exists('./app/tmp'):
        assert len(os.listdir('./app/tmp')) == 0
