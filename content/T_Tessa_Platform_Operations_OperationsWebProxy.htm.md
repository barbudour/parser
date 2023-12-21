# OperationsWebProxy - класс
Прокси для обращения к веб-сервису операций. Методы аналогичны
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class OperationsWebProxy : WebProxy
VB __Копировать
     Public NotInheritable Class OperationsWebProxy
    	Inherits WebProxy
C++ __Копировать
     public ref class OperationsWebProxy sealed : public WebProxy
F# __Копировать
     [<SealedAttribute>]
    type OperationsWebProxy = 
        class
            inherit WebProxy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm) __ OperationsWebProxy
##  __Конструкторы
[OperationsWebProxy](M_Tessa_Platform_Operations_OperationsWebProxy__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[BaseUri](P_Tessa_Platform_Runtime_WebProxy_BaseUri.htm)|  Базовый адрес папки
веб-сервисов системы. Например: https://localhost/tessa. Должен быть
установлен перед вызовом метода у прокси-объекта.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
---|---  
[ControllerRoute](P_Tessa_Platform_Runtime_WebProxy_ControllerRoute.htm)|
Путь до контроллера на серверной стороне. Например: api/Cards.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[HttpClient](P_Tessa_Platform_Runtime_WebProxy_HttpClient.htm)|  Объект,
обеспечивающий соединение с веб-сервисом по протоколам HTTP/HTTPS. Должен быть
установлен перед вызовом метода у прокси-объекта.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[InstanceName](P_Tessa_Platform_Runtime_WebProxy_InstanceName.htm)|  Имя
экземпляра сервера, с которым выполняется соединение. Например: default. Если
установлены null или пустая строка, то используется имя экземпляра по
умолчанию. Должен быть установлен перед вызовом метода у прокси-объекта.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[IsDisposed](P_Tessa_Platform_Runtime_WebProxy_IsDisposed.htm)| Признак того,
что ресурсы объекта были освобождены.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[IsSealed](P_Tessa_Platform_Runtime_WebProxy_IsSealed.htm)| Признак того, что
объект был защищён от изменений.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[ServiceName](P_Tessa_Platform_Runtime_WebProxy_ServiceName.htm)|  Имя веб-
сервиса ASP.NET Core. Например: web.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[SessionTokenHolder](P_Tessa_Platform_Runtime_WebProxy_SessionTokenHolder.htm)|
Объект, содержащий токен, связанный с текущей сессией, или null, если связь с
сессией не поддерживается.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[SessionVersionHolder](P_Tessa_Platform_Runtime_WebProxy_SessionVersionHolder.htm)|
Объект, содержащий версию платформы, связанную с текущей сессией, или null,
если связь с сессией не поддерживается.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[StreamingBufferSize](P_Tessa_Platform_Runtime_WebProxy_StreamingBufferSize.htm)|
Размер буфера в байтах, который используется для потоковой передачи. Обычно
равен 1 Мб из константы
[DefaultStreamingBufferSize](P_Tessa_Platform_Runtime_TessaHttpContent_DefaultStreamingBufferSize.htm).  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
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
[CompleteAsync](M_Tessa_Platform_Operations_OperationsWebProxy_CompleteAsync.htm)|
Завершает операцию заданного типа, т.е. переводит её в состояние
[Tessa.Platform.Operations.OperationState.Completed].  
[CreateAsync](M_Tessa_Platform_Operations_OperationsWebProxy_CreateAsync.htm)|
Создаёт операцию с заданными параметрами.  
[DeleteAsync](M_Tessa_Platform_Operations_OperationsWebProxy_DeleteAsync.htm)|
Удаляет операцию с заданным идентификатором. Если операция не существовала, то
не выдаётся сообщений об ошибках.  
[DeleteOlderThanAsync](M_Tessa_Platform_Operations_OperationsWebProxy_DeleteOlderThanAsync.htm)|
Выполняет удаление записей, которые были созданы раньше заданных даты и
времени.  
[Dispose](M_Tessa_Platform_Runtime_WebProxy_Dispose.htm)| Освобождает ресурсы,
занимаемые объектом.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[DisposeAsync()](M_Tessa_Platform_Runtime_WebProxy_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_Runtime_WebProxy_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
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
[GetAllAsync](M_Tessa_Platform_Operations_OperationsWebProxy_GetAllAsync.htm)|
Возвращает информацию по всем операциям. При запросе с клиента метод доступен
только администраторам.  
[GetAllByTypeAsync](M_Tessa_Platform_Operations_OperationsWebProxy_GetAllByTypeAsync.htm)|
Возвращает информацию по всем операциям заданного типа. При запросе с клиента
метод доступен только администраторам.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetRequestUri](M_Tessa_Platform_Runtime_WebProxy_GetRequestUri.htm)|
Возвращает полный путь
[Uri](https://learn.microsoft.com/dotnet/api/system.uri) к заданному методу
для выполнения запроса к контроллеру.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[GetStateAndProgressAsync](M_Tessa_Platform_Operations_OperationsWebProxy_GetStateAndProgressAsync.htm)|
Возвращает состояние и прогресс операции в процентах или null, если операция
не найдена.  
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
[IsAliveAsync](M_Tessa_Platform_Operations_OperationsWebProxy_IsAliveAsync.htm)|
Возвращает признак того, что операция с заданным идентификатором существует.  
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
[ReportProgressAsync](M_Tessa_Platform_Operations_OperationsWebProxy_ReportProgressAsync.htm)|
Сообщает о проценте готовности заданной операции, если операция находится в
состоянии [Tessa.Platform.Operations.OperationState.InProgress]? и возвращает
признак того, что изменение процента готовности удалось.  
[Seal](M_Tessa_Platform_Runtime_WebProxy_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[SendAsync<TResponse>](M_Tessa_Platform_Runtime_WebProxy_SendAsync__1.htm)|
Выполняет запрос заданного типа к веб-сервису с сериализуемыми параметрами и
возвращает результат.  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
[StartAsync](M_Tessa_Platform_Operations_OperationsWebProxy_StartAsync.htm)|
Запускает операцию с заданным идентификатором. Операция должна быть создана и
находиться в состоянии [Tessa.Platform.Operations.OperationState.Created].  
[StartFirstAsync](M_Tessa_Platform_Operations_OperationsWebProxy_StartFirstAsync.htm)|
Запускает из созданных операций заданного типа и возвращает идентификатор
запущенной операции или null, если подходящая операция отсутствует.  
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
[TryGetAsync](M_Tessa_Platform_Operations_OperationsWebProxy_TryGetAsync.htm)|
Возвращает информацию по операции с заданным идентификатором или null, если
операция отсутствует.  
[TryGetOperationIDByRequestHashAsync](M_Tessa_Platform_Operations_OperationsWebProxy_TryGetOperationIDByRequestHashAsync.htm)|
Возвращает идентификатор первой попавшейся операции по заданным идентификатору
типа и хешу от запроса или null, если операция не найдена.  
## __События
[Disposed](E_Tessa_Platform_Runtime_WebProxy_Disposed.htm)|  Событие,
выполняемое при освобождении ресурсов, занимаемых объектом, в методе
[System.IDisposable.Dispose].  
(Унаследован от [WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm))  
---|---  
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
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
