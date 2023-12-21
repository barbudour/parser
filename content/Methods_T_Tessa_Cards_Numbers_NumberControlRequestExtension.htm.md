# NumberControlRequestExtension - методы
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2_AfterRequest.htm)|
Действие, выполняемое после универсального взаимодействия с сервисом карточек
как при успешном, так и при неудачном результате.  
(Унаследован от [CardTypedRequestExtension<TRequest,
TResponse>](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRequestExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после универсального
взаимодействия с сервисом карточек как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
(Унаследован от
[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardRequestExtension_BeforeRequest.htm)|
Действие, выполняемое перед универсальным взаимодействием с сервисом карточек
стандартными средствами. Может установить ответ на запрос для того, чтобы
взаимодействие с сервисом карточек стандартными средствами не выполнялось.  
(Унаследован от
[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm))  
[CreateRequestAsync](M_Tessa_Cards_Numbers_NumberControlRequestExtension_CreateRequestAsync.htm)|
Создаёт строготипизированный объект запроса для заданного хранилища или null,
если создание невозможно.  
(Переопределяет [CardTypedRequestExtension<TRequest,
TResponse>.CreateRequestAsync(Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2_CreateRequestAsync.htm))  
[CreateResponseAsync](M_Tessa_Cards_Numbers_NumberControlRequestExtension_CreateResponseAsync.htm)|
Создаёт объект ответа на запрос для успешно выполненного действия с номером.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteNumberActionAsync](M_Tessa_Cards_Numbers_NumberControlRequestExtension_ExecuteNumberActionAsync.htm)|
Выполняет действие с номером для заданного контекста. Возвращает признак того,
что действие успешно выполнено.  
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
[ProcessRequestAsync](M_Tessa_Cards_Numbers_NumberControlRequestExtension_ProcessRequestAsync.htm)|
Выполняет обработку заданного запроса и возвращает ответ на запрос. Метод
может вернуть null, если устанавливать ответ на запрос не требуется.  
(Переопределяет [CardTypedRequestExtension<TRequest,
TResponse>.ProcessRequestAsync(ICardRequestExtensionContext,
TRequest)](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2_ProcessRequestAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryLoadOrCreateCardAsync](M_Tessa_Cards_Numbers_NumberControlRequestExtension_TryLoadOrCreateCardAsync.htm)|
Загружает или создаёт карточку по заданному идентификатору и возвращает
карточку или null, если карточка не была создана или загружена. Создание
выполняется в случае, если в запросе request указано, что карточка ещё ни разу
не была сохранена.  
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
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
