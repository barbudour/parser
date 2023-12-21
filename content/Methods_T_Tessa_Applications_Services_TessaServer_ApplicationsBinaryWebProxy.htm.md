# ApplicationsBinaryWebProxy - методы
##  __Методы
[AddSessionToken](M_Tessa_Platform_Runtime_WebProxy_AddSessionToken.htm)|
Добавляет токен с текущей сессией к заголовкам сообщения, отправляемого на
сервер, если объект
[SessionTokenHolder](P_Tessa_Platform_Runtime_WebProxy_SessionTokenHolder.htm)
задан и содержит действительный токен сессии.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
---|---  
[CheckSealed](M_Tessa_Platform_Runtime_WebProxy_CheckSealed.htm)|  Выбрасывает
исключение [Tessa.Platform.ObjectSealedException], если объект был защищён от
изменений.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[Dispose](M_Tessa_Platform_Runtime_WebProxy_Dispose.htm)| Освобождает ресурсы,
занимаемые объектом.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[DisposeAsync()](M_Tessa_Platform_Runtime_WebProxy_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_Runtime_WebProxy_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[DownloadAsync](M_Tessa_Applications_Services_TessaServer_ApplicationsBinaryWebProxy_DownloadAsync.htm)|
Операция скачивания приложения.  
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
[GetRequestUri](M_Tessa_Platform_Runtime_WebProxy_GetRequestUri.htm)|
Возвращает полный путь
[Uri](https://learn.microsoft.com/dotnet/api/system.uri) к заданному методу
для выполнения запроса к контроллеру.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Has](M_Tessa_Platform_Runtime_WebProxy_Has.htm)| Возвращает признак того, что
заданный флаг установлен.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[HasAny](M_Tessa_Platform_Runtime_WebProxy_HasAny.htm)| Возвращает признак
того, что один из заданных флагов установлен.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[HasNot](M_Tessa_Platform_Runtime_WebProxy_HasNot.htm)| Возвращает признак
того, что заданный флаг не установлен.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnDisposedAsync](M_Tessa_Platform_Runtime_WebProxy_OnDisposedAsync.htm)|
Действие, выполняемое при освобождении ресурсов, занимаемых объектом, в методе
[DisposeAsync(Boolean)](M_Tessa_Platform_Runtime_WebProxy_DisposeAsync_1.htm).
В реализации по умолчанию вызывает событие
[Disposed](E_Tessa_Platform_Runtime_WebProxy_Disposed.htm).  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[Seal](M_Tessa_Platform_Runtime_WebProxy_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[SendAsync<TResponse>](M_Tessa_Platform_Runtime_WebProxy_SendAsync__1.htm)|
Выполняет запрос заданного типа к веб-сервису с сериализуемыми параметрами и
возвращает результат.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[ThrowOnErrorAsync](M_Tessa_Platform_Runtime_WebProxy_ThrowOnErrorAsync.htm)|
Проверяет ответ от сервера на наличие ошибок. Если статусный код отличен от
успешного, то выбрасывается исключение. Метод умеет обрабатывать значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm),
полученное от сервера и содержащее серверный стек-трейс, в этом случае
выбрасывается
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm).  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetFaultedResultAsync](M_Tessa_Applications_Services_TessaServer_ApplicationsBinaryWebProxy_TryGetFaultedResultAsync.htm)|
Возвращает ошибки при скачивании приложения как объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) или null,
если информация недоступна: ошибок не было или пользователь не имеет доступа к
этой записи в истории.  
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
[ApplicationsBinaryWebProxy -
](T_Tessa_Applications_Services_TessaServer_ApplicationsBinaryWebProxy.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
