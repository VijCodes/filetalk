---------

Stage1

Initial Idea is to use Vector DB and Knowledge graph combination to store and retrieve file structure

We can use readme files in each folder as input to vector DB

Vector search will be used to get relevant info for query


----------

Stage 2

Knowledge graph is not needed as file structure is tree. We don't need too much knowledge as well

A simple tree with each leave pointing to parents is good enough

Current approach is to finding right file with vectorDB and then getting fetch all parentses Readme as well

This gives info to answer any query with details and path name

We want CLI installation like "brew install filetalk"

This tool is very helpful in CLI cause to move folders is hard in CLI, you need to remember exact path 

----------

Stage 3

For now we are just searching all space using cosine similarity on transformer embeddings - This lets us get baseline simple mode

We can now use LLM along with content in matched folder along with parents folder info to get relevant info 

using oobabooga we can increase the context length to 10k tokens - https://www.reddit.com/r/LocalLLaMA/comments/175hht2/best_open_source_ai_model_for_qa_generation_from/

More info needed on how mixtral compares models - perplexity, Sliding Window Attention, GQA(grouped query attention), Byte-fallback BPE tokenizer

-------



