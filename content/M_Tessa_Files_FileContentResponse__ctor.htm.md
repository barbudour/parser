# FileContentResponse - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileContentResponse(
    	IFileVersion version,
    	ValidationResult validationResult = null,
    	string suggestedFileName = null
    )
VB __Копировать
     Public Sub New ( 
    	version As IFileVersion,
    	Optional validationResult As ValidationResult = Nothing,
    	Optional suggestedFileName As String = Nothing
    )
C++ __Копировать
     public:
    FileContentResponse(
    	IFileVersion^ version, 
    	ValidationResult^ validationResult = nullptr, 
    	String^ suggestedFileName = nullptr
    )
F# __Копировать
     new : 
            version : IFileVersion * 
            ?validationResult : ValidationResult * 
            ?suggestedFileName : string 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
            let _suggestedFileName = defaultArg suggestedFileName null
    *)
    -> FileContentResponse
#### Параметры
version [IFileVersion](T_Tessa_Files_IFileVersion.htm)
    Версия файла, для которой был выполнен запрос.
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
(Optional)
     Результат валидации, отражающий произошедшие события и ошибки в процессе выполнения запроса, или null, если событий и ошибок не происходило. 
suggestedFileName
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Предпочитаемое название загруженного файла или null, если название не изменяется относительно заданного в версии. 
## __См. также
#### Ссылки
[FileContentResponse - ](T_Tessa_Files_FileContentResponse.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
