# NotificationEmailSource - класс
Реализация
[INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm),
которая возвращает шаблон уведомления по идентификатору карточки уведомления.
Базовая версия обрабатывает параметр с типом
[IDNotificationEmailSourceParameter](T_Tessa_Notices_Parameters_IDNotificationEmailSourceParameter.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices.Sources](N_Tessa_Notices_Sources.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NotificationEmailSource : INotificationEmailSource
VB __Копировать
     Public Class NotificationEmailSource
    	Implements INotificationEmailSource
C++ __Копировать
     public ref class NotificationEmailSource : INotificationEmailSource
F# __Копировать
     type NotificationEmailSource = 
        class
            interface INotificationEmailSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationEmailSource
Derived
[Tessa.Notices.Sources.AliasNotificationEmailSource](T_Tessa_Notices_Sources_AliasNotificationEmailSource.htm)
Implements
    [INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm)
##  __Конструкторы
[NotificationEmailSource](M_Tessa_Notices_Sources_NotificationEmailSource__ctor.htm)|
Инициализирует новый экземпляр класса NotificationEmailSource  
---|---  
##  __Свойства
[DbScope](P_Tessa_Notices_Sources_NotificationEmailSource_DbScope.htm)|
Объект для взаимодействия с базой данных.  
---|---  
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
[GetEmailAsync](M_Tessa_Notices_Sources_NotificationEmailSource_GetEmailAsync.htm)|
Возвращает шаблон уведомления, по которому будет формироваться email для
пользователя.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNotificationIDAsync](M_Tessa_Notices_Sources_NotificationEmailSource_GetNotificationIDAsync.htm)|
Метод для получения идентификатора карточки уведомления из параметров.  
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
[Tessa.Notices.Sources - пространство имён](N_Tessa_Notices_Sources.htm)
