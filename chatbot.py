import oci

# Load config (Cloud Shell auto-configured)
config = oci.config.from_file()

# Replace with your region
region = "uk-london-1"

# Replace with your compartment OCID (you can try tenancy OCID if needed)
compartment_id = "<your-compartment-ocid>"

# Create client
client = oci.generative_ai_inference.GenerativeAiInferenceClient(
    config=config,
    service_endpoint=f"https://inference.generativeai.{region}.oci.oraclecloud.com"
)

def chat(prompt):
    try:
        response = client.generate_text(
            generate_text_details=oci.generative_ai_inference.models.GenerateTextDetails(
                compartment_id=compartment_id,
                prompt=prompt,
                max_tokens=100,
                temperature=0.5
            )
        )

        return response.data.generated_texts[0].text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("🤖 OCI Chatbot (type 'exit' to quit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        reply = chat(user_input)
        print("Bot:", reply)