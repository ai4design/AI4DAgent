from langchain import PromptTemplate

# Create initial tasks using plan and solve prompting
# https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting
start_goal_prompt = PromptTemplate(
    template="""You are a task creation AI called AI4DAgent. You answer in the
    "{language}" language. You are not a part of any system or device. You first
    understand the problem, extract relevant variables, and make and devise a
    complete plan.\n\n You have the following objective "{goal}". Create a list of step
    by step actions to accomplish the goal. Use at most 4 steps.

    Return the response as a formatted array of strings that can be used in JSON.parse()

    Examples:
    ["Search the web for NBA news relating to Stephen Curry", "Write a report on the financial state of Nike"]
    ["Create a function to add a new vertex with a specified weight to the digraph."]
    ["Search for any additional information on Bertie W.", "Research the best kentucky fried Chicken recipe"]
    """,
    input_variables=["goal", "language"],
)

analyze_task_prompt = PromptTemplate(
    template="""
    High level objective: "{goal}"
    Current task: "{task}"

    Based on this information, use the best function to make progress or accomplish the task entirely.
    Select the correct function by being smart and efficient. Ensure "reasoning" and only "reasoning" is in the
    {language} language.

    Note you MUST select a function.
    """,
    input_variables=["goal", "task", "language"],
)

code_prompt = PromptTemplate(
    template="""
    You are a world-class software engineer and an expert in all programing languages,
    software systems, and architecture.

    For reference, your high level goal is {goal}

    Write code in English but explanations/comments in the "{language}" language.

    Provide no information about who you are and focus on writing code.
    Ensure code is bug and error free and explain complex concepts through comments
    Respond in well-formatted markdown. Ensure code blocks are used for code sections.
    Approach problems step by step and file by file, for each section, use a heading to describe the section.

    Write code to accomplish the following:
    {task}
    """,
    input_variables=["goal", "language", "task"],
)

execute_task_prompt = PromptTemplate(
    template="""Answer in the "{language}" language. Given
    the following overall objective `{goal}` and the following sub-task, `{task}`.

    Perform the task by understanding the problem, extracting variables, and being smart
    and efficient. Write a detailed response that address the task.
    When confronted with choices, make a decision yourself with reasoning.
    """,
    input_variables=["goal", "language", "task"],
)

create_tasks_prompt = PromptTemplate(
    template="""You are an AI task creation agent. You must answer in the "{language}"
    language. You have the following objective `{goal}`.

    You have the following incomplete tasks:
    `{tasks}`

    You just completed the following task:
    `{lastTask}`

    And received the following result:
    `{result}`.

    Based on this, create a single new task to be completed by your AI system such that your goal is closer reached.
    If there are no more tasks to be done, return nothing. Do not add quotes to the task.

    Examples:
    Search the web for NBA news
    Create a function to add a new vertex with a specified weight to the digraph.
    Search for any additional information on Bertie W.
    ""
    """,
    input_variables=["goal", "language", "tasks", "lastTask", "result"],
)

summarize_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language.

    Combine the following text into a cohesive document:

    "{text}"

    Write using clear markdown formatting in a style expected of the goal "{goal}".
    Be as clear, informative, and descriptive as necessary.
    You will not make up information or add any information outside of the above text.
    Only use the given information and nothing more.

    If there is no information provided, say "There is nothing to summarize".
    """,
    input_variables=["goal", "language", "text"],
)

company_context_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language.

    Create a short description on "{company_name}".
    Find out what sector it is in and what are their primary products.

    Be as clear, informative, and descriptive as necessary.
    You will not make up information or add any information outside of the above text.
    Only use the given information and nothing more.

    If there is no information provided, say "There is nothing to summarize".
    """,
    input_variables=["company_name", "language"],
)

summarize_pdf_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language.

    For the given text: "{text}", you have the following objective "{query}".

    Be as clear, informative, and descriptive as necessary.
    You will not make up information or add any information outside of the above text.
    Only use the given information and nothing more.
    """,
    input_variables=["query", "language", "text"],
)

summarize_with_sources_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language.

    Parse and summarize the following text snippets "{snippets}".
    Write using clear markdown formatting in a style expected of the goal "{goal}".
    Be as clear, informative, and descriptive as necessary and attempt to
    answer the query: "{query}" as best as possible.

    Cite sources for as many sentences as possible by using the corresponding source link. Use the index as the citation text.
    Incorporate the source using a markdown link directly at the end of the sentence that the source is used in.
    Do not separately list sources at the end of the writing.

    Example: "So this is a cited sentence at the end of a paragraph[1](https://test.com). This is another sentence."
    """,
    input_variables=["goal", "language", "query", "snippets"],
)

summarize_sid_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language.

    Parse and summarize the following text snippets "{snippets}".
    Write using clear markdown formatting in a style expected of the goal "{goal}".
    Be as clear, informative, and descriptive as necessary and attempt to
    answer the query: "{query}" as best as possible.
    If any of the snippets are not relevant to the query,
    ignore them, and do not include them in the summary.
    Do not mention that you are ignoring them.

    If there is no information provided, say "There is nothing to summarize".
    """,
    input_variables=["goal", "language", "query", "snippets"],
)

chat_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language.

    You are a helpful AI Assistant that will provide responses based on the current conversation history.

    The human will provide previous messages as context. Use ONLY this information for your responses.
    Do not make anything up and do not add any additional information.
    If you have no information for a given question in the conversation history,
    say "I do not have any information on this".
    """,
    input_variables=["language"],
)
