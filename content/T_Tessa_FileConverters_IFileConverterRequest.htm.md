# IFileConverterRequest - интерфейс
Запрос на конвертацию файла.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterRequest : ISealable
VB __Копировать
     Public Interface IFileConverterRequest
    	Inherits ISealable
C++ __Копировать
     public interface class IFileConverterRequest : ISealable
F# __Копировать
     type IFileConverterRequest = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[CardID](P_Tessa_FileConverters_IFileConverterRequest_CardID.htm)|
Идентификатор карточки с преобразуемым файлом.  
---|---  
[CardTypeID](P_Tessa_FileConverters_IFileConverterRequest_CardTypeID.htm)|
Идентификатор типа карточки с преобразуемым файлом, который указывается в
запросе на конвертацию CardGetFileContentRequest.CardTypeID, или null, если
свойство не указывается в запросе. От значения этого свойства не зависит
вычисление хеша запроса (и идентификация похожих операций). Значение
необязательно для заполнения, его можно использовать для конвертации
виртуальных файлов.  
[CardTypeName](P_Tessa_FileConverters_IFileConverterRequest_CardTypeName.htm)|
Имя типа карточки с преобразуемым файлом, который указывается в запросе на
конвертацию CardGetFileContentRequest.CardTypeName, или null, если свойство не
указывается в запросе. От значения этого свойства не зависит вычисление хеша
запроса (и идентификация похожих операций). Значение необязательно для
заполнения, его можно использовать для конвертации виртуальных файлов.  
[EventName](P_Tessa_FileConverters_IFileConverterRequest_EventName.htm)|
Алиас события, для которого выполняется предпросмотр. Значение используется
для вычисления хеша запроса. Список стандартных алиасов можно получить из
класса [Tessa.FileConverters.FileConverterEventNames].  
[FileID](P_Tessa_FileConverters_IFileConverterRequest_FileID.htm)|
Идентификатор преобразуемого файла.  
[FileName](P_Tessa_FileConverters_IFileConverterRequest_FileName.htm)|  Имя
преобразуемого файла. При установке автоматически определяет и устанавливает
значение свойства [Tessa.FileConverters.IFileConverterRequest.InputFormat].  
[FileRequestInfo](P_Tessa_FileConverters_IFileConverterRequest_FileRequestInfo.htm)|
Дополнительная информация, передаваемая в запрос на конвертацию
CardGetFileContentRequest.Info. От такой информации зависит вычисление хеша
запроса (и идентификация похожих операций). Если от некоторой части этих
данных должен зависеть хеш запроса, то скопируйте их в свойство Parameters.
Значение необязательно для заполнения, его можно использовать для конвертации
виртуальных файлов.  
[FileTypeID](P_Tessa_FileConverters_IFileConverterRequest_FileTypeID.htm)|
Идентификатор типа преобразуемого файла, который указывается в запросе на
конвертацию CardGetFileContentRequest.FileTypeID, или null, если свойство не
указывается в запросе. От значения этого свойства зависит вычисление хеша
запроса (и идентификация похожих операций). Значение необязательно для
заполнения, его можно использовать для конвертации виртуальных файлов.  
[FileTypeName](P_Tessa_FileConverters_IFileConverterRequest_FileTypeName.htm)|
Имя типа преобразуемого файла, который указывается в запросе на конвертацию
CardGetFileContentRequest.FileTypeName, или null, если свойство не указывается
в запросе. От значения этого свойства зависит вычисление хеша запроса (и
идентификация похожих операций). Значение необязательно для заполнения, его
можно использовать для конвертации виртуальных файлов.  
[Flags](P_Tessa_FileConverters_IFileConverterRequest_Flags.htm)| Флаги с
настройками конвертации файлов.  
[Info](P_Tessa_FileConverters_IFileConverterRequest_Info.htm)|  Дополнительная
информация, передаваемая в параметры конвертации. От такой информации не
зависит вычисление хеша запроса (и идентификация похожих операций), в отличие
от данных в свойстве [Tessa.FileConverters.IFileConverterRequest.Parameters].  
[InputFormat](P_Tessa_FileConverters_IFileConverterRequest_InputFormat.htm)|
Формат преобразуемого файла. Устанавливайте значение этого свойства после
установки [Tessa.FileConverters.IFileConverterRequest.FileName].  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[OutputFormat](P_Tessa_FileConverters_IFileConverterRequest_OutputFormat.htm)|
Выходной формат файла. Значение используется для вычисления хеша запроса.  
[Parameters](P_Tessa_FileConverters_IFileConverterRequest_Parameters.htm)|
Дополнительная информация, передаваемая в параметры конвертации, которая
влияет на вычисление хеша запроса. Файлы, сгенерированные с разными
параметрами, могут конвертироваться параллельно и могут сохраняться в кэш
одновременно. Если параметры идентичны (а также свойства VersionID, EventName
и OutputFormat), то система считает запросы идентичными, выполнит конвертацию
ровно один раз и вернёт результат из кэша.  
[VersionID](P_Tessa_FileConverters_IFileConverterRequest_VersionID.htm)|
Идентификатор версии преобразуемого файла. Значение используется для
вычисления хеша запроса.  
##  __Методы
[CalculateHash](M_Tessa_FileConverters_IFileConverterRequest_CalculateHash.htm)|
Вычисляет хеш операции по конвертации для данного запроса, по которому, в том
числе, выполняется сравнение операций и их результатов в кэше. По умолчанию
учитываются значения свойств VersionID, EventName, OutputFormat и Parameters.  
---|---  
[Deserialize](M_Tessa_FileConverters_IFileConverterRequest_Deserialize.htm)|
Десериализует информацию из заданного хранилища в свойства текущего объекта.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Serialize](M_Tessa_FileConverters_IFileConverterRequest_Serialize.htm)|
Сериализует информацию в заданном хранилище для передачи в запускаемую
операцию.  
##  __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
