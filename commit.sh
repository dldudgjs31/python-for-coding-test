#!/bin/sh

git config --global user.name dldudgjs31
git config --global user.email dldudgjs31@naver.com
git config --global user.mail dldudgjs31@naver.com

git add .

git checkout -b main

read -p "commit message : " message
git commit -am "(코테문제풀이) $message" 

git push --set-upstream origin main

