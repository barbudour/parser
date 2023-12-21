# ApplicationCardQuery.TryGetCardAsync(String, Boolean, CancellationToken) -
метод
Осуществляет попытку получения карточки приложения по псевдониму приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardGetResponse> TryGetCardAsync(
    	[NotNullAttribute] string applicationAlias,
    	bool client64Bit,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetCardAsync ( 
    	<NotNullAttribute> applicationAlias As String,
    	client64Bit As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
     public:
    Task<CardGetResponse^>^ TryGetCardAsync(
    	[NotNullAttribute] String^ applicationAlias, 
    	bool client64Bit, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member TryGetCardAsync : 
            [<NotNullAttribute>] applicationAlias : string * 
            client64Bit : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
#### Параметры
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Псевдоним приложения 
client64Bit [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что приложение использует 64-битную архитектуру.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)>  
Результат выполнения запроса на получение карточки
## __См. также
#### Ссылки
[ApplicationCardQuery -
](T_Tessa_Applications_Synchronization_ApplicationCardQuery.htm)
[TryGetCardAsync -
перегрузка](Overload_Tessa_Applications_Synchronization_ApplicationCardQuery_TryGetCardAsync.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
