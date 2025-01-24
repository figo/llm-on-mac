It is surprise me that the latest DeepSeek reasoning model can be launched locally with Mac Mini, I learned vividly that llama 3.1 model is so horrible at solving math problems.  

Let's look at this simple math problem:  
`if 2a + 4b = 120, What is a and b (multiple possible values)?`  

The llama 3.1 model would run into infinite loop or simply give up.
But here is the DeepSeek R1 model's answer, pretty good:  
```
if 2a + 4b = 120, What is a and b (multiple possible values)?<think>
First, I need to solve the equation \(2a + 4b = 120\) for variables \(a\) and \(b\).

To simplify the equation, I can divide the entire equation by 2, which gives me \(a + 2b = 60\).

Next, I'll solve for \(a\) in terms of \(b\): \(a = 60 - 2b\).

Since there are infinite possible values for \(b\), there are also infinite solutions for \(a\) based on the value of \(b\).

Therefore, the general solution is \(a = 60 - 2b\), where \(b\) can be any real number.
</think>

To find the possible values of \( a \) and \( b \) that satisfy the equation \( 2a + 4b = 120 \), follow these steps:

1. **Simplify the Equation:**

   Start by simplifying the equation to make it easier to solve.

   \[
   2a + 4b = 120
   \]

   Divide both sides of the equation by 2:

   \[
   a + 2b = 60
   \]

2. **Express \( a \) in Terms of \( b \):**

   Solve for \( a \) to express it in terms of \( b \):

   \[
   a = 60 - 2b
   \]

3. **Determine Possible Values:**

   Since \( b \) can be any real number, there are infinitely many solutions for \( a \) and \( b \). Here are a few examples:

   - **Example 1:** If \( b = 0 \),

     \[
     a = 60 - 2(0) = 60
     \]

     So, \( a = 60 \) and \( b = 0 \).

   - **Example 2:** If \( b = 10 \),

     \[
     a = 60 - 2(10) = 40
     \]

     So, \( a = 40 \) and \( b = 10 \).

   - **Example 3:** If \( b = 25 \),

     \[
     a = 60 - 2(25) = 10
     \]

     So, \( a = 10 \) and \( b = 25 \).

4. **General Solution:**

   The general solution for the equation \( a + 2b = 60 \) can be expressed as:

   \[
   a = 60 - 2b
   \]

   where \( b \) can be any real number.

**Final Answer:**

There are infinitely many solutions, but one possible solution is \( \boxed{a = 60 - 2b} \) where \( b \) is any real number. [end of text]
```


### How to inference the DeepSeek R1 with llama.cpp

```
llama-cli \
    --model "../reasoning-models/DeepSeek-R1-Distill-Qwen-32B-Q2_K.gguf" \  (replace with your local path)
    --cache-type-k q8_0 \
    --threads 10 \
    -no-cnv \
    --n-gpu-layers 5 \
    --prompt '<｜User｜>if 2a + 4b = 120, What is a and b (multiple possible values)?<｜Assistant｜>' \
```

### Observations

- The DeepSeek R1 model requires a large amount of memory even with llama.cpp,   
so I have to leverage the Mac Mini's GPU by specifying `--n-gpu-layers`
- The Mac mini's cpu, gpu, memory are barely sufficient, it took 3 hours to answer a simple question, but it is exciting.

### Reference
- [DeepSeek R1 at HF](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF)