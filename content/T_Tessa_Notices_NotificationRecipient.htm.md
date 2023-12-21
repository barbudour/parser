# NotificationRecipient - класс
Получатель уведомления по электронной почте.
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NotificationRecipient
VB __Копировать
     Public NotInheritable Class NotificationRecipient
C++ __Копировать
     public ref class NotificationRecipient sealed
F# __Копировать
     [<SealedAttribute>]
    type NotificationRecipient = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationRecipient
##  __Конструкторы
[NotificationRecipient](M_Tessa_Notices_NotificationRecipient__ctor.htm)|
Инициализирует новый экземпляр класса NotificationRecipient  
---|---  
##  __Свойства
[Email](P_Tessa_Notices_NotificationRecipient_Email.htm)|  Email получателя.  
---|---  
[HasMobileApproval](P_Tessa_Notices_NotificationRecipient_HasMobileApproval.htm)|
Флаг определяет, использует ли получатель уведомления мобильное согласование.  
[IsOptional](P_Tessa_Notices_NotificationRecipient_IsOptional.htm)|  Флаг
определяет, является ли получатель уведомления необязательным. Необязательный
получатель получает уведомление только в ситуации, когда в правилах получения
явно указано, что сотрудник должен получить уведомление.  
[LanguageCode](P_Tessa_Notices_NotificationRecipient_LanguageCode.htm)|  Код
языка, используемый для формирования текста уведомления.  
[NotificationSettings](P_Tessa_Notices_NotificationRecipient_NotificationSettings.htm)|
Правила получаения и фильтрации уведомлений.  
[TimeZoneUtcOffsetMinutes](P_Tessa_Notices_NotificationRecipient_TimeZoneUtcOffsetMinutes.htm)|
Временная зона получателя уведомления.  
[UserID](P_Tessa_Notices_NotificationRecipient_UserID.htm)|  Идентификатор
сотрудника получателя.  
[UserName](P_Tessa_Notices_NotificationRecipient_UserName.htm)|  Имя
сотрудника получателя.  
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
[Tessa.Notices - пространство имён](N_Tessa_Notices.htm)
