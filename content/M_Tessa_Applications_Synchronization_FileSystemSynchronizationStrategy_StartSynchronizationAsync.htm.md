# FileSystemSynchronizationStrategy.StartSynchronizationAsync - метод
Вызывается при запуске процесса синхронизации
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StartSynchronizationAsync(
    	ApplicationPackage applicationPackage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StartSynchronizationAsync ( 
    	applicationPackage As ApplicationPackage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StartSynchronizationAsync(
    	ApplicationPackage^ applicationPackage, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StartSynchronizationAsync : 
            applicationPackage : ApplicationPackage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override StartSynchronizationAsync : 
            applicationPackage : ApplicationPackage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
applicationPackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationSynchronizationStrategy.StartSynchronizationAsync(ApplicationPackage,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_StartSynchronizationAsync.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
