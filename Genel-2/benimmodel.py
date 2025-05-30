<<<<<<< HEAD
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# Hugging Face giriş işlemi
login(token="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")

print("Başarıyla giriş yapıldı!")

# Tokenizer ve modelin yüklenmesi
tokenizer = AutoTokenizer.from_pretrained("emredeveloper/DeepSeek-R1-Medical-COT")
model = AutoModelForCausalLM.from_pretrained("emredeveloper/DeepSeek-R1-Medical-COT")

# Modeli kullanarak bir metin oluşturma
def generate_response(input_text):
    # Input metnini token'lara dönüştürme
    inputs = tokenizer(input_text, return_tensors="pt")
    
    # Modelden çıkışı almak için generate metodunu kullanma
    outputs = model.generate(**inputs)
    
    # Çıktıyı decode ederek cevap verme
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Kullanıcıdan input almak
input_text = "baş ağrısı nedir?"

# Modeli çalıştırma ve sonucu yazdırma
response = generate_response(input_text)
print(f"Model Cevabı: {response}")
=======
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# Hugging Face giriş işlemi
login(token="")

print("Başarıyla giriş yapıldı!")

# Tokenizer ve modelin yüklenmesi
tokenizer = AutoTokenizer.from_pretrained("emredeveloper/DeepSeek-R1-Medical-COT")
model = AutoModelForCausalLM.from_pretrained("emredeveloper/DeepSeek-R1-Medical-COT")

# Modeli kullanarak bir metin oluşturma
def generate_response(input_text):
    # Input metnini token'lara dönüştürme
    inputs = tokenizer(input_text, return_tensors="pt")
    
    # Modelden çıkışı almak için generate metodunu kullanma
    outputs = model.generate(**inputs)
    
    # Çıktıyı decode ederek cevap verme
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Kullanıcıdan input almak
input_text = "baş ağrısı nedir?"

# Modeli çalıştırma ve sonucu yazdırma
response = generate_response(input_text)
print(f"Model Cevabı: {response}")
>>>>>>> 6e953b09772621b8cc37bb192b05fdf7daad2d9a
