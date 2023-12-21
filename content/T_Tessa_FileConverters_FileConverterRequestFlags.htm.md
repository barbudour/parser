# FileConverterRequestFlags - перечисление
Флаги с настройками конвертации файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum FileConverterRequestFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration FileConverterRequestFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class FileConverterRequestFlags
F# __Копировать
     [<FlagsAttribute>]
    type FileConverterRequestFlags
##  __Члены
None| 0|  Флаги отсутствуют, конвертация выполняется с настройками по
умолчанию.  
---|---|---  
IgnoreCacheBeforeConversion| 1|  Признак того, что гарантированно будет
выполнена новая конвертация, даже если файл уже присутствует в кэше.  
DoNotCacheResult| 2|  Результат конвертации не будет помещён в кэш. В таком
случае расширение
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm)
может получить файл с результатом, обработать его, после чего файл будет
удалён, и в следующий раз конвертация снова будет выполнена без обращения к
кэшу. Содержимое такого файла нельзя получить через метод
[ConvertFileAsync(IFileConverterRequest,
CancellationToken)](M_Tessa_FileConverters_IFileConverter_ConvertFileAsync.htm).  
DoNotAwaitResult| 4|  Ожидание завершения операции не будет выполнено. Укажите
флаг, если объект пытается получить значение из кэша, и как в случае неудачи,
так и в случае успеха сразу же возвращает управление. Если объекта в кэше не
было, то будет запущена операция, если она ещё не была запущена.  
WithoutResponse| 8|  Операция будет удалена вместо отметки о завершении.
Рекомендуется установить, если вызывающий код не будет ожидать завершения
операции и не будет получать её результат. При получении результата такой
операции возникнет ошибка.  
AllowConcurrentIdenticOperations| 16|  Признак того, что при конвертации
разрешено параллельное выполнение операций с идентичными параметрами в запросе
в соответствии с вычисленным значением хеша запроса
[CalculateHash(ISignatureProvider)](M_Tessa_FileConverters_IFileConverterRequest_CalculateHash.htm).  
## __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
