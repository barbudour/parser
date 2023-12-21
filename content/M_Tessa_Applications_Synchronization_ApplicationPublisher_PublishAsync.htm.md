# ApplicationPublisher.PublishAsync - метод
Выполняет публикацию приложения.
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task PublishAsync(
    	IApplicationContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function PublishAsync ( 
    	context As IApplicationContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ PublishAsync(
    	IApplicationContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract PublishAsync : 
            context : IApplicationContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override PublishAsync : 
            context : IApplicationContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IApplicationContext](T_Tessa_Platform_Runtime_IApplicationContext.htm)
    Контекст, связанный с запуском приложения в режиме публикации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationPublisher.PublishAsync(IApplicationContext,
CancellationToken)](M_Tessa_Platform_Runtime_IApplicationPublisher_PublishAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationPublisher -
](T_Tessa_Applications_Synchronization_ApplicationPublisher.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
