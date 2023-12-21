# StateHandlerResult - класс
Результат обработки состояния.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.StateMachine](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StateHandlerResult : IStateHandlerResult
VB __Копировать
     Public NotInheritable Class StateHandlerResult
    	Implements IStateHandlerResult
C++ __Копировать
     public ref class StateHandlerResult sealed : IStateHandlerResult
F# __Копировать
     [<SealedAttribute>]
    type StateHandlerResult = 
        class
            interface IStateHandlerResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StateHandlerResult
Implements
    [IStateHandlerResult](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_IStateHandlerResult.htm)
##  __Конструкторы
[StateHandlerResult](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult__ctor.htm)|
Инициализирует новый экземпляр класса StateHandlerResult.  
---|---  
## __Свойства
[ContinueCurrentRun](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_ContinueCurrentRun.htm)|
Возвращает значение, показывающее, необходимо ли после обработки сотсояния
продолжать текущее выполнение runner-a. Значение false, если текущее
выполнение должно быть прервано. Если запланировано еще одно сохранение
карточки, приводящее к запуску runner-a, то runner будет запущен с текущим
KrScope.  
---|---  
[ForceStartGroup](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_ForceStartGroup.htm)|
Возвращает значение, показывающее, необходимо ли начать выполнение этапов из
следующей группы этапов, несмотря на то, что в текущей группе этапов остались
не обработанные этапы.  
[Handled](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_Handled.htm)|
Возвращает значение, показывающее, что состояние было обработано.  
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
[ContinueCurrentRunResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_ContinueCurrentRunResult.htm)|
Результат обработки состояния без необходимости сохранения изменений.  
---|---  
[ContinueCurrentRunWithStartingNewGroupResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_ContinueCurrentRunWithStartingNewGroupResult.htm)|
Результат обработки состояния без необходимости сохранения изменений.  
[EmptyResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_EmptyResult.htm)|
Состояние не было обработано.  
[WithoutContinuationProcessResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_StateHandlerResult_WithoutContinuationProcessResult.htm)|
Результат обработки состояния с необходимостью сохранить изменения.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.StateMachine -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine.htm)
