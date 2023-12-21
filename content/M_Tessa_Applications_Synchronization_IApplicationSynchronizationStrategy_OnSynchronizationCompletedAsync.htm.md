# IApplicationSynchronizationStrategy.OnSynchronizationCompletedAsync - метод
Вызывается при завершении синхронизации элементов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task OnSynchronizationCompletedAsync(
    	[NotNullAttribute] ApplicationPackage applicationPackage,
    	[NotNullAttribute] ValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function OnSynchronizationCompletedAsync ( 
    	<NotNullAttribute> applicationPackage As ApplicationPackage,
    	<NotNullAttribute> validationResultBuilder As ValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ OnSynchronizationCompletedAsync(
    	[NotNullAttribute] ApplicationPackage^ applicationPackage, 
    	[NotNullAttribute] ValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract OnSynchronizationCompletedAsync : 
            [<NotNullAttribute>] applicationPackage : ApplicationPackage * 
            [<NotNullAttribute>] validationResultBuilder : ValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
applicationPackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
validationResultBuilder
[ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm)
     Построитель результатов валидации 
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
