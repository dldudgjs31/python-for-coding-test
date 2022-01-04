#!/bin/sh

/root/bin/git config --global user.name dldudgjs31
/root/bin/git config --global user.email dldudgjs31@naver.com
/root/bin/git config --global user.mail dldudgjs31@naver.com
/root/bin/git config --list > /root/silk/python-for-coding-test/git_id_check

cd /root/silk/python-for-coding-test/

/root/bin/git add .

/root/bin/git checkout -b main

/root/bin/git add .

eval $(ssh-agent -s)

ssh-add ~/.ssh/lee
read -p "commit message : " message
/root/bin/git commit -am "(코테문제풀이) $message" 

/root/bin/git push --set-upstream origin main

