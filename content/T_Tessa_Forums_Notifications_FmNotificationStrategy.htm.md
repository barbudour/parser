# FmNotificationStrategy - класс
Объект, обрабатывающий всплывающие уведомления по обсуждениям для индикатора
сообщений со стороны сервера.
## __Definition
 **Пространство имён:**
[Tessa.Forums.Notifications](N_Tessa_Forums_Notifications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FmNotificationStrategy : IFmNotificationStrategy, 
    	IFmNotificationProvider
VB __Копировать
     Public NotInheritable Class FmNotificationStrategy
    	Implements IFmNotificationStrategy, IFmNotificationProvider
C++ __Копировать
     public ref class FmNotificationStrategy sealed : IFmNotificationStrategy, 
    	IFmNotificationProvider
F# __Копировать
     [<SealedAttribute>]
    type FmNotificationStrategy = 
        class
            interface IFmNotificationStrategy
            interface IFmNotificationProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FmNotificationStrategy
Implements
    [IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm), [IFmNotificationStrategy](T_Tessa_Forums_Notifications_IFmNotificationStrategy.htm)
##  __Конструкторы
[FmNotificationStrategy](M_Tessa_Forums_Notifications_FmNotificationStrategy__ctor.htm)|
Инициализирует новый экземпляр класса FmNotificationStrategy  
---|---  
##  __Методы
[AddReadMessageAsync](M_Tessa_Forums_Notifications_FmNotificationStrategy_AddReadMessageAsync.htm)|
Отмечает сообщение как прочитанное.  
---|---  
[AddServiceMessageInNotificationsAsync](M_Tessa_Forums_Notifications_FmNotificationStrategy_AddServiceMessageInNotificationsAsync.htm)|
Добавляет служебное сообщение в ленту уведомлений. Само служебное сообщение
содержит в себе список пользователей, которым отправляются эти уведомления.  
[ClearNotificationsAsync](M_Tessa_Forums_Notifications_FmNotificationStrategy_ClearNotificationsAsync.htm)|
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
[GetNotificationsAsync(Nullable<DateTime>,
CancellationToken)](M_Tessa_Forums_Notifications_FmNotificationStrategy_GetNotificationsAsync.htm)|
Получает уведомления для индикатора сообщений.  
[GetNotificationsAsync(IForumData, DateTime,
CancellationToken)](M_Tessa_Forums_Notifications_FmNotificationStrategy_GetNotificationsAsync_1.htm)|
Получает уведомления для индикатора сообщений.  
[GetReadTopicStatusListFromNotificationAsync](M_Tessa_Forums_Notifications_FmNotificationStrategy_GetReadTopicStatusListFromNotificationAsync.htm)|
Возвращает информацию по прочитанным сообщениям в топиках.  
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
[RemoveReadMessageAsync](M_Tessa_Forums_Notifications_FmNotificationStrategy_RemoveReadMessageAsync.htm)|
Отмечает сообщение как непрочитанное.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateNotificationsAsync](M_Tessa_Forums_Notifications_FmNotificationStrategy_UpdateNotificationsAsync.htm)|
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
