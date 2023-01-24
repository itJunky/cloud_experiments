
## INSTALL

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requiremnts.txt
python3 create_db.py
```
If need mysql, just run it on localhost:
```
docker run --name mysql -d
	-p 3306:3306
	-e MYSQL_ROOT_PASSWORD=change-me
	--restart unless-stopped
	mysql:8
```

## RUN

```
python3 generator.py
```

