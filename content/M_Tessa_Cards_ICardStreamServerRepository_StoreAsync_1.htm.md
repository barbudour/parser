# ICardStreamServerRepository.StoreAsync(CardStoreRequest,
IReadOnlyCollection<ICardFileContentProvider>, Nullable<Guid>,
CancellationToken) - метод
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreResponse> StoreAsync(
    	CardStoreRequest request,
    	IReadOnlyCollection<ICardFileContentProvider> files = null,
    	Guid? operationID = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function StoreAsync ( 
    	request As CardStoreRequest,
    	Optional files As IReadOnlyCollection(Of ICardFileContentProvider) = Nothing,
    	Optional operationID As Guid? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
    Task<CardStoreResponse^>^ StoreAsync(
    	CardStoreRequest^ request, 
    	IReadOnlyCollection<ICardFileContentProvider^>^ files = nullptr, 
    	Nullable<Guid> operationID = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            ?files : IReadOnlyCollection<ICardFileContentProvider> * 
            ?operationID : Nullable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _files = defaultArg files null
            let _operationID = defaultArg operationID null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
files
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[ICardFileContentProvider](T_Tessa_Cards_ICardFileContentProvider.htm)>
(Optional)
    Список объектов, обеспечивающих получение контента файла по его идентификатору.
operationID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор операции по сохранению карточки с файлами или null, если операция не была создана. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Ответ на запрос по сохранению карточки.
##  __См. также
#### Ссылки
[ICardStreamServerRepository -
](T_Tessa_Cards_ICardStreamServerRepository.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_ICardStreamServerRepository_StoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
