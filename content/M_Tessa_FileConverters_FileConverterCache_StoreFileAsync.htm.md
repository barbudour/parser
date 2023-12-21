# FileConverterCache.StoreFileAsync - метод
Сохраняет преобразованный файл в кэше и возвращает результат операции по
сохранению. Возвращаемое значение не равно null.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> StoreFileAsync(
    	Guid versionID,
    	byte[] requestHash,
    	Guid fileID,
    	string fileName,
    	string contentFilePath,
    	Dictionary<string, Object> responseInfo = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreFileAsync ( 
    	versionID As Guid,
    	requestHash As Byte(),
    	fileID As Guid,
    	fileName As String,
    	contentFilePath As String,
    	Optional responseInfo As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ StoreFileAsync(
    	Guid versionID, 
    	array<unsigned char>^ requestHash, 
    	Guid fileID, 
    	String^ fileName, 
    	String^ contentFilePath, 
    	Dictionary<String^, Object^>^ responseInfo = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreFileAsync : 
            versionID : Guid * 
            requestHash : byte[] * 
            fileID : Guid * 
            fileName : string * 
            contentFilePath : string * 
            ?responseInfo : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _responseInfo = defaultArg responseInfo null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override StoreFileAsync : 
            versionID : Guid * 
            requestHash : byte[] * 
            fileID : Guid * 
            fileName : string * 
            contentFilePath : string * 
            ?responseInfo : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _responseInfo = defaultArg responseInfo null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
versionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии исходного файла.
requestHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Хеш от запроса на преобразование файла.
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор преобразованного файла. Обычно здесь создают новый уникальный идентификатор.
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя преобразованного файла с расширением.
contentFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
     Путь к содержимому преобразованного файла. Обычно файл размещается во временной папке. 
responseInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Информация из ответа на запрос по конвертированию файла или null, если такая информация отсутствует. Пустая хеш-таблица будет сериализована точно так же, как и значение null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат операции по сохранению. Возвращаемое значение не равно null.
#### Реализации
[IFileConverterCache.StoreFileAsync(Guid, Byte[], Guid, String, String,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_StoreFileAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
