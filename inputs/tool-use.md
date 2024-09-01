
# Introducing Llama-3-Groq-Tool-Use Models - Groq is Fast AI Inference

> ## Excerpt
> While the Llama-3 Groq Tool Use models excel at function calling and tool use tasks, we recommend implementing a hybrid approach that combines these specialized models with general-purpose language models. This strategy allows you to leverage the strengths of both model types and optimize performance across a wide range of tasks.

---
##### **Specialized Models & Routing**

While the Llama-3 Groq Tool Use models excel at function calling and tool use tasks, we recommend implementing a hybrid approach that combines these specialized models with general-purpose language models. This strategy allows you to leverage the strengths of both model types and optimize performance across a wide range of tasks.

###### **Recommended approach:**

1.  **Query Analysis**: Implement a routing system that analyzes incoming user queries to determine their nature and requirements.
2.  **Model Selection**: Based on the query analysis, route the request to the most appropriate model:
    -   For queries involving function calling, API interactions, or structured data manipulation, use the Llama 3 Groq Tool Use models.
    -   For general knowledge, open-ended conversations, or tasks not specifically related to tool use, route to a general-purpose language model like unmodified the Llama-3 70B.

By implementing this routing strategy, you can ensure that each query is handled by the most suitable model, maximizing the overall performance and capabilities of your AI system. This approach allows you to harness the specialized tool use abilities of the Llama-3 Groq models while maintaining the flexibility and broad knowledge base of general-purpose models.

##### **Conclusion**

The Llama-3 Groq Tool Use models represent a significant step forward in open-source AI for tool use. With state-of-the-art performance and a permissive license, we believe these models will enable developers and researchers to push the boundaries of AI applications in various domains.

We invite the community to explore, utilize, and build upon these models. Your feedback and contributions are crucial as we continue to advance the field of AI together.

We’re looking forward to seeing more innovation and experimentation with open-source models and see even higher scores on BFCL to reach full saturation on the benchmark and have solved the first inning of tool use for LLMs.  

##### Start Building

Both Llama-3-Groq-70B-Tool-Use and Llama-3-Groq-8B-Tool-Use are available for preview access through the Groq API with the following model IDs:

-   ```
    llama3-groq-70b-8192-tool-use-preview
    ```
    
-   ```
    llama3-groq-8b-8192-tool-use-preview
    ```
    

Get started in the [GroqCloud Dev Hub](http://console.groq.com/) today!
