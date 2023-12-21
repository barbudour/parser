# GlobalSignalHandlerResult - класс
Представляет результат обработки глобального сигнала.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.GlobalSignals](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GlobalSignalHandlerResult : IGlobalSignalHandlerResult
VB __Копировать
     Public NotInheritable Class GlobalSignalHandlerResult
    	Implements IGlobalSignalHandlerResult
C++ __Копировать
     public ref class GlobalSignalHandlerResult sealed : IGlobalSignalHandlerResult
F# __Копировать
     [<SealedAttribute>]
    type GlobalSignalHandlerResult = 
        class
            interface IGlobalSignalHandlerResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalSignalHandlerResult
Implements
    [IGlobalSignalHandlerResult](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_IGlobalSignalHandlerResult.htm)
##  __Конструкторы
[GlobalSignalHandlerResult](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult__ctor.htm)|
Инициализирует новый экземпляр класса GlobalSignalHandlerResult.  
---|---  
## __Свойства
[ContinueCurrentRun](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_ContinueCurrentRun.htm)|
Возвращает значение, показывающее, необходимо ли после обработки сигнала
продолжать текущее выполнение runner-a. Значение false, если текущее
выполнение должно быть прервано. Если запланировано еще одно сохранение
карточки, приводящее к запуску runner-a, то runner будет запущен с текущим
KrScope.  
---|---  
[ForceStartGroup](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_ForceStartGroup.htm)|
Возвращает значение, показывающее, необходимо ли начать выполнение этапов из
следующей группы этапов, несмотря на то, что в текущей группе этапов остались
не обработанные этапы.  
[Handled](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_Handled.htm)|
Возвращает значение, показывающее, что сигнал был обработан.  
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
##  __Поля
[ContinueCurrentRunResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_ContinueCurrentRunResult.htm)|
Сигнал был обработан. Необходимо продолжить выполнение runner-а.  
---|---  
[ContinueCurrentRunWithStartingNewGroupResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_ContinueCurrentRunWithStartingNewGroupResult.htm)|
Сигнал был обработан. Необходимо продолжить выполнение runner-а и начать
выполнение этапов из следующей группы этапов.  
[EmptyHandlerResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_EmptyHandlerResult.htm)|
Сигнал не был обработан. Необходимо продолжить выполнение runner-а.  
[WithoutContinuationProcessResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_GlobalSignalHandlerResult_WithoutContinuationProcessResult.htm)|
Сигнал был обработан. Необходимо прервать выполнение runner-а.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.GlobalSignals -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals.htm)
