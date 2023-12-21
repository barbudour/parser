# IApplicationSynchronizationStrategy.StartSynchronizationAsync - метод
Вызывается при запуске процесса синхронизации
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task StartSynchronizationAsync(
    	[NotNullAttribute] ApplicationPackage applicationPackage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function StartSynchronizationAsync ( 
    	<NotNullAttribute> applicationPackage As ApplicationPackage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ StartSynchronizationAsync(
    	[NotNullAttribute] ApplicationPackage^ applicationPackage, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract StartSynchronizationAsync : 
            [<NotNullAttribute>] applicationPackage : ApplicationPackage * 
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
##  __См. также
#### Ссылки
[IApplicationSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
