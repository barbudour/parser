# FmNotificationProvider - класс
Объект, обрабатывающий всплывающие уведомления по обсуждениям для индикатора
сообщений.
## __Definition
 **Пространство имён:**
[Tessa.Forums.Notifications](N_Tessa_Forums_Notifications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FmNotificationProvider : IFmNotificationProvider
VB __Копировать
     Public NotInheritable Class FmNotificationProvider
    	Implements IFmNotificationProvider
C++ __Копировать
     public ref class FmNotificationProvider sealed : IFmNotificationProvider
F# __Копировать
     [<SealedAttribute>]
    type FmNotificationProvider = 
        class
            interface IFmNotificationProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FmNotificationProvider
Implements
    [IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm)
##  __Конструкторы
[FmNotificationProvider](M_Tessa_Forums_Notifications_FmNotificationProvider__ctor.htm)|
Инициализирует новый экземпляр класса FmNotificationProvider  
---|---  
##  __Методы
[AddReadMessageAsync](M_Tessa_Forums_Notifications_FmNotificationProvider_AddReadMessageAsync.htm)|
Отмечает сообщение как прочитанное.  
---|---  
[ClearNotificationsAsync](M_Tessa_Forums_Notifications_FmNotificationProvider_ClearNotificationsAsync.htm)|
Очищает ленту уведомлений.  
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
[GetNotificationsAsync](M_Tessa_Forums_Notifications_FmNotificationProvider_GetNotificationsAsync.htm)|
Получает уведомления для индикатора сообщений.  
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
[RemoveReadMessageAsync](M_Tessa_Forums_Notifications_FmNotificationProvider_RemoveReadMessageAsync.htm)|
Отмечает сообщение как непрочитанное.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateNotificationsAsync](M_Tessa_Forums_Notifications_FmNotificationProvider_UpdateNotificationsAsync.htm)|
Добавляет сообщение в ленту уведомлений для текущего пользователя. Функция
умеет переключать активный батч. При необходимости создаются уведомления.  
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
[Tessa.Forums.Notifications - пространство
имён](N_Tessa_Forums_Notifications.htm)
