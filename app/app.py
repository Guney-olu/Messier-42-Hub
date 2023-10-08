import streamlit as st

# Function to display Project Information
def display_project_information():
    st.title("Project XYZ")
    st.write("This is a project description.")
    st.write("Author: John Doe")

# Function to display Repository Details
def display_repository_details():
    st.header("Repository Details")
    st.write("Repository Name: ProjectXYZ")
    st.write("Repository URL: [Link to Repository](https://github.com/your_username/projectxyz)")
    st.write("README: [Link to README](https://github.com/your_username/projectxyz/blob/main/README.md)")

# Function to display Project Files
def display_project_files():
    st.header("Project Files")
    files = ["file1.py", "file2.py", "data.csv", "README.md"]
    selected_file = st.selectbox("Select a file to view:", files)
    if selected_file:
        st.write(f"Displaying contents of {selected_file}.")

# Function to display Related Items
def display_related_items():
    st.header("Related Items")
    st.write("Related Projects:")
    st.write("- [Related Project 1](link_to_related_project_1)")
    st.write("- [Related Project 2](link_to_related_project_2)")

    st.write("Contributors:")
    st.write("- Contributor 1")
    st.write("- Contributor 2")

    st.write("Issues:")
    st.write("- Issue 1")
    st.write("- Issue 2")

# Function to display Comments Section
def display_comments_section():
    st.header("Comments")
    comment = st.text_area("Add your comment", "")
    if st.button("Submit Comment"):
        pass  # You can add logic to process and store the comment here

# Function to display Profile Information
# Function to display Profile Information
def display_profile():
    st.title("Keshwam Pandey")
    
    # Profile Image
    st.image("https://avatars.githubusercontent.com/u/129495697?v=4", caption="Keshwam Pandey", use_column_width=True)

    # Bio
    st.header("Bio")
    st.write("Lets just pretend this is a very attractive bio ")

    # Skills
    st.header("Skills")
    st.write("- Web Development")
    st.write("- Python")
    st.write("- Data Science")
    st.write("- UI/UX Design")

    # Contact Information
    st.header("Contact")
    st.write("Email: john.doe@example.com")
    st.write("Phone: +123-456-7890")

    # Social Media Links
    st.header("Connect with me")
    st.write("[LinkedIn](https://www.linkedin.com/in/itskeshwam)")
    st.write("[GitHub](https://github.com/itskeshwam)")
    st.write("[Twitter](https://twitter.com/)")

    # Additional Information
    st.header("Additional Info")
    st.write("Location: New York, USA")
    st.write("Languages: English, Spanish")

    # Add more profile information as needed


# Main function to handle page navigation
def main():
    st.sidebar.title("Navigate")
    pages = ["Profile", "Project Information", "Repository Details", "Project Files", "Related Items", "Comments"]
    selected_page = st.sidebar.selectbox("Go to", pages)

    if selected_page == "Profile":
        display_profile()
    elif selected_page == "Project Information":
        display_project_information()
    elif selected_page == "Repository Details":
        display_repository_details()
    elif selected_page == "Project Files":
        display_project_files()
    elif selected_page == "Related Items":
        display_related_items()
    elif selected_page == "Comments":
        display_comments_section()

if __name__ == "__main__":
    main()
