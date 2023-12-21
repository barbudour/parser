# CardTypedRequestExtension<TRequest, TResponse> \- класс
Базовый класс расширений для процесса универсального взаимодействия с сервисом
карточек через строготипизированные объекты запроса TRequest и ответа на
запрос TResponse.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardTypedRequestExtension<TRequest, TResponse> : CardRequestExtension
    where TRequest : class, IStorageObjectProvider
    where TResponse : class, IStorageObjectProvider
VB __Копировать
     Public MustInherit Class CardTypedRequestExtension(Of TRequest As {Class, IStorageObjectProvider}, TResponse As {Class, IStorageObjectProvider})
    	Inherits CardRequestExtension
C++ __Копировать
    generic<typename TRequest, typename TResponse>
    where TRequest : ref class, IStorageObjectProvider
    where TResponse : ref class, IStorageObjectProvider
    public ref class CardTypedRequestExtension abstract : public CardRequestExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardTypedRequestExtension<'TRequest, 'TResponse when 'TRequest : not struct and IStorageObjectProvider when 'TResponse : not struct and IStorageObjectProvider> = 
        class
            inherit CardRequestExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm) __ CardTypedRequestExtension<TRequest, TResponse>
Derived
[Tessa.Cards.Numbers.NumberControlRequestExtension](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
#### Параметры типа
TRequest
     Строготипизированный запрос. Должен реализовывать интерфейс [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm). 
TResponse
     Строготипизированный ответ на запрос. Должен реализовывать интерфейс [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm). 
## __Конструкторы
[CardTypedRequestExtension<TRequest,
TResponse>](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2__ctor.htm)|
Инициализирует новый экземпляр класса CardTypedRequestExtension<TRequest,
TResponse>  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2_AfterRequest.htm)|
Действие, выполняемое после универсального взаимодействия с сервисом карточек
как при успешном, так и при неудачном результате.  
(Переопределяет
[CardRequestExtension.AfterRequest(ICardRequestExtensionContext)](M_Tessa_Cards_Extensions_CardRequestExtension_AfterRequest.htm))  
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
[CreateRequestAsync](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2_CreateRequestAsync.htm)|
Создаёт строготипизированный объект запроса для заданного хранилища или null,
если создание невозможно.  
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
[ProcessRequestAsync](M_Tessa_Cards_Extensions_CardTypedRequestExtension_2_ProcessRequestAsync.htm)|
Выполняет обработку заданного запроса и возвращает ответ на запрос. Метод
может вернуть null, если устанавливать ответ на запрос не требуется.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
