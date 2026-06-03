SYSTEM_PROMPT = """
You are given a text which contains various menu items extracted from menu pdf file.
Your have two main tasks:
 1.Map each of the menu item in the text to the following Pydantic model:
    
    class MenuItem(BaseModel):

    id: int = Field(
        description="Unique identifier of the menu item.",
    )
    category: str = Field(
        description="Category of the menu item.",
    )
    name: str = Field(
        description="Menu item name",
    )
    price: float = Field(
        description="Menu item price",
        default=0
    )
    description: str = Field(
        description="Menu item description",
    )
    
 2. Construct Menu Pydantic model with all of the menu items you mapped previously:
    class Menu(BaseModel):
    items: list[MenuItem] = Field(
        description="Menu items",
        default_factory=list,
    )
"""
