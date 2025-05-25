import requests
from behave import given, when, then

@given('the country name is "{country_name}"')
def given_country_name(context, country_name):
    context.country_name = country_name
    print("country name: ", country_name)

@when('I fetch data from the REST Countries API')
def when_fetch_data(context):
    url = f"https://restcountries.com/v3.1/name/{context.country_name}"
    context.response = requests.get(url)
    context.response_json = context.response.json()

@then('the API response status code should be {status_code:d}')
def then_status_code(context, status_code):
    assert context.response.status_code == status_code

@then('the country capital should be "{expected_capital}"')
def then_check_capital(context, expected_capital):
    capital = context.response_json[0]['capital'][0]
    assert capital == expected_capital
