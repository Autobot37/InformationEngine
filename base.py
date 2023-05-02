from typing import Generator, Optional, Dict, List, Set, Union, Any
FilterType = Dict[str, Union[Dict[str, Any], List[Any], str, int, float, bool]]

class BaseDocumentStore:

    label_index:Optional[str]
    similarity:Optional[str]

    def write_document(self,
                        documents:Union[List[dict],List[Document]],
                        index:Optional[str] = None,
                        batch_size:int = 10_000, 
                        ):
                        pass
    def get_all_documents(self,index,filters:Optional[FilterType]=None,return_embeddings,batch_size):
        pass

class KeywordDocumentSearch(BaseDocumentStore):

    @abstractmethod
    def query(self,query,filters,tok_k,index,scale_score) -> List[Document]:
        pass
    



    


    