import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services.live_weather_service import get_live_report

router = fastapi.APIRouter()


@router.get('/api/umbrella', response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()) -> UmbrellaStatus:
    data = await get_live_report(location)

    #print(data)
    #{'weather': {'description': 'few clouds', 'category': 'Clouds'}, 'wind': {'speed': 3.44, 'deg': 230}, 'units': 'imperial', 'forecast': {'temp': 49.89, 'feels_like': 49.17, 'pressure': 1022, 'humidity': 88, 'low': 45, 'high': 53}, 'location': {'city': 'Portland', 'state': None, 'country': 'US'}, 'rate_limiting': {'unique_lookups_remaining': 48, 'lookup_reset_window': '1 hour'}}


    weather = data.get('weather', {})
    category = weather.get('category', 'UNKNOWN')

    forcast = data.get('forecast', {})
    temp = forcast.get("temp", -999.999)

    bring = category.lower().strip() in {'rain', 'mist'}

    return UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)
