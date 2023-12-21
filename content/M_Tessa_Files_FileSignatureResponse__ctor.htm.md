# FileSignatureResponse - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSignatureResponse(
    	IFileVersion version,
    	IFileSignatureCollection signatures,
    	bool allowCaching = true,
    	ValidationResult validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	version As IFileVersion,
    	signatures As IFileSignatureCollection,
    	Optional allowCaching As Boolean = true,
    	Optional validationResult As ValidationResult = Nothing
    )
C++ __Копировать
     public:
    FileSignatureResponse(
    	IFileVersion^ version, 
    	IFileSignatureCollection^ signatures, 
    	bool allowCaching = true, 
    	ValidationResult^ validationResult = nullptr
    )
F# __Копировать
     new : 
            version : IFileVersion * 
            signatures : IFileSignatureCollection * 
            ?allowCaching : bool * 
            ?validationResult : ValidationResult 
    (* Defaults:
            let _allowCaching = defaultArg allowCaching true
            let _validationResult = defaultArg validationResult null
    *)
    -> FileSignatureResponse
#### Параметры
version [IFileVersion](T_Tessa_Files_IFileVersion.htm)
    Версия файла, для которой был выполнен запрос.
signatures
[IFileSignatureCollection](T_Tessa_Files_IFileSignatureCollection.htm)
    Коллекция подписей, доступных для версии файла.
allowCaching [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что полученный список подписей может быть сохранён для последующего многократного использования. 
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
(Optional)
     Результат валидации, отражающий произошедшие события и ошибки в процессе выполнения запроса, или null, если событий и ошибок не происходило. 
## __См. также
#### Ссылки
[FileSignatureResponse - ](T_Tessa_Files_FileSignatureResponse.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
