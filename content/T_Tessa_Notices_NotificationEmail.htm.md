# NotificationEmail - класс
Сообщение почты, формируемое и отправляемое объектом
[INotificationManager](T_Tessa_Notices_INotificationManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NotificationEmail
VB __Копировать
     Public NotInheritable Class NotificationEmail
C++ __Копировать
     public ref class NotificationEmail sealed
F# __Копировать
     [<SealedAttribute>]
    type NotificationEmail = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationEmail
##  __Конструкторы
[NotificationEmail](M_Tessa_Notices_NotificationEmail__ctor.htm)|
Инициализирует новый экземпляр класса NotificationEmail  
---|---  
##  __Свойства
[BodyTemplate](P_Tessa_Notices_NotificationEmail_BodyTemplate.htm)|  Тело
документа с плейсхолдерами.  
---|---  
[GetMailInfoFuncAsync](P_Tessa_Notices_NotificationEmail_GetMailInfoFuncAsync.htm)|
Функция, вызываемая для каждого получателя, которому фактически отправляется
письмо. Возвращает объект
[MailInfo](P_Tessa_Notices_NotificationEmail_MailInfo.htm), содержащий также
информацию по файлам, прикладываемым к письмам. Если свойство возвращает null
или функция вернула null, то используется значение по умолчанию
[MailInfo](P_Tessa_Notices_NotificationEmail_MailInfo.htm). Если оно также
равно null, то выполняется отправка без приложенных файлов. По умолчанию
свойство равно null.  
[IsGlobal](P_Tessa_Notices_NotificationEmail_IsGlobal.htm)|  Определяет,
является ли данное уведомление глобальным. Определяется по типу уведомления  
[MailInfo](P_Tessa_Notices_NotificationEmail_MailInfo.htm)|  Объект,
содержащий информацию по файлам, прикладываемым к письмам. Значение свойства
используется, если функция
[GetMailInfoFuncAsync](P_Tessa_Notices_NotificationEmail_GetMailInfoFuncAsync.htm)
не задана или возвращает null. Если текущее свойство также возвращает null, то
выполняется отправка без приложенных файлов. По умолчанию свойство равно null.  
[ModifyBodyFuncAsync](P_Tessa_Notices_NotificationEmail_ModifyBodyFuncAsync.htm)|
Функция, вызываемая для каждого получателя, которому фактически отправляется
письмо. Производит изменение тела письма, сформированную под конкретного
получателя. Если свойство возвращает null или функция вернула null, то
модификация тела письма не производится. По умолчанию свойство равно null.  
[ModifySubjectFuncAsync](P_Tessa_Notices_NotificationEmail_ModifySubjectFuncAsync.htm)|
Функция, вызываемая для каждого получателя, которому фактически отправляется
письмо. Производит изменение темы письма, сформированную под конкретного
получателя. Если свойство возвращает null или функция вернула null, то
модификация темы письма не производится. По умолчанию свойство равно null.  
[NotificationID](P_Tessa_Notices_NotificationEmail_NotificationID.htm)|
Идентификатор карточки уведомления. Если уведомление сформировано не по
карточке, имеет значение null.  
[NotificationType](P_Tessa_Notices_NotificationEmail_NotificationType.htm)|
Идентификатор типа уведомления.  
[PlaceholderAliases](P_Tessa_Notices_NotificationEmail_PlaceholderAliases.htm)|
Алиасы плейсхолдеров. Могут быть равны null.  
[SubjectTemplate](P_Tessa_Notices_NotificationEmail_SubjectTemplate.htm)|
Тема документа с плейсхолдерами.  
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
