# ApplicationCardCreator.CreateApplicationCardAsync - метод
Создает карточку приложения с идентификатором cardId
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public Task<CardNewResponse> CreateApplicationCardAsync(
    	Guid cardId,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <NotNullAttribute>
    Public Function CreateApplicationCardAsync ( 
    	cardId As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardNewResponse)
C++ __Копировать
     public:
    [NotNullAttribute]
    Task<CardNewResponse^>^ CreateApplicationCardAsync(
    	Guid cardId, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<NotNullAttribute>]
    member CreateApplicationCardAsync : 
            cardId : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardNewResponse> 
#### Параметры
cardId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>  
Результат создания карточки
## __См. также
#### Ссылки
[ApplicationCardCreator -
](T_Tessa_Applications_Synchronization_ApplicationCardCreator.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
