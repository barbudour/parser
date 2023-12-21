# FileConverterResponse(ValidationResult, Func<CancellationToken,
ValueTask<Stream>>, Int64, Boolean, Boolean, Dictionary<String, Object>) -
конструктор
Создаёт экземпляр класса с указанием значений его свойств и методов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterResponse(
    	ValidationResult validationResult,
    	Func<CancellationToken, ValueTask<Stream>> getStreamFuncAsync = null,
    	long size = -1,
    	bool isAcquiredFromCache = false,
    	bool hasAwaitedResult = true,
    	Dictionary<string, Object> info = null
    )
VB __Копировать
     Public Sub New ( 
    	validationResult As ValidationResult,
    	Optional getStreamFuncAsync As Func(Of CancellationToken, ValueTask(Of Stream)) = Nothing,
    	Optional size As Long = -1,
    	Optional isAcquiredFromCache As Boolean = false,
    	Optional hasAwaitedResult As Boolean = true,
    	Optional info As Dictionary(Of String, Object) = Nothing
    )
C++ __Копировать
     public:
    FileConverterResponse(
    	ValidationResult^ validationResult, 
    	Func<CancellationToken, ValueTask<Stream^>>^ getStreamFuncAsync = nullptr, 
    	long long size = -1, 
    	bool isAcquiredFromCache = false, 
    	bool hasAwaitedResult = true, 
    	Dictionary<String^, Object^>^ info = nullptr
    )
F# __Копировать
     new : 
            validationResult : ValidationResult * 
            ?getStreamFuncAsync : Func<CancellationToken, ValueTask<Stream>> * 
            ?size : int64 * 
            ?isAcquiredFromCache : bool * 
            ?hasAwaitedResult : bool * 
            ?info : Dictionary<string, Object> 
    (* Defaults:
            let _getStreamFuncAsync = defaultArg getStreamFuncAsync null
            let _size = defaultArg size -1
            let _isAcquiredFromCache = defaultArg isAcquiredFromCache false
            let _hasAwaitedResult = defaultArg hasAwaitedResult true
            let _info = defaultArg info null
    *)
    -> FileConverterResponse
#### Параметры
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
    Результат выполнения операции.
getStreamFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
(Optional)
     Асинхронная функция, которая возвращает поток с содержимым файла, или null, если возвращается пустой поток или результат validationResult содержит ошибки. 
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64) (Optional)
     Размер содержимого getStreamFuncAsync в байтах или -1, если содержимое отсутствует или размер неизвестен. 
isAcquiredFromCache
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что результат конвертации был получен из кэша. 
hasAwaitedResult
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что ожидание результата было выполнено и результат был получен (успешный или с ошибками). Если значение равно false, то метод получения содержимого файла [GetStreamOrThrowAsync(CancellationToken)](M_Tessa_FileConverters_IFileConverterResponse_GetStreamOrThrowAsync.htm) выбросит исключение. 
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, полученная из результатов операции конвертации, или null, если дополнительная информация отсутствует. 
## __См. также
#### Ссылки
[FileConverterResponse - ](T_Tessa_FileConverters_FileConverterResponse.htm)
[FileConverterResponse -
перегрузка](Overload_Tessa_FileConverters_FileConverterResponse__ctor.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
