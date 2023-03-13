from library.models.base import Link


def include_links(text: str, args: list[Link]):
    return text.format(
        *map(lambda link: f'<a href="{link.ref}">{link.name}</a>', args))
