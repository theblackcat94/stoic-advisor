# Import the required libraries
import openai
import streamlit as st
import random

# Set the GPT-3 API key
openai.api_key = "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"


#generate policy violation argument
def advicegenerator(random_philosopher, problem, feeling):
    prompts = [
        "Please consider all the best advice given by " + random_philosopher + ".",
        "Now please ponder how " + random_philosopher + " would solve: '" + problem + "' and what advice would be given based on my feelings: '" + feeling + "'.",
        #As many as you want....
    ]
    responses = []
    for prompt in prompts:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        responses.append(response["choices"][0]["text"].strip())
    return "\n\n".join(responses)

def randomphilosophers(philosophers_list, problem):
    prompt = "From this list " + philosophers_list + " please pick the best philosopher to solve this problem: " + problem + "."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choices"][0]["text"].strip()
    
def philosopherslist():
    prompt = "Please give me a list of the top 10 most profound philosophers of all time? "
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choices"][0]["text"].strip()


def main():
    # Prompt user for input
    st.title("Stoic Advisor")
    st.success("Built by Zach Featherstone on 08/02/2023. Not intented to solve all problems, but I hope it helps with some.")
    feeling = st.text_input("How are you feeling today? ")
    problem = st.text_input("What problem are you facing? ")

    # Get list of philosophers
    philosophers_list = philosopherslist()
    #st.write(philosophers_list)

    # Choose a random philosopher
    random_philosopher = randomphilosophers(philosophers_list, problem)
    #st.write(random_philosopher)
    # Generate a response
    advice = advicegenerator(random_philosopher, problem, feeling)
    
    generate_advice = st.button("Generate Advice")
    st.warning("Remember, this is just a computer. If the advice is wack, just press this button again.")

    if generate_advice:
        st.subheader("Advice")
        st.write("Chosen philisopher: ", random_philosopher)
        st.write(advice)
        st.balloons()

if __name__ == "__main__":
    main()
