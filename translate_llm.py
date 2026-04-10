from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("[translate_llm] Loading NLLB-200 translation model...")

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("[translate_llm] Model loaded.")


def translate(text, target_lang):
    tokenizer.src_lang = "eng_Latn"

    inputs = tokenizer(text, return_tensors="pt")

    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=forced_bos_token_id,
        max_length=200
    )

    translated_text = tokenizer.batch_decode(
        translated_tokens,
        skip_special_tokens=True
    )[0]

    return translated_text