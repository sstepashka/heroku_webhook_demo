Install heroku CLI from https://devcenter.heroku.com/articles/heroku-command-line

$ heroku login
$ heroku create <project_name>
$ cd <path to current directory>
$ git init
$ git add --all
$ git commit -m "Initial commit"
$ heroku git:remote --app <project_name>
$ git push heroku master

$ heroku logs --app <project_name> --source app --tail
$ curl -S POST -d '{}' https://<project_name>.herokuapp.com/webhook