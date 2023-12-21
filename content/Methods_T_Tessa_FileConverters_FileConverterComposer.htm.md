# FileConverterComposer - методы
##  __Методы
[BeginConversionAsync](M_Tessa_FileConverters_FileConverterComposer_BeginConversionAsync.htm)|
Запускает процесс конвертации файла карточки в заданный формат и возвращает
идентификатор операции, по которой можно контролировать ход конвертации.
Вторым полем возвращает новое значение параметра requestHash. Файл после
конвертации обычно помещается в кэш, но этот метод всегда создаёт новую
операцию по конвертации, даже если конвертация этой версии файла уже была
выполнена и содержится в кэше.  
---|---  
[CalculateHash](M_Tessa_FileConverters_FileConverterComposer_CalculateHash.htm)|
Вычисляет хеш запроса, который может использоваться при обращении к кэшу.  
[DeleteFileAsync](M_Tessa_FileConverters_FileConverterComposer_DeleteFileAsync.htm)|
Удаляет сконвертированный файл из кэша файлов, если он там присутствует.
Возвращает результат удаления с сообщениями об ошибках и предупреждениями, а
также признак того, был ли файл в кэше на момент вызова метода. Используйте
метод в таких сценариях, как конвертация, инициируемая с веб-сервиса, но
фактически выполняемая в плагине Chronos, где кэш файлов требуется как способ
передачи содержимого файла после конвертации. Если известно, что операция по
конвертации уникальна и результат конвертации не будет нужен, то посредством
этого метода можно удалить содержимое файла из кэша файлов.  
[EndConversionAsync](M_Tessa_FileConverters_FileConverterComposer_EndConversionAsync.htm)|
Возвращает результат конвертации, который предоставляет доступ к содержимому
файла, для которого была выполнена конвертация. После выполнения функции
операция удаляется, поэтому повторный вызов метода возвращает ошибку.
Результат всегда не равен null, ошибки и исключения будут сохранены в объекте
результата.  
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
[InProgressAsync](M_Tessa_FileConverters_FileConverterComposer_InProgressAsync.htm)|
Возвращает признак того, что операция по конвертации запущена и ещё
выполняется. Возвращает false, если операция завершилась или она была удалена
(например, администратором).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryConvertFromCacheAsync](M_Tessa_FileConverters_FileConverterComposer_TryConvertFromCacheAsync.htm)|
Возвращает результат конвертации, который предоставляет доступ к потоку файла,
для которого была выполнена конвертация, но только если выходной файл
присутствует в кэше на момент вызова, т.е. конвертация выполнялась ранее. В
противном случае возвращает null, т.е. для получения файла потребуется
выполнить конвертацию. Вторым полем возвращает новое значение параметра
requestHash.  
[TryConvertFromCacheOrBeginConversionAsync](M_Tessa_FileConverters_FileConverterComposer_TryConvertFromCacheOrBeginConversionAsync.htm)|
Возвращает результат конвертации, если объект доступен через кэш, или null,
если объект недоступен, и был запущен асинхронный процесс конвертации файла
карточки в заданный формат, и возвращает идентификатор операции, по которой
можно контролировать ход конвертации. Файл после конвертации обычно помещается
в кэш. Вторым полем возвращает идентификатор операции, по которой можно
контролировать ход конвертации. Он актуален только в том случае, если метод
первым полем вернул null, т.е. не удалось получить значение из кэша.  
## __Методы расширения
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
[FileConverterComposer - ](T_Tessa_FileConverters_FileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
