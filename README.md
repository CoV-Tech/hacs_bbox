# Fork from [Earion68/hass_custom_bbox](https://github.com/earion68/hass_custom_bbox)
## ChangeLog
### 0.0.3
- Added new Entity: `last_error`
- Instead of failing to initialize (the random 400 errors on login), 
  the returned values are now `None` and `last_error` is set to the exception thrown.

### 0.0.2
- Added HACS information.  
- Fixed component on Home Assistant 2025.1.1

## Tested using:

| Home Assistant Version | BBox Version | Plugin Version |
|------------------------|--------------|----------------|
| 2025.1.2               | 23.7.12      | 0.0.3          |
| 2025.1.1               | 23.7.12      | 0.0.2          |
| 2024.12.3              | ?            | 0.0.1          |
| 2024.11.3              | 23.7.12      | 0.0.1          |

## Installation:
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=CoV-Tech&repository=hacs_bbox&category=intergration)

**OR**

* Open HACS
* Open the menu on the top right
* Add a custom repository:
  - Repository: https://github.com/CoV-Tech/hacs_bbox
  - Type: integration
* Search for Bbox and install


## Configuration:
* Add the configuration to `/homeassistant/configuration.yaml`:
```yaml
device_tracker:
  - platform: custom_bbox
    host: mabbox.bytel.fr
    password: !secret bbox_password

sensor:
  - platform: custom_bbox
    password: !secret bbox_password
    host: mabbox.bytel.fr
    monitored_variables:
      - down_max_bandwidth
      - up_max_bandwidth
      - current_down_bandwidth
      - current_up_bandwidth
      - uptime
      - number_of_reboots
      - last_error
```
* Add the password to `/homeassistant/secrets.yaml`
```yaml
bbox_password: "YOUR_BBOX_PASSWORD_HERE"
```

# Original README:
## hass_custom_bbox
Custom Home Assistant integration for Bbox

Based on Home Assistant Bbox integration: https://www.home-assistant.io/integrations/bbox and PyBbox: https://github.com/HydrelioxGitHub/pybbox

Merged both codes into one custom component to solve:
- the SSL DH_KEY_TOO_SMALL issue arising from Home Assistant 2022.7 which uses an up-to-date version of OpenSSL with higher security requirements and for which Bouygues Telecom did not update the firmware.
- deprecated constants to be removed in 2025.1
- the Bbox firmware 23.7.8 which systematically requires login to the API

### Breaking changes
- The last version fixing the firmware 23.7.8 makes the "password" key in the configuration mandatory.
- The default host, if not mentioned, will be mabbox.bytel.fr

### Usage:
- download all files in a new folder named "custom_bbox" under "custom_components" of the Home Assistant config folder (example: /config/custom_components/custom_bbox)
- instanciate the custom component in configuration.yaml as below:

```yaml
device_tracker:
- platform: custom_bbox
  password: YOUR_BBOX_PASSWORD_HERE # mandatory
  host: mabbox.bytel.fr # optional, some users reported it should not be added when using a different subnet (10.x.x.x)
  
sensor:
  - platform: custom_bbox
    password: YOUR_BBOX_PASSWORD_HERE # mandatory
    host: mabbox.bytel.fr  # optional, some users reported it should not be added when using a different subnet (10.x.x.x)
    monitored_variables: # pick the sensors you need below
      - down_max_bandwidth
      - up_max_bandwidth
      - current_down_bandwidth
      - current_up_bandwidth
      - uptime
      - number_of_reboots
```
