from transformers import pipeline

caption_generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_caption(prompt):
    result = caption_generator(
        f"Make a short, funny meme caption for: {prompt}",
        max_new_tokens=50,
        do_sample=True,
        temperature=0.9,
        top_k=50,
        top_p=0.95
    )
    return result[0]['generated_text'].strip()
