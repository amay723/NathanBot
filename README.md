# NathanBot
A Discord bot that tracks a user's activity in voice channels.

## Libraries Used
- [discord.py](https://discordpy.readthedocs.io/)


# Setup
1. Make a copt of `.env.default` called `.env` and update the following values:
    * `TOKEN`: The Discord Bot access token
    * `USER_ID`: The ID of the user to track
    * `CHANNEL_ID`: The channel ID to send the "joined"/"left" messages to
2. Install project dependencies
```sh
# Setup the virtual environment
python3 -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux

# Install the project dependencies
pip install -r requirements.txt
```
3. Run the Bot
```sh
python3 bot.py
```

# Deployment (Linux)
Use `NathanBot.service` to create a service that will allow the program to automatically run on system startup.

## Setup
*Note*: You should first update `NathanBot.service` to ensure all file paths match your deployment.
```sh
cp NathanBot.service /lib/systemd/system/

# Starts the service
systemctl start NathanBot.service
# Marks the service to be started on system boot
systenctl enable NathanBot.service
```

## Update Project
If your project files were updated, you will need to restart the service for the changes to fully take effect.
```sh
systemctl restart NathanBot.service
```