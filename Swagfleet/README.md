# Swagfleet  

⚡ Tired of wrestling with pentest with Swagger docs and manually updating API endpoints? Swagfleet does the dirty work for you extracting, replacing, and testing all discovered endpoints. It seamlessly integrates with BurpSuite, making your pentesting workflow smoother. and if you're hunting for juicy GET endpoints that scream "exploit me!", thorugh Authentication bypasses? this script got it covered. **  

## 🚀 Features  
✅ Supports **OpenAPI 3.x** (servers) & **Swagger 2.0** (host, basePath, schemes)  
✅ Allows **optional domain replacement** for easy external testing  
✅ **Automatically tests** endpoint responses (200, 404, etc.) for quick insights  
✅ Seamless **integration with BurpSuite** for smooth proxying  

## 🛠 Installation
If you're looking for an installation guide, you clearly haven't been in this game long enough... but fine, here you go:
```sh
pip install -r requirements.txt
```

## 📜 Usage  

Extract API endpoints from a Swagger JSON:  

```sh
python3 swagfleet.py -u <swagger_json_url> 
```

Replace domain for external testing:

```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com
```

Enable SSL certificate verification (default is disabled)
```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com --verify
```

Check if endpoints return a 200 or 404 status.
```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com --check
```

Proxy URL to route requests through Brupsuit. Can only be used with --check.
```sh
python3 swagfleet.py -u <swagger_json_url> -d new.domain.com --proxy 127.0.0.1:8080
```

## ☕ Contribute
If you think you can add more chaos to this madness, fork it & PR it 😈
