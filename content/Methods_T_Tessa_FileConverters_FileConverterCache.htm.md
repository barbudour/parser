# FileConverterCache - методы
##  __Методы
[CleanCacheAsync](M_Tessa_FileConverters_FileConverterCache_CleanCacheAsync.htm)|
Очищает кэш от преобразованных файлов, доступ к содержимому которых выполнялся
раньше заданной даты, и возвращает результат операции по очистке кэша.
Возвращённое значение не равно null. В случае ошибок очистки исключение не
выбрасывается.  
---|---  
[DeleteFileAsync](M_Tessa_FileConverters_FileConverterCache_DeleteFileAsync.htm)|
Удаляет сконвертированный файл из кэша файлов, если он там присутствует.
Возвращает результат удаления с сообщениями об ошибках и предупреждениями, а
также признак того, был ли файл в кэше на момент вызова метода. Используйте
метод в таких сценариях, как конвертация, инициируемая с веб-сервиса, но
фактически выполняемая в плагине Chronos, где кэш файлов требуется как способ
передачи содержимого файла после конвертации. Если известно, что операция по
конвертации уникальна и результат конвертации не будет нужен, то посредством
этого метода можно удалить содержимое файла из кэша файлов.  
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
[GetFileAsync](M_Tessa_FileConverters_FileConverterCache_GetFileAsync.htm)|
Возвращает объект со значениями: 1) результат обращения к кэшу, может
содержать сообщения об ошибках; 2) асинхронную функцию, которая создаёт поток
к содержимому преобразованного файла, который расположен в кэше (функция может
быть равна null, если возникли ошибки при доступе к кэшу); 3) размер
возвращаемого содержимого в байтах или -1, если содержимое отсутствует или
размер неизвестен.  
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
[StoreFileAsync](M_Tessa_FileConverters_FileConverterCache_StoreFileAsync.htm)|
Сохраняет преобразованный файл в кэше и возвращает результат операции по
сохранению. Возвращаемое значение не равно null.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetConvertedFileIDAsync](M_Tessa_FileConverters_FileConverterCache_TryGetConvertedFileIDAsync.htm)|
Возвращает идентификатор преобразованного файла в кэше по идентификатору
версии исходного файла и по хешу от запроса или null, если файл ещё не был
преобразован или операция неизвестна.  
[TryGetResponseInfoAsync](M_Tessa_FileConverters_FileConverterCache_TryGetResponseInfoAsync.htm)|
Возвращает информацию Info из ответа на запрос по выполнению конвертации,
которая была сохранена в кэше, или null, если либо в кэше нет файла с заданным
идентификатором, либо при конвертации не была указана информация.  
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
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
