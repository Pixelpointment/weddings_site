# weddings/context_processors.py

def color_scheme(request):
    """Add the current color scheme to the context."""
    # Assuming you have a way to determine the current color scheme
    color_scheme = {
        'primary_color': '#ff5733',  # Example color
        'secondary_color': '#33c1ff',
        'accent_color': '#ff33a1',
        'font_color': '#000000',
        'btn_hover_color': '#ffcc00',
    }
    return {'color_scheme': color_scheme}
