from streamlit_drawable_canvas import st_canvas

def create_canvas():
    canvas = st_canvas(
            fill_color="rgb(255, 255, 255)",
            stroke_width=5,
            stroke_color="rgb(0,0,0)",
            update_streamlit=True,
            height=250,
            width=250, 
            drawing_mode="freedraw",
            key="canvas",
        )
    return canvas