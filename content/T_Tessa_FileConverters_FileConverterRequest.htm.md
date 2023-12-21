# FileConverterRequest - класс
Запрос на конвертацию файла.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileConverterRequest : IFileConverterRequest, 
    	ISealable
VB __Копировать
     Public Class FileConverterRequest
    	Implements IFileConverterRequest, ISealable
C++ __Копировать
     public ref class FileConverterRequest : IFileConverterRequest, 
    	ISealable
F# __Копировать
     type FileConverterRequest = 
        class
            interface IFileConverterRequest
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterRequest
Implements
    [IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
Наследники класса могут добавить свойства и переопределить методы
[Serialize(IDictionary<String,
Object>)](M_Tessa_FileConverters_FileConverterRequest_Serialize.htm) и
[Deserialize(IDictionary<String,
Object>)](M_Tessa_FileConverters_FileConverterRequest_Deserialize.htm).
## __Конструкторы
[FileConverterRequest](M_Tessa_FileConverters_FileConverterRequest__ctor.htm)|
Инициализирует новый экземпляр класса FileConverterRequest  
---|---  
##  __Свойства
[CardID](P_Tessa_FileConverters_FileConverterRequest_CardID.htm)|
Идентификатор карточки с преобразуемым файлом.  
---|---  
[CardTypeID](P_Tessa_FileConverters_FileConverterRequest_CardTypeID.htm)|
Идентификатор типа карточки с преобразуемым файлом, который указывается в
запросе на конвертацию CardGetFileContentRequest.CardTypeID, или null, если
свойство не указывается в запросе. От значения этого свойства не зависит
вычисление хеша запроса (и идентификация похожих операций). Значение
необязательно для заполнения, его можно использовать для конвертации
виртуальных файлов.  
[CardTypeName](P_Tessa_FileConverters_FileConverterRequest_CardTypeName.htm)|
Имя типа карточки с преобразуемым файлом, который указывается в запросе на
конвертацию CardGetFileContentRequest.CardTypeName, или null, если свойство не
указывается в запросе. От значения этого свойства не зависит вычисление хеша
запроса (и идентификация похожих операций). Значение необязательно для
заполнения, его можно использовать для конвертации виртуальных файлов.  
[EventName](P_Tessa_FileConverters_FileConverterRequest_EventName.htm)|  Алиас
события, для которого выполняется предпросмотр. Значение используется для
вычисления хеша запроса. Список стандартных алиасов можно получить из класса
[Tessa.FileConverters.FileConverterEventNames].  
[FileID](P_Tessa_FileConverters_FileConverterRequest_FileID.htm)|
Идентификатор преобразуемого файла.  
[FileName](P_Tessa_FileConverters_FileConverterRequest_FileName.htm)|  Имя
преобразуемого файла. При установке автоматически определяет и устанавливает
значение свойства [Tessa.FileConverters.IFileConverterRequest.InputFormat].  
[FileRequestInfo](P_Tessa_FileConverters_FileConverterRequest_FileRequestInfo.htm)|
Дополнительная информация, передаваемая в запрос на конвертацию
CardGetFileContentRequest.Info. От такой информации зависит вычисление хеша
запроса (и идентификация похожих операций). Если от некоторой части этих
данных должен зависеть хеш запроса, то скопируйте их в свойство Parameters.
Значение необязательно для заполнения, его можно использовать для конвертации
виртуальных файлов.  
[FileTypeID](P_Tessa_FileConverters_FileConverterRequest_FileTypeID.htm)|
Идентификатор типа преобразуемого файла, который указывается в запросе на
конвертацию CardGetFileContentRequest.FileTypeID, или null, если свойство не
указывается в запросе. От значения этого свойства зависит вычисление хеша
запроса (и идентификация похожих операций). Значение необязательно для
заполнения, его можно использовать для конвертации виртуальных файлов.  
[FileTypeName](P_Tessa_FileConverters_FileConverterRequest_FileTypeName.htm)|
Имя типа преобразуемого файла, который указывается в запросе на конвертацию
CardGetFileContentRequest.FileTypeName, или null, если свойство не указывается
в запросе. От значения этого свойства зависит вычисление хеша запроса (и
идентификация похожих операций). Значение необязательно для заполнения, его
можно использовать для конвертации виртуальных файлов.  
[Flags](P_Tessa_FileConverters_FileConverterRequest_Flags.htm)| Флаги с
настройками конвертации файлов.  
[Info](P_Tessa_FileConverters_FileConverterRequest_Info.htm)|  Дополнительная
информация, передаваемая в параметры конвертации. От такой информации не
зависит вычисление хеша запроса (и идентификация похожих операций), в отличие
от данных в свойстве [Tessa.FileConverters.IFileConverterRequest.Parameters].  
[InputFormat](P_Tessa_FileConverters_FileConverterRequest_InputFormat.htm)|
Формат преобразуемого файла. Устанавливайте значение этого свойства после
установки [Tessa.FileConverters.IFileConverterRequest.FileName].  
[IsSealed](P_Tessa_FileConverters_FileConverterRequest_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[OutputFormat](P_Tessa_FileConverters_FileConverterRequest_OutputFormat.htm)|
Выходной формат файла. Значение используется для вычисления хеша запроса.  
[Parameters](P_Tessa_FileConverters_FileConverterRequest_Parameters.htm)|
Дополнительная информация, передаваемая в параметры конвертации, которая
влияет на вычисление хеша запроса. Файлы, сгенерированные с разными
параметрами, могут конвертироваться параллельно и могут сохраняться в кэш
одновременно. Если параметры идентичны (а также свойства VersionID, EventName
и OutputFormat), то система считает запросы идентичными, выполнит конвертацию
ровно один раз и вернёт результат из кэша.  
[VersionID](P_Tessa_FileConverters_FileConverterRequest_VersionID.htm)|
Идентификатор версии преобразуемого файла. Значение используется для
вычисления хеша запроса.  
##  __Методы
[CalculateHash](M_Tessa_FileConverters_FileConverterRequest_CalculateHash.htm)|
Вычисляет хеш операции по конвертации для данного запроса, по которому, в том
числе, выполняется сравнение операций и их результатов в кэше. По умолчанию
учитываются значения свойств VersionID, EventName, OutputFormat и Parameters.  
---|---  
[Deserialize](M_Tessa_FileConverters_FileConverterRequest_Deserialize.htm)|
Десериализует информацию из заданного хранилища в свойства текущего объекта.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[ResolveHashData](M_Tessa_FileConverters_FileConverterRequest_ResolveHashData.htm)|
Заполняет хеш-таблицу со свойствами объекта, которые влияют на хеш операции по
конвертации, по которому, в том числе, выполняется сравнение операций и их
результатов в кэше. По умолчанию учитываются значения свойств VersionID,
EventName, OutputFormat и Parameters.  
[Seal](M_Tessa_FileConverters_FileConverterRequest_Seal.htm)| Защищает объект
от изменений.  
[SealInternal](M_Tessa_FileConverters_FileConverterRequest_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[Serialize](M_Tessa_FileConverters_FileConverterRequest_Serialize.htm)|
Сериализует информацию в заданном хранилище для передачи в запускаемую
операцию.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
