# ISynchronizationTarget.TryGetApplicationPackageAsync - метод
Возвращает пакет приложения содержащий файлы которые содержатся в целевом
объекте синхронизации. В случае ошибки получения или отсутствия приложения в
целевом объекте возвращает null. Ошибки получения пакета приложения
записываются в validationResultBuilder
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ApplicationPackage> TryGetApplicationPackageAsync(
    	[NotNullAttribute] ValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetApplicationPackageAsync ( 
    	<NotNullAttribute> validationResultBuilder As ValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ApplicationPackage)
C++ __Копировать
    Task<ApplicationPackage^>^ TryGetApplicationPackageAsync(
    	[NotNullAttribute] ValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetApplicationPackageAsync : 
            [<NotNullAttribute>] validationResultBuilder : ValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ApplicationPackage> 
#### Параметры
validationResultBuilder
[ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm)
     Построитель результатов валидации 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)>  
Пакет приложения или null
##  __См. также
#### Ссылки
[ISynchronizationTarget -
](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
