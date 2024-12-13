import discord
from discord.ext import commands

# Replace with your bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Intents allow the bot to access more events and data
default_intents = discord.Intents.default()
default_intents.guilds = True
default_intents.guild_messages = True
default_intents.members = True  # Required to manage roles

# Set up the bot
bot = commands.Bot(command_prefix="!", intents=default_intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def create_roles(ctx, *role_names):
    """Creates multiple roles from a list of role names."""
    try:
        if not role_names:
            await ctx.send("No role names provided!")
            return

        created_roles = []
        for role_name in role_names:
            new_role = await ctx.guild.create_role(name=role_name)
            created_roles.append(new_role.name)
            print(f"Created role: {role_name}")

        await ctx.send(f'Roles created successfully: {", ".join(created_roles)}')
    except Exception as e:
        await ctx.send(f'Error creating roles: {e}')
        print(f"Error: {e}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def delete_roles(ctx, *role_names):
    """Deletes multiple roles from a list of role names."""
    try:
        if not role_names:
            await ctx.send("No role names provided!")
            return

        deleted_roles = []
        for role_name in role_names:
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                await role.delete()
                deleted_roles.append(role_name)
                print(f"Deleted role: {role_name}")
            else:
                await ctx.send(f'Role not found: {role_name}')

        if deleted_roles:
            await ctx.send(f'Roles deleted successfully: {", ".join(deleted_roles)}')
    except Exception as e:
        await ctx.send(f'Error deleting roles: {e}')
        print(f"Error: {e}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def assign_role(ctx, role_name, *usernames):
    """Assigns a specific role to a list of usernames."""
    try:
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            await ctx.send(f'Role not found: {role_name}')
            return

        assigned_users = []
        for username in usernames:
            member = discord.utils.get(ctx.guild.members, name=username)
            if member:
                await member.add_roles(role)
                assigned_users.append(username)
                print(f"Assigned role {role_name} to {username}")
            else:
                await ctx.send(f'User not found: {username}')

        if assigned_users:
            await ctx.send(f'Role {role_name} assigned to: {", ".join(assigned_users)}')
    except Exception as e:
        await ctx.send(f'Error assigning role: {e}')
        print(f"Error: {e}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx, role_name, *usernames):
    """Removes a specific role from a list of usernames."""
    try:
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            await ctx.send(f'Role not found: {role_name}')
            return

        removed_users = []
        for username in usernames:
            member = discord.utils.get(ctx.guild.members, name=username)
            if member:
                await member.remove_roles(role)
                removed_users.append(username)
                print(f"Removed role {role_name} from {username}")
            else:
                await ctx.send(f'User not found: {username}')

        if removed_users:
            await ctx.send(f'Role {role_name} removed from: {", ".join(removed_users)}')
    except Exception as e:
        await ctx.send(f'Error removing role: {e}')
        print(f"Error: {e}")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_category_with_channels(ctx, category_name, *args):
    """Creates a category with specific channels accessible only to specific roles."""
    try:
        roles = []
        text_channels = []
        audio_channels = []

        # Parse arguments for roles (-r), text channels (-ch), and audio channels (-a)
        args_list = list(args)
        while args_list:
            arg = args_list.pop(0)
            if arg == "-r":
                while args_list and not args_list[0].startswith("-"):
                    roles.append(args_list.pop(0))
            elif arg == "-ch":
                while args_list and not args_list[0].startswith("-"):
                    text_channels.append(args_list.pop(0))
            elif arg == "-a":
                while args_list and not args_list[0].startswith("-"):
                    audio_channels.append(args_list.pop(0))

        if not roles or (not text_channels and not audio_channels):
            await ctx.send("Please specify roles (-r), and at least one type of channel (-ch or -a). Example: !create_category_with_channels category_name -r Role1 Role2 -ch TextChannel1 -a VoiceChannel1")
            return

        # Create overwrites for the specified roles
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False)
        }
        for role_name in roles:
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
            else:
                await ctx.send(f'Role not found: {role_name}')
                return

        # Create the category
        category = await ctx.guild.create_category(category_name, overwrites=overwrites)
        print(f"Created category: {category_name}")

        # Create text channels within the category
        created_text_channels = []
        for channel_name in text_channels:
            channel = await category.create_text_channel(channel_name)
            created_text_channels.append(channel.name)
            print(f"Created text channel: {channel_name} in category {category_name}")

        # Create audio channels within the category
        created_audio_channels = []
        for channel_name in audio_channels:
            channel = await category.create_voice_channel(channel_name)
            created_audio_channels.append(channel.name)
            print(f"Created audio channel: {channel_name} in category {category_name}")

        await ctx.send(f'Category "{category_name}" with text channels "{", ".join(created_text_channels)}" and audio channels "{", ".join(created_audio_channels)}" created for roles "{", ".join(roles)}".')
    except Exception as e:
        await ctx.send(f'Error creating category or channels: {e}')
        print(f"Error: {e}")

# Run the bot
bot.run(BOT_TOKEN)
