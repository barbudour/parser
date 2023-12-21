# FileResponse - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileResponse(
    	IFileCollection files,
    	ValidationResult validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	files As IFileCollection,
    	Optional validationResult As ValidationResult = Nothing
    )
C++ __Копировать
     public:
    FileResponse(
    	IFileCollection^ files, 
    	ValidationResult^ validationResult = nullptr
    )
F# __Копировать
     new : 
            files : IFileCollection * 
            ?validationResult : ValidationResult 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> FileResponse
#### Параметры
files [IFileCollection](T_Tessa_Files_IFileCollection.htm)
    Коллекция доступных файлов.
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
(Optional)
     Результат валидации, отражающий произошедшие события и ошибки в процессе выполнения запроса, или null, если событий и ошибок не происходило. 
## __См. также
#### Ссылки
[FileResponse - ](T_Tessa_Files_FileResponse.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
