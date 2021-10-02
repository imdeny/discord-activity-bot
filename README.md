# Discord Voice Activities Bot


A simple bot for launching Discord's activities in voice channels.

Once the bot is added, you can launch an activity with `/activity` or `>activity`.

This bot makes use of [discord-together](https://github.com/apurv-r/discord-together) by apurv-r.

## Commands

Slash command support with `/activity`

![slash command](https://user-images.githubusercontent.com/20955511/133788815-2f67757f-5092-49df-a085-a657a98830b5.png)

Legacy-style commands

* `>activity` - Select from a list of activities
* `>youtube` - Launch YouTube Together
* `>poker` - Launch Poker Night
* `>chess` - Launch Chess in the Park
* `>betrayal` - Launch Betrayal.io
* `>fishing` - Launch Fishington.io
* `>letter-tile` - Launch Letter Tile
* `>word-snack` - Launch Word Snack
* `>doodle-crew` - Launch Doodle Crew
* `>help` - Shows help for legacy-style commands

## Environment Variables

The following environment variables can be specified in a `.env` file to configure the bot for self-hosting:

* `DISCORD_TOKEN`: The token for the bot.
* `GUILD_IDS` (optional): A comma-separated list of guild IDs to activate slash commands in. (This is for testing since global slash commands can take an hour to register.)
