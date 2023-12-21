# ICardStreamServerRepository - методы
##  __Методы
[GetFileContentAsAggregatedStreamAsync](M_Tessa_Cards_ICardStreamServerRepository_GetFileContentAsAggregatedStreamAsync.htm)|
Получает контент версии файла в виде агрегированного потока, в котором
содержится ответ на запрос и собственно контент.  
---|---  
[GetFileContentAsync](M_Tessa_Cards_ICardStreamServerRepository_GetFileContentAsync.htm)|
Получает контент версии файла.  
[StoreAsync(Stream, CardServiceType,
CancellationToken)](M_Tessa_Cards_ICardStreamServerRepository_StoreAsync.htm)|
Сохраняет карточку и её файлы, переданные в потоке карточки.  
[StoreAsync(CardStoreRequest, IReadOnlyCollection<ICardFileContentProvider>,
Nullable<Guid>,
CancellationToken)](M_Tessa_Cards_ICardStreamServerRepository_StoreAsync_1.htm)|
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].  
## __Методы расширения
[GenerateFileFromTemplateAsync](M_Tessa_Cards_CardExtensions_GenerateFileFromTemplateAsync_1.htm)|
Асинхронно создаёт файл по заданному шаблону и возвращает контент созданного
файла и ответ на запрос на создание.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[ICardStreamServerRepository -
](T_Tessa_Cards_ICardStreamServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
