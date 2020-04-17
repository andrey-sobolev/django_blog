### **blog_restapi**

For run django project you should set environments variables:

`HUNTERIO_API_KEY`
`CLEARBIT_PUBLIC_KEY`
`CLEARBIT_SECRET_KEY`

you can use `.env` file in blog_restapi main folder.

Clearbit API running with celery, for start it you should install redis and run additional worker:

`celery worker -A config --loglevel=debug --concurrency=1 -B `  

### **post_bot**

You could config bot using `config.ini` file;


Users credentials for sign_up are stored in `data/users.json` file;


Text for new posts are stored in `data/posts.json` file;

