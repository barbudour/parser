# IAvailableApplicationsQuery.TryGetApplicationIdAsync - метод
Осуществляет попытку получения идентификатора приложения по его алиасу.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<Guid?> TryGetApplicationIdAsync(
    	string applicationAlias,
    	bool client64Bit,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetApplicationIdAsync ( 
    	applicationAlias As String,
    	client64Bit As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
    Task<Nullable<Guid>>^ TryGetApplicationIdAsync(
    	String^ applicationAlias, 
    	bool client64Bit, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetApplicationIdAsync : 
            applicationAlias : string * 
            client64Bit : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Алиас приложения.
client64Bit [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что приложение использует 64-битную архитектуру.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор приложения или null, если карточка отсутствует.
##  __См. также
#### Ссылки
[IAvailableApplicationsQuery -
](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
