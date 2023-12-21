# FileConverterContext - класс
Контекст операции конвертации для
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) или
для расширений
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileConverterContext : IFileConverterContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class FileConverterContext
    	Implements IFileConverterContext, IExtensionContext
C++ __Копировать
     public ref class FileConverterContext sealed : IFileConverterContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type FileConverterContext = 
        class
            interface IFileConverterContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)
##  __Конструкторы
[FileConverterContext(String, String, IFileConverterRequest, IOperation,
CancellationToken)](M_Tessa_FileConverters_FileConverterContext__ctor_1.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
[FileConverterContext(String, String, String, String, IFileConverterRequest,
IOperation,
CancellationToken)](M_Tessa_FileConverters_FileConverterContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
## __Свойства
[CancellationToken](P_Tessa_FileConverters_FileConverterContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[Info](P_Tessa_FileConverters_FileConverterContext_Info.htm)|
Неструктурированная информация для цепочки расширений. Такая информация нигде
не сохраняется после завершения конвертации.  
[InputExtension](P_Tessa_FileConverters_FileConverterContext_InputExtension.htm)|
Расширение для конвертируемого файла. Задаётся как расширение файла в нижнем
регистре без ведущей точки. Может быть равно null или пустой строке, если у
файла нет расширения.  
[InputFilePath](P_Tessa_FileConverters_FileConverterContext_InputFilePath.htm)|
Путь к файлу для пребразования.  
[Operation](P_Tessa_FileConverters_FileConverterContext_Operation.htm)|
Операция, в рамках которой выполняется конвертация, или null, если операция
неизвестна или отсутствует. Из операции можно получить информацию по тому,
какой сотрудник создал запрос на конвертацию, и, например, в соответствии с
этим локализовать сообщения.  
[OutputExtension](P_Tessa_FileConverters_FileConverterContext_OutputExtension.htm)|
Расширение для выходного формата файла. Задаётся как расширение файла в нижнем
регистре без ведущей точки. Может быть равно null или пустой строке, если у
файла нет расширения.  
[OutputFilePath](P_Tessa_FileConverters_FileConverterContext_OutputFilePath.htm)|
Путь к выходному файлу. Может быть изменён, если приложение-конвертер записало
файл по другому пути. Не может быть равен null или пустой строке.  
[Request](P_Tessa_FileConverters_FileConverterContext_Request.htm)|  Запрос на
выполнение операции, в рамках которого выполняется конвертация, или null, если
запрос неизвестен или отсутствует.  
[RequestInfo](P_Tessa_FileConverters_FileConverterContext_RequestInfo.htm)|
Информация, полученная из запроса на выполнение операции. В отличие от
свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.  
[RequestIsSuccessful](P_Tessa_FileConverters_FileConverterContext_RequestIsSuccessful.htm)|
Признак того, что запрос успешно выполнен. Проверять значение рекомендуется
только в методах расширений AfterRequest.  
[RequestParameters](P_Tessa_FileConverters_FileConverterContext_RequestParameters.htm)|
Параметры, полученные из запроса на выполнение операции, которые влияют на
вычисление хеша запроса. Файлы, сгенерированные с разными параметрами, могут
конвертироваться параллельно и могут сохраняться в кэш одновременно. В отличие
от свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.  
[ResponseInfo](P_Tessa_FileConverters_FileConverterContext_ResponseInfo.htm)|
Информация, передаваемая вместе с результатом выполнения операции.  
[ValidationResult](P_Tessa_FileConverters_FileConverterContext_ValidationResult.htm)|
Результат валидации, содержащий сообщения, возникающие в процессе конвертации.
Если сообщения содержат ошибки, то считается, что конвертация не выполнена и
выходной файл может отсутствовать.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetOutputStreamOrThrow](M_Tessa_FileConverters_FileConverterExtensions_GetOutputStreamOrThrow.htm)|
Возвращает поток на выходной файл или выбрасывает исключение, если файл не
найден или произошла другая ошибка при его открытии. Возвращённый поток
необходимо закрыть вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose).  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
