**8-Week Practical Course: Application Programming with GEN-AI and Python**

---

## **Week 1: Python Foundations & Environment Setup**

### **Day 1: Course Introduction & Environment Setup**
- Course overview, objectives, goals.
- Python installation & PATH setup.
- Virtual Environments: `venv`/`uv`.
- IDE Setup: VSCode basics, extensions.
- "Hello, World!".

### **Day 2: Python Basics**
- Data Types: Numbers, Strings, Booleans.
- Data Structures: Lists, Tuples, Dictionaries, Sets.
- Control Flow: `if`/`elif`/`else`, `for`/`while`.
- Debugging Intro: `print`, tracebacks, IDE debugger.

### **Day 3: Python Essentials for GEN-AI**
- Functions: `def`, arguments, return, scope.
- Error Handling: `try...except`.
- Modules & Packages: `import`, stdlib (`os`, `math`), install (`uv`).
- Code Style: PEP 8, modularity.
- **Lab:** Text manipulation utility functions.

### **Day 4: Working with Libraries & Data**
- HTTP Basics: Methods, status codes.
- `requests` Library: API calls, responses.
- `json` Library: Parsing (`loads()`) & serialization (`dumps()`).
- Intro Data Handling: `numpy` arrays, file I/O.
- **Lab:** Fetch & process API data; optional file saving.

### **Day 5: Project - Weather & News Dashboard**
- API Concepts: REST, API keys.
- App Structure: CLI design, error handling, user experience.
- **Project:** Build a CLI dashboard that fetches and displays weather forecasts, latest news headlines, and fun facts using public APIs. Include data persistence and user location preferences.

---

## **Week 2: Introduction to Generative AI & LLM Integration**

### **Day 1: What Is Generative AI?**
- Definition, history, concepts (LLMs, prompts, tokens).
- Major models/players (OpenAI, Google, Anthropic).
- Ethics: Bias, misuse, responsible AI usage.
- Demo: Text/image generation (ChatGPT, Claude).

### **Day 2: Working with OpenAI's GPT APIs**
- OpenAI Platform: Models (GPT-4/3.5), pricing.
- API Key Management & Security.
- OpenAI Python Library: Install (`uv add openai`), usage.
- Chat Completions API: `openai.chat.completions.create`, roles.
- Key Params: `model`, `messages`, `temperature`, `max_tokens`.
- **Lab:** Python script using GPT API for prompts/responses.

### **Day 3: Advanced OpenAI Features & Prompting**
- Model Capabilities/Limitations (cutoff, hallucinations).
- Prompt Engineering: Context, format, zero/few-shot.
- System prompts and role-based conversations.
- Tools/Function Calling: Basics and implementation.
- **Lab:** Experiment with prompt engineering and function calling.

### **Day 4: OpenAI Assistants API & Stateful Conversations**
- Assistants API: Stateful conversations, persistent threads.
- Creating assistants with instructions and tools.
- Thread management and message handling.
- File uploads and code interpreter.
- **Lab:** Build a stateful assistant using the Assistants API.

### **Day 5: Project - Intelligent Personal Assistant**
- Application Architecture: CLI vs GUI approaches.
- Conversation history management.
- Cost optimization strategies.
- Error handling and rate limiting.
- **Project:** Build an intelligent personal assistant with conversation memory, function calling capabilities (calendar, reminders, web search), and persistent chat history across sessions.

---

## **Week 3: Google Gemini & UI with Streamlit**

### **Day 0: Vibe coding tutorial (Cursor and Copilot)**
- Intro AI code assistants: Cursor, Copilot.
- Setup, basic usage (chat, code gen).
- AI pair programming tips.

### **Day 1: Exploring Google AI Studio & Vertex AI**
- Google AI Ecosystem: Vertex AI overview.
- Google AI Studio: Web-based Gemini prototyping.
- Gemini Models: Pro, Flash.
- Hands-on: Prompting, params, safety settings in AI Studio.
- **Lab:** Use AI Studio for text tasks (generate, summary, Q&A) with Gemini.

### **Day 2: Programming with the Google Gemini API**
- Google AI Python SDK: Install (`uv add google-generativeai`), setup.
- Authentication: API keys.
- API Calls: `GenerativeModel.generate_content`.
- Streaming Responses: Handling chunks.
- **Lab:** Python script using Gemini API for text generation (incl. streaming).

### **Day 3: Introduction to Streamlit for UI Development**
- Streamlit Basics: Rapid UI, execution model, caching.
- Core Widgets: Text (`st.write`), input (`st.text_input`, `st.button`), layout (`st.columns`, `st.sidebar`).
- Data Display: DataFrames (`st.dataframe`), basic charts.
- **Lab:** Build simple Streamlit app with various widgets/layout.

### **Day 4: Building Streamlit Chatbots with Gemini**
- Chat UI: `st.chat_input`, `st.chat_message`.
- State Management: `st.session_state` for history.
- Integration: Connect Streamlit I/O to Gemini API.
- Workflow: Input -> History -> API call -> Display -> History.
- **Lab:** Simple Streamlit chatbot using `st.session_state` & Gemini API.

