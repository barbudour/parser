# FileLocalCache - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileLocalCache(
    	[OptionalDependencyAttribute] IFileContentNameReplacer nameReplacer = null
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> Optional nameReplacer As IFileContentNameReplacer = Nothing
    )
C++ __Копировать
     public:
    FileLocalCache(
    	[OptionalDependencyAttribute] IFileContentNameReplacer^ nameReplacer = nullptr
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] ?nameReplacer : IFileContentNameReplacer 
    (* Defaults:
            let _nameReplacer = defaultArg nameReplacer null
    *)
    -> FileLocalCache
#### Параметры
nameReplacer
[IFileContentNameReplacer](T_Tessa_Files_IFileContentNameReplacer.htm)
(Optional)
     Объект, выполняющий исправление имени файла, создаваемого в кэше, или null, если используется исправление по умолчанию. 
## __См. также
#### Ссылки
[FileLocalCache - ](T_Tessa_Files_FileLocalCache.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
