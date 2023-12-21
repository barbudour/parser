# NotificationSendContext - класс
Контекст отправки уведомления через
[INotificationManager](T_Tessa_Notices_INotificationManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NotificationSendContext : INotificationSendContext
VB __Копировать
     Public NotInheritable Class NotificationSendContext
    	Implements INotificationSendContext
C++ __Копировать
     public ref class NotificationSendContext sealed : INotificationSendContext
F# __Копировать
     [<SealedAttribute>]
    type NotificationSendContext = 
        class
            interface INotificationSendContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationSendContext
Implements
    [INotificationSendContext](T_Tessa_Notices_INotificationSendContext.htm)
##  __Конструкторы
[NotificationSendContext](M_Tessa_Notices_NotificationSendContext__ctor.htm)|
Инициализирует новый экземпляр класса NotificationSendContext  
---|---  
##  __Свойства
[DisableSubscribers](P_Tessa_Notices_NotificationSendContext_DisableSubscribers.htm)|
Флаг определяет, нужно ли исключить из списка получателей подписчиков на
данный тип уведомления для данной карточки.  
---|---  
[ExcludeDeputies](P_Tessa_Notices_NotificationSendContext_ExcludeDeputies.htm)|
Флаг определяет, нужно ли исключить из списка сотрудников заместителей.  
[GetCardFuncAsync](P_Tessa_Notices_NotificationSendContext_GetCardFuncAsync.htm)|
Функция для получения объекта карточки из кеша. Может иметь значение null.  
[IgnoreUserSessions](P_Tessa_Notices_NotificationSendContext_IgnoreUserSessions.htm)|
Флаг определяет, нужно ли игнорировать сессии пользователей при формировании
текста писем. Игнорирование сессии ускоряет скорость отправки писем, однако в
данном режиме не работают плейсхолдеры, которые опираются на сессию
получателя.  
[Info](P_Tessa_Notices_NotificationSendContext_Info.htm)|  Дополнительная
информация, которая передается в info методов замены плейсхолдеров.  
[MainCardID](P_Tessa_Notices_NotificationSendContext_MainCardID.htm)|
Идентификатор основной карточки.  
[ModifyEmailActionAsync](P_Tessa_Notices_NotificationSendContext_ModifyEmailActionAsync.htm)|
Действие модификации шаблона сообщения.  
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
