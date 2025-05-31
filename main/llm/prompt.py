class PromptBuilder:
    @staticmethod
    def build_prompt(context, question):
        return f"""You are a knowledgeable assistant. Use the provided context to answer the user's question accurately and thoroughly.

        Instructions:
        - If the question involves a comparison (e.g., between two plans), list differences clearly in a tabular or bullet-point format.
        - Focus on key aspects such as benefits, coverage, eligibility (e.g., HSA), costs, or employer contributions if mentioned.
        - Format the answer using bullet points if multiple key points are involved.
        - If an explanation is requested, provide a clear and concise explanation.
        - If the content to be summarized is lengthy, group and condense it into a few meaningful bullet points using logical grouping or abstraction.

Context:
{context}

Question:
{question}

If the answer is not found in the context, respond with: "I don't know."
"""
