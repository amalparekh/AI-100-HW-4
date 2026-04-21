from openai import OpenAI

client = OpenAI()

prompts = [
    "Explain reinforcement learning in 3 simple sentences.",
    "Write a haiku about neural networks.",
    "Give 3 pros and 3 cons of using LLM APIs in production.",
    "Explain overfitting like I’m a beginner."
]

def run_experiment():
    with open("sample_outputs.txt", "w", encoding="utf-8") as f:
        for i, prompt in enumerate(prompts, start=1):
            response = client.responses.create(
                model="gpt-5.4",
                input=prompt
            )

            output_text = response.output_text

            block = (
                f"--- Prompt {i} ---\n"
                f"INPUT:\n{prompt}\n\n"
                f"OUTPUT:\n{output_text}\n\n"
            )

            print(block)
            f.write(block)

if __name__ == "__main__":
    run_experiment()
