# Usage
### Redis
```bash
docker run -p 6379:6379 -d redis:2.8  
```
* to stop a running redis instance
```bash
/etc/init.d/redis-server stop 
```
### Django Backend
> /backend
```bash
source env/bin/activate 
```
> /backend/src
```bash
python manage.py runserver
```
### React Frontend
> /frontend
```bash
npm start
```