# 1. Check for any vaccine.py and delete if any.
# 2. Verify that the userSetup.py is not infected, if so rename to userSetup.backup and notify user (email)
# 3. Change ~/maya/script/ folder permissions to read only using os.chmod ? 
# 4. Create scriptJob:

def remove_unwanted_script_nodes():
   # Delete unwanted scriptNodes
   # Restore ~/maya/script/ folder permissions using os.chmod?
   # remove the script node -> cmds.scriptJob(kill=temp_script_job)

temp_script_job = cmds.scriptJob(e=("SceneOpened", remove_unwanted_script_nodes))
