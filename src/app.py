import streamlit as st
import canvas
import utils
import model
import torch
import numpy

st.markdown(
    """
    <style>
    .reportview-container {
        background-color:#f6fbf6
    }
    .correct{
        color:green
    }
    .incorrect{
        color:red
    }
    </style>
    """,
    unsafe_allow_html=True
)

a, b, s = utils.a, utils.b, utils.s

cols = st.beta_columns((1,2,1))

with cols[1]:
    st.title("Play with MNIST")
    st.write("   ")
    st.write("   ")

    st.header("What is %d + %d?"%(a,b))
    st.text("**Answer by drawing**")
    st.write("   ")
    st.write("   ")
    st.write("   ")

    canvas = canvas.create_canvas()

    check_btn = st.button("Check")

    if check_btn:
        next_btn = st.button("Next")

        model = model.load_model()
        img_arr_tensor = utils.create_tensor(canvas.image_data)
        pred = model(img_arr_tensor)
        pred_value = torch.argmax(pred)

        if pred_value == s:
            st.markdown('<p class="correct">Correct ✅</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="incorrect">Incorrect ❌</p>', unsafe_allow_html=True)
        
        utils.create_new()


with cols[2]:
    for i in range(15):
        st.write("   ")

    st.write("**Model Status**")

    if not check_btn:
        st.write("No image is passed")
    else:
        st.write("Image passed to the network   ")
        st.image(img_arr_tensor[0][0].numpy().reshape(28,28,-1), clamp=True)
        st.write(f"Predicted value:**{pred_value}**")