### **Day 5: Project - Interactive AI Content Generator**
- Combine Gemini API with Streamlit for a polished UI.
- Multi-modal content generation (text, creative writing, analysis).
- Interactive features: real-time streaming, chat history, export options.
- **Project:** Build a comprehensive Streamlit app that generates various content types (stories, summaries, analysis) with an intuitive UI, chat history, and content export functionality.

---

## **Week 4: Introduction to Retrieval-Augmented Generation (RAG)**

### **Day 1: What is RAG? Core Concepts & Use Cases**
- Problem: LLM limitations (cutoff, hallucinations).
- RAG Concept: Retrieve info, then generate.
- Architecture: Retriever + Generator (LLM).
- Benefits: Grounding, factual consistency, domain knowledge.
- Use Cases: Chatbots, Q&A on private data, summarization.
- **Activity:** Brainstorm RAG applications.

### **Day 2: RAG Implementation with Langchain**
- Intro LangChain: Orchestration (Components, Chains).
- RAG Components: Loaders, Splitters, Embeddings, Vector Stores, Retrievers, LLMs.
- `RetrievalQA` Chain: Basic RAG Q&A.
- **Lab:** Simple LangChain RAG: Load -> Split -> Retrieve -> Generate (OpenAI/Gemini).

### **Day 3: Embeddings & Vector Databases**
- Embeddings: Semantic representation (OpenAI, Sentence Transformers).
- Vector Stores: Storing embeddings (e.g., `Chroma`).
- LangChain Integration: Using `Chroma`.
- **Lab:** Enhance RAG: Embed -> Store in ChromaDB -> Retrieve via similarity.

### **Day 4: Improving RAG Performance**
- RAG Challenges: Retrieval/generation quality.
- Text Splitting Strategies: Impact of chunking.
- Retrieval Techniques: MMR, metadata filtering, compression.
- **Lab:** Experiment with splitting/retrieval methods in LangChain RAG.

### **Day 5: Project - Document Intelligence Assistant**
- Combine Weeks 3 & 4: Streamlit UI for RAG.
- Workflow: Streamlit input -> RAG Chain -> Streamlit output.
- State Handling: `st.session_state` for RAG chat history.
- **Project:** Build a document intelligence assistant that can ingest PDFs, websites, and text files, then answer questions with source citations, summary generation, and conversation history.

---

## **Week 5: Open Source Models & Fine-Tuning**

### **Day 1: Introduction to Hugging Face**
- Hugging Face Hub: Models, datasets, Spaces.
- Transformers Library: Concepts, pipeline usage.
- Loading pre-trained models/tokenizers.
- Basic tasks: Text generation, classification via `transformers`.
- **Lab:** Use `transformers` pipeline for text gen & sentiment analysis.

### **Day 2: Running Models Locally with Ollama & LM Studio**
- Ollama: Run LLMs locally via CLI.
- Installation & setup.
- Running models (Llama 3, Mistral).
- LM Studio: GUI for local LLMs.
- Comparison: Ollama vs. LM Studio.
- **Lab:** Install Ollama, run model via CLI; optional LM Studio exploration.

### **Day 3: Interacting with Ollama via Python**
- Ollama Python Library: Install (`uv add ollama`).
- Connect to running Ollama instance.
- Generate text/chat via library.
- Streaming responses.
- Integrate local models into Python apps (CLI/Streamlit).
- **Lab:** Python script using `ollama` lib to interact with local model.

### **Day 4: Fine-Tuning Theory**
- What is Fine-Tuning?: Adapting pre-trained models.
- Why Fine-Tune?: Better niche performance, domain adaptation.
- Full vs. PEFT: Concepts, pros/cons.
- Data Prep: Instruction datasets (prompt/response).

### **Day 5: Project - Custom Domain Expert Model**
- Unsloth: Faster LoRA/QLoRA fine-tuning library.
- Environment: Kaggle/Colab GPUs.
- Data Formatting: HuggingFace dataset selection.
- Fine-tuning Script: Unsloth + `transformers` SFTTrainer.
- Model evaluation and comparison with base model.
- **Project:** Fine-tune a specialized model for a chosen domain (customer service, coding assistant, creative writing) and build a comparison interface to demonstrate the improvements over the base model.

---

## **Week 6: Multimodal Models**

### **Day 1: Vision Models (Image Understanding)**
- Intro Multimodality: Combining text, images, audio.
- Vision Models: Captioning, VQA.
- APIs/Libraries: Gemini Vision, OpenAI Vision API, HF `transformers`.
- **Lab:** Use Vision API (e.g., Gemini Pro) for image description/Q&A.

### **Day 2: Multimodal Reasoning**
- Reasoning Across Modalities: Text + image tasks.
- Examples: Explain visual jokes, follow visual instructions.
- Prompting techniques.
- **Lab:** Experiment with text+image prompts for reasoning (Gemini/GPT-4V).

### **Day 3: Image Generation Models**
- Text-to-Image: Diffusion model concepts.
- Models & APIs: Stable Diffusion, DALL-E 3, Imagen.
- Prompting: Style, content, negative prompts.
- **Lab:** Generate images via API (DALL-E) or local setup (Diffusers).

