from  git import Repo
import os
import logging
import shutil


def IsWorkspaceAvailable(workspace_name):
    check_result = os.path.isdir(workspace_name)
    if check_result == True:
        logging.info("Workspace Exists so removing it")
        shutil.rmtree(workspace_name)


def GitClone(git_url, user_name, access_token=None, branch_name=None):
    ''''''
    if access_token == None:
        raise Exception("Token cannot be None")
    else:
        IsWorkspaceAvailable("dbt_workspace")
        url_after_split = git_url.split("@")[1]
        Repo.clone_from(f"https://{user_name}:{access_token}@{url_after_split}", 'dbt_workspace', branch=branch_name)

if __name__ == '__main__':
    GitClone("https://sarojdongol@bitbucket.org/cartiga/cartiga_dw.git","sarojdongol","zgqdr93kXMuVDcJrxDTQ","silvertbl/accountfirm")
