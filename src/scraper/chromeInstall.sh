# Installing google chrome via APT (sadly no SNAP available from Google, like there is for Chromium)

# Setup the Google signer and repo
curl -O https://packages.cloud.google.com/apt/doc/apt-key.gpg
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo tee /etc/apt/trusted.gpg.d/google.asc >/dev/null
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' 

# Install
sudo apt-get update
sudo apt-get install google-chrome-stable