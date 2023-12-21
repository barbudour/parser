# KrEventExtensionContext - класс
Контекст
[IKrEventManager](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Events](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrEventExtensionContext : IKrEventExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrEventExtensionContext
    	Implements IKrEventExtensionContext, IExtensionContext
C++ __Копировать
     public ref class KrEventExtensionContext sealed : IKrEventExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrEventExtensionContext = 
        class
            interface IKrEventExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrEventExtensionContext
Implements
    [IKrEventExtensionContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrEventExtensionContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext__ctor.htm)|
Инициализирует новый экземпляр класса KrEventExtensionContext  
---|---  
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_CancellationToken.htm)|  
---|---  
[CardExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_CardExtensionContext.htm)|
Контекст расширения, в рамках которого выполняется Kr процесс.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_ContextualSatellite.htm)|
Текущий контекстуальный сателлит.  
[EventType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_EventType.htm)|
Тип события.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_Info.htm)|
Дополнительная неперсистентная информация о событии.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_InitiationCause.htm)|
Причина, по которой был вызван раннер: запуск процесса, завершение задания,
обработка сигнала и др.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[MainCardDocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_MainCardDocTypeID.htm)|
Тип документа основной карточки или значение null, если процесс запущен вне
карточки.  
[MainCardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_MainCardID.htm)|
Идентификатор основной карточки или значение null, если процесс запущен вне
карточки.  
[MainCardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_MainCardType.htm)|
Тип основной карточки или значение null, если процесс запущен вне карточки.  
[ProcessHolder](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_ProcessHolder.htm)|
Холдер текущего процесса.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_ProcessHolderSatellite.htm)|
Текущий сателлит процесса.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_ProcessInfo.htm)|
Информация по процессу WorkflowAPI.  
[RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_RunnerMode.htm)|
Режим раннера, запустившего обработку этапа.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_SecondaryProcess.htm)|
Вторичный процесс.  
[SignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_SignalInfo.htm)|
Информация по сигналу WorkflowAPI.  
[Stage](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_Stage.htm)|
Текущий этап процесса.  
[TaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_TaskInfo.htm)|
Информация по заданию WorkflowAPI.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_ValidationResult.htm)|
Результат валидации.  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensionContext_WorkflowProcess.htm)|
Процесс.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Events - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events.htm)
