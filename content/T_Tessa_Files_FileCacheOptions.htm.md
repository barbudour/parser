# FileCacheOptions - перечисление
Опции, которые дополнительно поддерживает кэш файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum FileCacheOptions
VB __Копировать
    <FlagsAttribute>
    Public Enumeration FileCacheOptions
C++ __Копировать
    [FlagsAttribute]
    public enum class FileCacheOptions
F# __Копировать
     [<FlagsAttribute>]
    type FileCacheOptions
##  __Члены
None| 0|  Кэш файлов не поддерживает дополнительных опций.  
---|---|---  
SupportsDelayedDisposal| 1|  Кэш файлов поддерживает отложенное освобождение
содержимого (удаление временных файлов), если его не удалось удалить сразу в
вызове метода IFileContent.Dispose() (например, если другой объект блокирует
удаление файла).  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
