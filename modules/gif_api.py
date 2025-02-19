"""
GIF backend functions.
"""

from random import choice
from aiohttp import ClientSession
from discord import Embed

from modules.vault import get_api_key


async def get_gif_url(method: str) -> str("url"):
    """
    Get a GIF url using search query
    """

    async with ClientSession() as session:
        async with session.get(
            f"https://g.tenor.com/v1/random?q=Anime {method} GIF&key={get_api_key('tenor')}&limit=9"
        ) as response:
            data = await response.json()
            return choice(data["results"])["media"][0]["gif"]["url"]


async def construct_gif_embed(author: str, target: str, method: str, lang: dict) -> Embed:
    """
    Construct a GIF embed
    """

    title = lang[method]["title"]

    if method == "slap":
        desc = f"{target} {lang[method]['mid_text']} {author}"
    else:
        desc = f"{author} {lang[method]['mid_text']} {target}"
    if method in ["hug", "kick", "poke", "bite", "cuddle"]:
        desc = desc + lang[method]["mid_text_2"]

    embed = Embed(title=title, description=desc)
    embed.set_image(url=await get_gif_url(method))
    return embed
