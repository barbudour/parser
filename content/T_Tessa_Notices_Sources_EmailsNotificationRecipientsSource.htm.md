# EmailsNotificationRecipientsSource - класс
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая получает список получателей как список явно заданных email-ов с
указанием идентификатора пользователя, настройки которого исопльзуются для
формирования письма. Обрабатывает тип параметров
[EmailsNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_EmailsNotificationRecipientsSourceParameter.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices.Sources](N_Tessa_Notices_Sources.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class EmailsNotificationRecipientsSource : INotificationRecipientsSource
VB __Копировать
     Public NotInheritable Class EmailsNotificationRecipientsSource
    	Implements INotificationRecipientsSource
C++ __Копировать
     public ref class EmailsNotificationRecipientsSource sealed : INotificationRecipientsSource
F# __Копировать
     [<SealedAttribute>]
    type EmailsNotificationRecipientsSource = 
        class
            interface INotificationRecipientsSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ EmailsNotificationRecipientsSource
Implements
    [INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm)
##  __Конструкторы
[EmailsNotificationRecipientsSource](M_Tessa_Notices_Sources_EmailsNotificationRecipientsSource__ctor.htm)|
Инициализирует новый экземпляр класса EmailsNotificationRecipientsSource  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetRecipientsAsync](M_Tessa_Notices_Sources_EmailsNotificationRecipientsSource_GetRecipientsAsync.htm)|
Возвращает список получателей уведомления.  
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
