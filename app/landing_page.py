import streamlit as st





def home():

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['user'] = 'none'
    st.image('./media/athena.jpeg')
    st.markdown('# Athen.ai')

    st.markdown("""


Are you a pioneer in open science, seeking the perfect collaborator for your project? Or perhaps you're a skilled individual with a passion for scientific exploration, eager to contribute your expertise? Athen.ai is here to empower both project creators and contributors in the realm of open science.

## For Project Creators:
Athen.ai provides a platform for project creators to share their vision and seek the ideal collaborators. Here's how it works:

1. **Project Description**: Craft a detailed project description outlining the essence of your scientific endeavor. Explain your project's goals, objectives, and the impact you intend to make.

2. **Collaborator Profile**: Specify the type of collaborators you're looking for and the level of expertise required. Whether you need a data scientist, a biologist, or a statistician, we've got you covered.

3. **Scope of Work**: Define the scope of work for your project. Detail the tasks, responsibilities, and timelines to give potential collaborators a clear understanding of what's expected.

## For Contributors:
Are you a scientist, researcher, or expert in your field, eager to engage in meaningful open science projects? Athen.ai makes it easy:

1. **Skill Showcase**: Showcase your skills and expertise by listing your areas of specialization. Let the world know what you bring to the table, whether it's data analysis, experimental design, or coding skills.

2. **Project Preferences**: Specify the types of open science projects that align with your interests. Whether it's environmental research, medical studies, or astronomy, we help you find projects that resonate with your passion.

3. **Availability**: Indicate when you're available to contribute to projects. Whether it's evenings, weekends, or a specific timeframe, we help match your availability with project creators' needs.

## Connecting Collaborators:
Athen.ai's intelligent platform enables seamless collaboration:

- **Search and Match**: Project creators can easily search for collaborators based on specific skills and expertise. Contributors can discover projects that align with their interests and skills.

- **Communication Hub**: Our built-in chat feature facilitates direct communication between creators and contributors, making it simple to exchange ideas and plan collaborative efforts.

- **Collaboration in Action**: Watch as your projects come to life with the perfect team in place, sharing the same enthusiasm for open science.

Athen.ai is your gateway to a world of scientific collaboration. Join our community today, find your next scientific adventure, and embark on a journey of discovery and innovation. Experience the power of open science collaboration with Athen.ai!""")

def signup_page():

    st.markdown("# Signup")

def signin_page():

    st.markdown("# Signin")

def signup_callback():
    st.session_state['current_page'] = "signup"
    
def signin_callback():
    st.session_state['current_page'] = "signin"
def home_callback():
    st.session_state['current_page'] = 'home'



if __name__ == "__main__":
    
        pages = {"home":home,"signup":signup_page,"signin":signin_page}
        
        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = "home"
        
        pages[st.session_state['current_page']]()
    
    
    