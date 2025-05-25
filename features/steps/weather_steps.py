from behave import given, when, then
import requests

@given('I provide the city name as "{city}"')
def step_impl(context, city):
    context.city = city
    print("this is city: ", city)

@when('I call the weather API')
def step_impl(context):
    api_key = "f25d9d5e076475d13d6182163535ccd3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={context.city}&appid={api_key}&units=metric"
    context.response = requests.get(url)
    context.response_json = context.response.json()
    print("url:", url)

@then('the response status code should be 200')
def then_status_code(context):
    assert context.response.status_code == 200
    

@then('I should get the current temperature')
def step_impl(context):
    data = context.response.json()
    assert 'main' in data and 'temp' in data['main']

@then('the response status code should be 404')
def then_status_code(context):
    assert context.response.status_code == 404
    


