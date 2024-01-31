#### Forked from (https://github.com/PromptEngineer48/Ollama), inspired from ((https://github.com/imartinez/privateGPT) and (https://github.com/jmorganca/ollama)

#### Step 1: Setup a Virtual Environment

Python should be > 3.8
```
python3 --version
python3 -m venv .env
. .env/bin/activate
```

#### Upgrade VENV's PIP

```
python -m pip install --upgrade pip
```

#### Avoid deprecations when installing requirements

```
python -m pip install wheel
```

#### Step 2: Install the Requirements

```
python -m pip install -r requirements.txt
```

#### Step 3: Pull the models (if you already have models loaded in Ollama, then not required)
#### Make sure to have Ollama running on your system from https://ollama.ai
```
ollama pull mistral
```

#### Step 4: put your files in the source_documents folder after making a directory
```
mkdir source_documents
```

#### Step 5: Ingest the files (use python3 if on mac)
```
python ingest.py
```

Output should look like this:
```shell
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|██████████████████████| 1/1 [00:01<00:00,  1.99s/it]
Loaded 235 new documents from source_documents
Split into 1268 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes...
Ingestion complete! You can now run privateGPT.py to query your documents
```

#### Step 6: Run this command (use python3 if on mac)
```
python privateGPT.py
```

##### Play with your docs
Enter a query: How many locations does WeWork have?


### Try with a different model:
```
ollama pull llama2:13b
MODEL=llama2:13b python privateGPT.py
```

## Add more files

Put any and all your files into the `source_documents` directory

The supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),
