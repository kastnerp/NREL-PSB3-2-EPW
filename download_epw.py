from assets import download_epw


lat, lon = 42.434269, -76.500354
location = "Ithaca"
year = '2019'
attributes = 'air_temperature,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,dhi,dni,fill_flag,ghi,relative_humidity,solar_zenith_angle,surface_albedo,surface_pressure,total_precipitable_water,wind_direction,wind_speed,ghuv-280-400,ghuv-295-385'

interval = '60'
utc = 'false'
your_name = "Patrick+Kastner"
api_key_file = open("api_key", 'r')
api_key = api_key_file.readline()
reason_for_use = 'beta+testing'
your_affiliation = 'aaa'
your_email = "pk373@cornell.edu"
mailing_list = 'false'
leap_year = 'true'

download_epw(lat, lon,year, location,  attributes,  interval, utc, your_name, api_key,reason_for_use, your_affiliation, your_email, mailing_list, leap_year)