### **Day 4: Audio Models**
- Speech-to-Text (STT): Transcription (OpenAI Whisper).
- Text-to-Speech (TTS): Synthesis (Google TTS, OpenAI TTS).
- APIs/Libraries for audio.
- **Lab:** Use Whisper API/lib for transcription; TTS API/lib for speech generation.

### **Day 5: Project - Multimodal AI Assistant**
- Integrating Vision, Audio, and Text capabilities.
- Streamlit app with file upload for images, audio, and documents.
- Multi-modal reasoning and cross-modal interactions.
- **Project:** Build a comprehensive multimodal assistant that can analyze images, transcribe/respond to audio, generate images from descriptions, and handle text-vision reasoning tasks in one unified interface.

---

## **Week 7: AI Agents**

### **Day 1: Introduction to AI Agents**
- What are Agents?: LLMs that reason, plan, use tools.
- Core Concepts: Reasoning loop (Observe, Think, Act), planning, memory.
- Architectures: ReAct, Plan-and-Execute.
- Frameworks Overview: LangChain Agents, OpenAI Assistants.

### **Day 2: Agents and Tools**
- Why Tools?: Extend agent capabilities (search, code, APIs).
- Defining Tools: Functions for agents.
- Tool Selection & Invocation.
- Framework Integration: Using tools.
- **Lab:** Create simple tool (calculator) & integrate with basic agent.

### **Day 3: Model Context Protocol (MCP) Introduction**
- What is MCP?: Standard protocol for model/tool interaction.
- Core Concepts: Resources, Prompts, Tools, Sampling.
- Benefits: Interoperability (models, clients, tools).
- How it works: Client <-> Server (STDIO, SSE).
- Overview: SDKs (Python/TS), integrations (Cursor).
- **Lab:** Explore MCP docs/SDKs; optionally set up simple server or connect client.

### **Day 4: OpenAI Agents SDK**
- Overview: Lightweight multi-agent framework.
- Core Concepts: Agents (instructions, tools), Handoffs, Guardrails, Tracing.
- Runner & Loop: `Runner.run()` execution.
- Defining Tools: `@function_tool` decorator.
- Compatibility: OpenAI Chat Completions format.
- **Lab:** Install SDK (`uv add openai-agents`), run examples (hello world, tool, handoffs).

### **Day 5: Project - Autonomous Research Assistant**
- Goal: Agent researches topics and creates comprehensive reports.
- Components: LLM, Agent Framework, Multiple Tools (search, scraping, analysis).
- Advanced features: Source verification, fact-checking, citation generation.
- **Project:** Build an autonomous research assistant that can research any topic, verify information across multiple sources, and generate comprehensive reports with proper citations and analysis.

---

## **Week 8: AI Agent Testing, Evaluation & Production Deployment**

### **Day 1: LLM & Agent Evaluation Fundamentals**
- Beyond Traditional Metrics: Moving past BLEU/ROUGE to holistic evaluation.
- Agent-Specific Metrics: Planning accuracy, tool use success, reasoning quality.
- Evaluation Frameworks: HELM, LM-evaluation-harness, custom benchmarks.
- Human vs. Automated Evaluation: When to use expert review vs automated scoring.
- **Lab:** Set up comprehensive evaluation pipelines for LLM applications using multiple metrics.

### **Day 2: Adversarial Testing & Robustness Evaluation**
- Adversarial Prompts: Jailbreaking, prompt injection, red-teaming techniques.
- Robustness Testing: Edge cases, out-of-distribution inputs, stress testing.
- Safety Evaluation: Harmful output detection, bias measurement, fairness testing.
- Automated Red-Teaming: Tools and frameworks for systematic adversarial testing.
- **Lab:** Build automated adversarial test suites and evaluate model robustness against attacks.

### **Day 3: Domain-Specific & Real-World Evaluation**
- Domain Expertise Testing: Medical, legal, financial accuracy evaluation.
- Real-World Performance Metrics: User satisfaction, task completion, ROI measurement.
- A/B Testing for AI: Comparing model performance in production environments.
- Cost-Efficiency Analysis: Balancing accuracy with computational and financial costs.
- **Lab:** Design domain-specific evaluation benchmarks and conduct A/B testing simulations.

### **Day 4: Agent Interpretability & Error Analysis**
- Explainability Testing: Understanding agent decision-making processes.
- Error Pattern Analysis: Systematic failure mode identification and categorization.
- Hallucination Detection: Measuring and mitigating factual inaccuracies.
- Agent Introspection: Self-reflection and confidence calibration evaluation.
- **Lab:** Implement interpretability tools and conduct systematic error analysis on agent outputs.

### **Day 5: Project - AI System Evaluation Dashboard**
- Production Monitoring: Real-time evaluation metrics, alerting systems.
- Evaluation Pipeline Design: Automated testing, continuous evaluation, reporting.
- Multi-Model Comparison: Benchmarking different models and approaches.
- Quality Assurance Framework: Establishing evaluation standards for AI deployment.
- **Project:** Build a comprehensive AI evaluation dashboard that monitors model performance, detects issues, and provides actionable insights for improvement.

---