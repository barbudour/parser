# AliasNotificationEmailSource - класс
Реализация
[INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm),
которая возвращает шаблон уведомления по алиасу карточки уведомления.
Обрабатывает параметр с типом
[AliasNotificationEmailSourceParameter](T_Tessa_Notices_Parameters_AliasNotificationEmailSourceParameter.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices.Sources](N_Tessa_Notices_Sources.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AliasNotificationEmailSource : NotificationEmailSource
VB __Копировать
     Public Class AliasNotificationEmailSource
    	Inherits NotificationEmailSource
C++ __Копировать
     public ref class AliasNotificationEmailSource : public NotificationEmailSource
F# __Копировать
     type AliasNotificationEmailSource = 
        class
            inherit NotificationEmailSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationEmailSource](T_Tessa_Notices_Sources_NotificationEmailSource.htm) __ AliasNotificationEmailSource
##  __Конструкторы
[AliasNotificationEmailSource](M_Tessa_Notices_Sources_AliasNotificationEmailSource__ctor.htm)|
Инициализирует новый экземпляр класса AliasNotificationEmailSource  
---|---  
##  __Свойства
[DbScope](P_Tessa_Notices_Sources_NotificationEmailSource_DbScope.htm)|
Объект для взаимодействия с базой данных.  
(Унаследован от
[NotificationEmailSource](T_Tessa_Notices_Sources_NotificationEmailSource.htm))  
---|---  
##  __Методы
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
(Унаследован от
[NotificationEmailSource](T_Tessa_Notices_Sources_NotificationEmailSource.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNotificationIDAsync](M_Tessa_Notices_Sources_AliasNotificationEmailSource_GetNotificationIDAsync.htm)|
Метод для получения идентификатора карточки уведомления из параметров.  
(Переопределяет
[NotificationEmailSource.GetNotificationIDAsync(INotificationEmailSourceParameter,
INotificationSendContext,
CancellationToken)](M_Tessa_Notices_Sources_NotificationEmailSource_GetNotificationIDAsync.htm))  
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
