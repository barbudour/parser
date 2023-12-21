# CustomNotification - класс
Уведомление, не привязанное к заданию.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
    [NotificationAttribute("custom")]
    public sealed class CustomNotification : INotification
VB __Копировать
    <NotificationAttribute("custom")>
    Public NotInheritable Class CustomNotification
    	Implements INotification
C++ __Копировать
    [NotificationAttribute(L"custom")]
    public ref class CustomNotification sealed : INotification
F# __Копировать
     [<SealedAttribute>]
    [<NotificationAttribute("custom")>]
    type CustomNotification = 
        class
            interface INotification
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CustomNotification
Implements
    [INotification](T_Tessa_Extensions_Default_Shared_Notices_INotification.htm)
##  __Конструкторы
[CustomNotification(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Notices_CustomNotification__ctor.htm)|
Инициализирует новый экземпляр класса CustomNotification  
---|---  
[CustomNotification(String, String,
String)](M_Tessa_Extensions_Default_Shared_Notices_CustomNotification__ctor_1.htm)|
Инициализирует новый экземпляр класса CustomNotification  
##  __Свойства
[Body](P_Tessa_Extensions_Default_Shared_Notices_CustomNotification_Body.htm)|  
---|---  
[Email](P_Tessa_Extensions_Default_Shared_Notices_CustomNotification_Email.htm)|  
[Subject](P_Tessa_Extensions_Default_Shared_Notices_CustomNotification_Subject.htm)|  
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
[SerializeTo](M_Tessa_Extensions_Default_Shared_Notices_CustomNotification_SerializeTo.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[Key](F_Tessa_Extensions_Default_Shared_Notices_CustomNotification_Key.htm)|
Ключ, по которому должен быть зарегистрирован обработчик
[INotificationSender](T_Tessa_Extensions_Default_Shared_Notices_INotificationSender.htm).
Ключ также используется для указания секции при сериализации уведомлений. Ключ
должен быть уникальным для каждого типа уведомлений.  
---|---  
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
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
