import requests
import pytest

@pytest.fixture
def global_var():
    pytest.global_var=0

def test_get():
    response = requests.get('https://api.planet.com/data/v1/searches',
                            headers={'authorization': 'api-key ab2118c30721496495ddc8d4f3603d69'})
    assert response.status_code == 200

def test_created():
    url = 'https://api.planet.com/data/v1/searches'
    headers = {'authorization': 'api-key ab2118c30721496495ddc8d4f3603d69', 'Content-Type': 'application/json'}
    response = requests.post(url, data = open('postData.json', 'rb'), headers=headers)
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict['search_type'] == 'saved'
    pytest.global_var = response_dict['id']

def test_updated():
    url = 'https://api.planet.com/data/v1/searches/{}'.format(pytest.global_var)
    headers = {'authorization': 'api-key ab2118c30721496495ddc8d4f3603d69', 'Content-Type': 'application/json'}
    response = requests.put(url, data = open('putData.json', 'rb'), headers=headers)
    assert response.status_code == 200
    respone_dict = response.json()
    assert respone_dict['name'] == 'Ashvini_test_1.3'

def test_post_invalidDiscriminator():
    url = 'https://api.planet.com/data/v1/searches'
    headers = {'authorization': 'api-key ab2118c30721496495ddc8d4f3603d69', 'Content-Type': 'application/json'}
    response = requests.post(url, data = open('postInvalidData.json', 'rb'), headers=headers)
    assert response.status_code == 400
    respone_dict = response.json()
    assert respone_dict['field']['filter.config.0.type'][0]['message'] == 'Dummy is not a valid type for discriminator'

def test_put_invalidRangeFilter():
    url = 'https://api.planet.com/data/v1/searches/{}'.format(pytest.global_var)
    headers = {'authorization': 'api-key ab2118c30721496495ddc8d4f3603d69', 'Content-Type': 'application/json'}
    response = requests.put(url, data = open('putInvalidData.json', 'rb'), headers=headers)
    assert response.status_code == 400
    respone_dict = response.json()
    assert respone_dict['field']['filter.config.0.config.gt'][0]['message'] == "'abc@' is not of type 'number'"



