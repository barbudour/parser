# CardGetComponent.GetFileVersionsAsync - метод
Загружает версии файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardGetFileVersionsResponse> GetFileVersionsAsync(
    	CardGetFileVersionsRequest request,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFileVersionsAsync ( 
    	request As CardGetFileVersionsRequest,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetFileVersionsResponse)
C++ __Копировать
     public:
    virtual Task<CardGetFileVersionsResponse^>^ GetFileVersionsAsync(
    	CardGetFileVersionsRequest^ request, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetFileVersionsAsync : 
            request : CardGetFileVersionsRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetFileVersionsResponse> 
    override GetFileVersionsAsync : 
            request : CardGetFileVersionsRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetFileVersionsResponse> 
#### Параметры
request
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm)
    Запрос на загрузку версий файла.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего загрузку версий файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm)>  
Ответ на запрос по загрузке версий файла.
#### Реализации
[ICardGetComponent.GetFileVersionsAsync(CardGetFileVersionsRequest,
ICardMetadata, ISession,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetComponent_GetFileVersionsAsync.htm)  
##  __См. также
#### Ссылки
[CardGetComponent - ](T_Tessa_Cards_ComponentModel_CardGetComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
