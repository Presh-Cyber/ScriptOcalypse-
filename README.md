# 🏴‍☠️ ScriptOcalypse: Swagfleet  

⚡ **Nothing here… just a lot of weird ideas with a chaotic mix of caffeine, frustration, and automation that somehow work.**  

## 🚀 Features  
✅ Supports **OpenAPI 3.x** (servers) & **Swagger 2.0** (host, basePath, schemes)  
✅ Allows **optional domain replacement** for easy external testing  
✅ **Automatically tests** endpoint responses (200, 404, etc.) for quick insights  
✅ Seamless **integration with BurpSuite** for smooth proxying  

## 📜 Usage  

Extract API endpoints from a Swagger JSON:  

```sh
python3 swagfleet.py -u <swagger_json_url> 



Replace domain for external testing:
```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com


Enable SSL certificate verification (default is disabled)
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com --verify


Check if endpoints return a 200 or 404 status.
```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com --check


Proxy URL to route requests through Brupsuit. Can only be used with --check.
```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com --proxy 127.0.0.1



## 🛠 Installation

```sh
pip install -r requirements.txt


## ☕ Contribute
If you think you can add more chaos to this madness, fork it & PR it 😈
