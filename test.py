import generate from generator

print(
    generator.generate(num_samples=5, max_new_tokens=50, start="To be")
)