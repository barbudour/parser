# IFileConverterComposer.EndConversionAsync - метод
Возвращает результат конвертации, который предоставляет доступ к содержимому
файла, для которого была выполнена конвертация. После выполнения функции
операция удаляется, поэтому повторный вызов метода возвращает ошибку.
Результат всегда не равен null, ошибки и исключения будут сохранены в объекте
результата.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<IFileConverterResponse> EndConversionAsync(
    	Guid operationID,
    	bool? resultIsNotCached = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function EndConversionAsync ( 
    	operationID As Guid,
    	Optional resultIsNotCached As Boolean? = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IFileConverterResponse)
C++ __Копировать
    Task<IFileConverterResponse^>^ EndConversionAsync(
    	Guid operationID, 
    	Nullable<bool> resultIsNotCached = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract EndConversionAsync : 
            operationID : Guid * 
            ?resultIsNotCached : Nullable<bool> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _resultIsNotCached = defaultArg resultIsNotCached false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IFileConverterResponse> 
#### Параметры
operationID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор операции по конвертации файла.
resultIsNotCached
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
     Признак того, что результат операции не добавлен в кэш файлов на основании флага [Tessa.FileConverters.FileConverterRequestFlags.DoNotCacheResult]. Если указано значение null, то флаг определяется на основании значения, сериализованного в операции при запуске, при этом информация десериализуется теми же средствами, которые использовались методом [Tessa.FileConverters.IFileConverterComposer.BeginConversionAsync] для сериализации при создании операции. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IFileConverterResponse](T_Tessa_FileConverters_IFileConverterResponse.htm)>  
Результат конвертации, который предоставляет доступ к содержимому файла, для
которого была выполнена конвертация. Результат всегда не равен null, ошибки и
исключения будут сохранены в объекте результата.
## __См. также
#### Ссылки
[IFileConverterComposer - ](T_Tessa_FileConverters_IFileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
