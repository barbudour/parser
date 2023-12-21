# IFileConverterComposer.InProgressAsync - метод
Возвращает признак того, что операция по конвертации запущена и ещё
выполняется. Возвращает false, если операция завершилась или она была удалена
(например, администратором).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> InProgressAsync(
    	Guid operationID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InProgressAsync ( 
    	operationID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ InProgressAsync(
    	Guid operationID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InProgressAsync : 
            operationID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
operationID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор операции по конвертации файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если операция по конвертации запущена и ещё выполняется; false в
противном случае.
## __См. также
#### Ссылки
[IFileConverterComposer - ](T_Tessa_FileConverters_IFileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
