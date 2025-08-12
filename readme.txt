# in this project, i have developed a github actions to activate on push
# once activated, the git hub actions will build the docker image, push onto the docker hub automatically 
# to create docker image cmd = docker build -t rohithkumar124/retail_app
# to run container cmd = docker run -p 5000:5000 rohithkumar124/retail_app
# to push image to docker hub cmd = docker push rohithkumar124/retail_app
# to create a github repository and push all files to github repo, follow below steps
# git init
# git add .
# git commit -m "any comment"
# gh repo create repo_name --public --source=. --remote=origin --push