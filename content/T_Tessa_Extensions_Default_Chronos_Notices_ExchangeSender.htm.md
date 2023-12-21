# ExchangeSender - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Chronos.Notices](N_Tessa_Extensions_Default_Chronos_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Chronos (в
Tessa.Extensions.Default.Chronos.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExchangeSender : MailSender, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class ExchangeSender
    	Inherits MailSender
    	Implements IAsyncDisposable
C++ __Копировать
     public ref class ExchangeSender sealed : public MailSender, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type ExchangeSender = 
        class
            inherit MailSender
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm) __ ExchangeSender
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Конструкторы
[ExchangeSender](M_Tessa_Extensions_Default_Chronos_Notices_ExchangeSender__ctor.htm)|
Инициализирует новый экземпляр класса ExchangeSender  
---|---  
##  __Свойства
[Context](P_Tessa_Extensions_Default_Chronos_Notices_MailSender_Context.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
---|---  
[MaxAttemptsBeforeDelete](P_Tessa_Extensions_Default_Chronos_Notices_MailSender_MaxAttemptsBeforeDelete.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
[MaxFilesSizeEmail](P_Tessa_Extensions_Default_Chronos_Notices_MailSender_MaxFilesSizeEmail.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
[Settings](P_Tessa_Extensions_Default_Chronos_Notices_ExchangeSender_Settings.htm)|  
[StopRequested](P_Tessa_Extensions_Default_Chronos_Notices_MailSender_StopRequested.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
##  __Методы
[AddMissedFilesInfo](M_Tessa_Extensions_Default_Chronos_Notices_MailSender_AddMissedFilesInfo.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
---|---  
[DisposeAsync](M_Tessa_Extensions_Default_Chronos_Notices_ExchangeSender_DisposeAsync.htm)|  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[LogProcessingErrorAsync](M_Tessa_Extensions_Default_Chronos_Notices_MailSender_LogProcessingErrorAsync.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ProcessAsync](M_Tessa_Extensions_Default_Chronos_Notices_MailSender_ProcessAsync.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
[ProcessMessageAsync](M_Tessa_Extensions_Default_Chronos_Notices_MailSender_ProcessMessageAsync.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
[SendMessageAsync](M_Tessa_Extensions_Default_Chronos_Notices_ExchangeSender_SendMessageAsync.htm)|  
(Переопределяет [MailSender.SendMessageAsync(MailSenderMessage,
CancellationToken)](M_Tessa_Extensions_Default_Chronos_Notices_MailSender_SendMessageAsync.htm))  
[StartAsync](M_Tessa_Extensions_Default_Chronos_Notices_MailSender_StartAsync.htm)|  
(Унаследован от
[MailSender](T_Tessa_Extensions_Default_Chronos_Notices_MailSender.htm))  
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
[Tessa.Extensions.Default.Chronos.Notices - пространство
имён](N_Tessa_Extensions_Default_Chronos_Notices.htm)
