# Pop3MailReceiver - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Chronos.Workflow](N_Tessa_Extensions_Default_Chronos_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Chronos (в
Tessa.Extensions.Default.Chronos.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Pop3MailReceiver : IMailReceiver, 
    	IPop3ImapSettingsContainer
VB __Копировать
     Public NotInheritable Class Pop3MailReceiver
    	Implements IMailReceiver, IPop3ImapSettingsContainer
C++ __Копировать
     public ref class Pop3MailReceiver sealed : IMailReceiver, 
    	IPop3ImapSettingsContainer
F# __Копировать
     [<SealedAttribute>]
    type Pop3MailReceiver = 
        class
            interface IMailReceiver
            interface IPop3ImapSettingsContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Pop3MailReceiver
Implements
    [IPop3ImapSettingsContainer](T_Tessa_Extensions_Default_Server_Notices_IPop3ImapSettingsContainer.htm), [IMailReceiver](T_Tessa_Extensions_Default_Server_Workflow_IMailReceiver.htm)
##  __Конструкторы
[Pop3MailReceiver](M_Tessa_Extensions_Default_Chronos_Workflow_Pop3MailReceiver__ctor.htm)|
Инициализирует новый экземпляр класса Pop3MailReceiver  
---|---  
##  __Свойства
[Pop3ImapSettings](P_Tessa_Extensions_Default_Chronos_Workflow_Pop3MailReceiver_Pop3ImapSettings.htm)|
Настройки отправки и получения почты по протоколу POP3 или IMAP.  
---|---  
[StopRequested](P_Tessa_Extensions_Default_Chronos_Workflow_Pop3MailReceiver_StopRequested.htm)|  
[StopRequestedFunc](P_Tessa_Extensions_Default_Chronos_Workflow_Pop3MailReceiver_StopRequestedFunc.htm)|
Функция, возвращающая признак того, что запрошена остановка процесса обработки
писем.  
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
[ReceiveMessagesAsync](M_Tessa_Extensions_Default_Chronos_Workflow_Pop3MailReceiver_ReceiveMessagesAsync.htm)|
Обработка сообщений  
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
[Tessa.Extensions.Default.Chronos.Workflow - пространство
имён](N_Tessa_Extensions_Default_Chronos_Workflow.htm)
