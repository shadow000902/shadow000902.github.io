Commit_Docs=$1

hexo clean
git add .
if [ ! -n "$Commit_Docs" ];
then
    git commit -m "Updates Docs"
else
    git commit -m "$Commit_Docs"
fi
git push