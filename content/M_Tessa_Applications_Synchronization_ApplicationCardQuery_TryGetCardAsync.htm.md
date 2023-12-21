# ApplicationCardQuery.TryGetCardAsync(Guid, CancellationToken) - метод
Осуществляет попытку получения карточки приложения по идентификатору карточки.
Если карточка с указанным идентификатором не существует будет возвращает null
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardGetResponse> TryGetCardAsync(
    	Guid cardId,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetCardAsync ( 
    	cardId As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
     public:
    Task<CardGetResponse^>^ TryGetCardAsync(
    	Guid cardId, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member TryGetCardAsync : 
            cardId : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
#### Параметры
cardId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)>  
Результат запроса к карточке или null
##  __См. также
#### Ссылки
[ApplicationCardQuery -
](T_Tessa_Applications_Synchronization_ApplicationCardQuery.htm)
[TryGetCardAsync -
перегрузка](Overload_Tessa_Applications_Synchronization_ApplicationCardQuery_TryGetCardAsync.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
