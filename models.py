from pydantic import BaseModel, Field


class MenuItem(BaseModel):
    """
    Pydantic model representing a menu item.
    """

    id: int = Field(
        description="Unique identifier of the menu item.",
    )
    category: str = Field(
        description="Category of the menu item.",
    )
    name: str = Field(
        description="Menu item name",
    )
    price: float = Field(description="Menu item price", default=0)
    description: str = Field(
        description="Menu item description",
        default_factory=str,
    )


class Menu(BaseModel):
    """
    Pydantic model representing a menu.
    """

    items: list[MenuItem] = Field(
        description="Menu items",
        default_factory=list,
    )
