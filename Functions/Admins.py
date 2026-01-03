from rich.console import *
from rich.panel import *
from rich import *
from rich.color import *
console = Console()
console.print(
    Panel(
        "Ласкаво просимо до CryptoTrade!",
        title="WELCOME",
        style="cyan",
        border_style="bright_blue"
    )
)