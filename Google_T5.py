from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class T5Model:
    def __init__(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained('GilbertKrantz/Text-Summarizer_T5-Finetune')
        self.tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")

    def encode_text(self, text):
        return self.tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)
    
    def decode_text(self, text, skip_special_tokens=True):
        return self.tokenizer.decode(text, skip_special_tokens=skip_special_tokens)
    
    def summarize(self, text, max_length=150):
        # Append text with the summarization prefix (summarize:) and encode it
        text = "summarize: " + text
        input_ids = self.encode_text(text)
        summary_ids = self.model.generate(input_ids)
        summary = self.decode_text(summary_ids[0])
        return summary
    
class textHandler:
    def __init__(self, max_length=512):
        self.text = str()
        self.max_length = max_length
        
    def summarize(self, text):
        self.text = text
        summarizer = T5Model()
        return summarizer.summarize(self.text, max_length=self.max_length)
    
    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text
        
def main() :
    text = input("Enter the text you want to summarize: ")
    max_length = text.count(' ') + 1
    text_handler = textHandler(max_length=max_length)
    print(text_handler.summarize(text))
    
if __name__ == "__main__":
    main()
        