# IFileConverterContext - интерфейс
Контекст операции конвертации для
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) или
для расширений
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterContext : IExtensionContext
VB __Копировать
     Public Interface IFileConverterContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IFileConverterContext : IExtensionContext
F# __Копировать
     type IFileConverterContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Info](P_Tessa_FileConverters_IFileConverterContext_Info.htm)|
Неструктурированная информация для цепочки расширений. Такая информация нигде
не сохраняется после завершения конвертации.  
[InputExtension](P_Tessa_FileConverters_IFileConverterContext_InputExtension.htm)|
Расширение для конвертируемого файла. Задаётся как расширение файла в нижнем
регистре без ведущей точки. Может быть равно null или пустой строке, если у
файла нет расширения.  
[InputFilePath](P_Tessa_FileConverters_IFileConverterContext_InputFilePath.htm)|
Путь к файлу для пребразования.  
[Operation](P_Tessa_FileConverters_IFileConverterContext_Operation.htm)|
Операция, в рамках которой выполняется конвертация, или null, если операция
неизвестна или отсутствует. Из операции можно получить информацию по тому,
какой сотрудник создал запрос на конвертацию, и, например, в соответствии с
этим локализовать сообщения.  
[OutputExtension](P_Tessa_FileConverters_IFileConverterContext_OutputExtension.htm)|
Расширение для выходного формата файла. Задаётся как расширение файла в нижнем
регистре без ведущей точки. Может быть равно null или пустой строке, если у
файла нет расширения.  
[OutputFilePath](P_Tessa_FileConverters_IFileConverterContext_OutputFilePath.htm)|
Путь к выходному файлу. Может быть изменён, если приложение-конвертер записало
файл по другому пути. Не может быть равен null или пустой строке.  
[Request](P_Tessa_FileConverters_IFileConverterContext_Request.htm)|  Запрос
на выполнение операции, в рамках которого выполняется конвертация, или null,
если запрос неизвестен или отсутствует.  
[RequestInfo](P_Tessa_FileConverters_IFileConverterContext_RequestInfo.htm)|
Информация, полученная из запроса на выполнение операции. В отличие от
свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.  
[RequestIsSuccessful](P_Tessa_FileConverters_IFileConverterContext_RequestIsSuccessful.htm)|
Признак того, что запрос успешно выполнен. Проверять значение рекомендуется
только в методах расширений AfterRequest.  
[RequestParameters](P_Tessa_FileConverters_IFileConverterContext_RequestParameters.htm)|
Параметры, полученные из запроса на выполнение операции, которые влияют на
вычисление хеша запроса. Файлы, сгенерированные с разными параметрами, могут
конвертироваться параллельно и могут сохраняться в кэш одновременно. В отличие
от свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.  
[ResponseInfo](P_Tessa_FileConverters_IFileConverterContext_ResponseInfo.htm)|
Информация, передаваемая вместе с результатом выполнения операции.  
[ValidationResult](P_Tessa_FileConverters_IFileConverterContext_ValidationResult.htm)|
Результат валидации, содержащий сообщения, возникающие в процессе конвертации.
Если сообщения содержат ошибки, то считается, что конвертация не выполнена и
выходной файл может отсутствовать.  
## __Методы расширения
[GetOutputStreamOrThrow](M_Tessa_FileConverters_FileConverterExtensions_GetOutputStreamOrThrow.htm)|
Возвращает поток на выходной файл или выбрасывает исключение, если файл не
найден или произошла другая ошибка при его открытии. Возвращённый поток
необходимо закрыть вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose).  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
