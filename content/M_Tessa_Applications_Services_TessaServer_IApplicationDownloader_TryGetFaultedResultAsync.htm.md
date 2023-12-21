# IApplicationDownloader.TryGetFaultedResultAsync - метод
Возвращает ошибки при скачивании приложения как объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm), или
null, если информация недоступна: ошибок не было или пользователь не имеет
доступа к этой записи в истории.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ValidationResult> TryGetFaultedResultAsync(
    	Guid rowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetFaultedResultAsync ( 
    	rowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
    Task<ValidationResult^>^ TryGetFaultedResultAsync(
    	Guid rowID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetFaultedResultAsync : 
            rowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор записи в истории, которая возвращается в свойстве [ActionHistoryRowID](P_Tessa_Applications_Package_ApplicationPackage_ActionHistoryRowID.htm) для загруженного пакета. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Объект [ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm),
или null, если информация по ошибке скачивания недоступна.
## __См. также
#### Ссылки
[IApplicationDownloader -
](T_Tessa_Applications_Services_TessaServer_IApplicationDownloader.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
