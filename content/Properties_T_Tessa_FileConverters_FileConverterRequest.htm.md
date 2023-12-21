# FileConverterRequest - свойства
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
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
