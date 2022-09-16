  
#!/bin/sh
# code from https://github.com/jupyterhub/oauthenticator/tree/master/examples/full

IFS="
"
for line in `cat userlist`; do
  test -z "$line" && continue
  user=`echo $line | cut -f 1 -d','`
  echo "adding user $user"
  useradd -m -s /bin/bash $user
 # cp -r /srv/ipython/examples /home/$user/examples
  chown -R $user /home/$user
done