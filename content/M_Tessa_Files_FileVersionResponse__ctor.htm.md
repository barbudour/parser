# FileVersionResponse - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileVersionResponse(
    	IFile file,
    	IFileVersionCollection versions,
    	bool allowCaching = true,
    	ValidationResult validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	file As IFile,
    	versions As IFileVersionCollection,
    	Optional allowCaching As Boolean = true,
    	Optional validationResult As ValidationResult = Nothing
    )
C++ __Копировать
     public:
    FileVersionResponse(
    	IFile^ file, 
    	IFileVersionCollection^ versions, 
    	bool allowCaching = true, 
    	ValidationResult^ validationResult = nullptr
    )
F# __Копировать
     new : 
            file : IFile * 
            versions : IFileVersionCollection * 
            ?allowCaching : bool * 
            ?validationResult : ValidationResult 
    (* Defaults:
            let _allowCaching = defaultArg allowCaching true
            let _validationResult = defaultArg validationResult null
    *)
    -> FileVersionResponse
#### Параметры
file [IFile](T_Tessa_Files_IFile.htm)
    Файл, для которого был выполнен запрос.
versions [IFileVersionCollection](T_Tessa_Files_IFileVersionCollection.htm)
    Коллекция версий, доступных для файла.
allowCaching [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что полученный список версий может быть сохранён для последующего многократного использования. 
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
(Optional)
     Результат валидации, отражающий произошедшие события и ошибки в процессе выполнения запроса, или null, если событий и ошибок не происходило. 
## __См. также
#### Ссылки
[FileVersionResponse - ](T_Tessa_Files_FileVersionResponse.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
