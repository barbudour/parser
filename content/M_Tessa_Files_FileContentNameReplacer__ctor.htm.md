# FileContentNameReplacer - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileContentNameReplacer(
    	[OptionalDependencyAttribute] IFileContentOptions contentOptions = null
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> Optional contentOptions As IFileContentOptions = Nothing
    )
C++ __Копировать
     public:
    FileContentNameReplacer(
    	[OptionalDependencyAttribute] IFileContentOptions^ contentOptions = nullptr
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] ?contentOptions : IFileContentOptions 
    (* Defaults:
            let _contentOptions = defaultArg contentOptions null
    *)
    -> FileContentNameReplacer
#### Параметры
contentOptions [IFileContentOptions](T_Tessa_Files_IFileContentOptions.htm)
(Optional)
     Настройки, связанные с хранением контента файлов, или null, если используются настройки по умолчанию. 
## __См. также
#### Ссылки
[FileContentNameReplacer - ](T_Tessa_Files_FileContentNameReplacer.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
