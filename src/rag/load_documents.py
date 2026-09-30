from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader


BASE_DIR = Path(__file__).resolve().parents[2]
KNOWLEDGE_BASE_DIR = BASE_DIR / "data" / "knowledge_base"


def load_knowledge_base():
    loader = DirectoryLoader(
        str(KNOWLEDGE_BASE_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
    )

    documents = loader.load()

    return documents


if __name__ == "__main__":
    documents = load_knowledge_base()

    print(f"\nLoaded documents: {len(documents)}")

    for document in documents:
        print("-" * 60)
        print(f"Source: {document.metadata.get('source')}")
        print(f"Characters: {len(document.page_content)}")