# IFileConverterCache.TryGetResponseInfoAsync - метод
Возвращает информацию Info из ответа на запрос по выполнению конвертации,
которая была сохранена в кэше, или null, если либо в кэше нет файла с заданным
идентификатором, либо при конвертации не была указана информация.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<Dictionary<string, Object>> TryGetResponseInfoAsync(
    	Guid convertedFileID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetResponseInfoAsync ( 
    	convertedFileID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Dictionary(Of String, Object))
C++ __Копировать
    Task<Dictionary<String^, Object^>^>^ TryGetResponseInfoAsync(
    	Guid convertedFileID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetResponseInfoAsync : 
            convertedFileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Dictionary<string, Object>> 
#### Параметры
convertedFileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла в карточке кэша.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>  
Информацию Info из ответа на запрос по выполнению конвертации, которая была
сохранена в кэше, или null, если либо в кэше нет файла с заданным
идентификатором, либо при конвертации не была указана информация.
## __См. также
#### Ссылки
[IFileConverterCache - ](T_Tessa_FileConverters_IFileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
