# StageHandlerResult - структура
Результат выполнения этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct StageHandlerResult : IEquatable<StageHandlerResult>
VB __Копировать
     Public Structure StageHandlerResult
    	Implements IEquatable(Of StageHandlerResult)
C++ __Копировать
     public value class StageHandlerResult : IEquatable<StageHandlerResult>
F# __Копировать
     [<SealedAttribute>]
    type StageHandlerResult = 
        struct
            inherit ValueType
            interface IEquatable<StageHandlerResult>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ StageHandlerResult
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<StageHandlerResult>
##  __Конструкторы
[StageHandlerResult](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult__ctor.htm)|
Инициализирует новый экземпляр объекта StageHandlerResult.  
---|---  
## __Свойства
[Action](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_Action.htm)|
Возвращает результат взаимодействия StageRunner c этапом после выполнения его
обработчика.  
---|---  
[KeepStageStates](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_KeepStageStates.htm)|
Возвращает значение флага показывающего, что необходимо сохранить состояния
этапов.  
[TransitionID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_TransitionID.htm)|
Возвращает идентификатор объекта (этапа или группы этапов) к которому должен
быть выполнен переход.  
## __Методы
[CurrentGroupTransition](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_CurrentGroupTransition.htm)|
Сообщение для ProcessRunner о том, что следует совершить переход в начало
текущей группы.  
---|---  
[Equals(Object)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_Equals.htm)|
Indicates whether this instance and a specified object are equal.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Equals(StageHandlerResult)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_Equals_1.htm)|
Indicates whether the current object is equal to another object of the same
type.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_GetHashCode.htm)|
Returns the hash code for this instance.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GroupTransition](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_GroupTransition.htm)|
Сообщение для ProcessRunner о том, что следует совершить переход в начало
другой группы этапов.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NextGroupTransition](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_NextGroupTransition.htm)|
Сообщение для ProcessRunner о том, что следует совершить переход на следующую
группу с учетом пересчета набора групп.  
[PreviousGroupTransition](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_PreviousGroupTransition.htm)|
Сообщение для ProcessRunner о том, что следует совершить переход на следующую
группу с учетом пересчета набора групп.  
[ToString](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring)| Returns the fully qualified type name of this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
[Transition](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_Transition.htm)|
Сообщение для ProcessRunner о том, что следует совершить переход на другой
этап в текущей группе.  
## __Операторы
[Equality(StageHandlerResult,
StageHandlerResult)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_op_Equality.htm)|  
---|---  
[Inequality(StageHandlerResult,
StageHandlerResult)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_op_Inequality.htm)|  
## __Поля
[CancelProcessResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_CancelProcessResult.htm)|
Сообщение для ProcessRunner о том, что необходимо отменить весь процесс.  
---|---  
[CompleteResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_CompleteResult.htm)|
Сообщение для ProcessRunner о том, что этап завершен.  
[EmptyResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_EmptyResult.htm)|
Сообщение для ProcessRunner о том, что обработчик не обработал этап.  
[InProgressResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_InProgressResult.htm)|
Сообщение для ProcessRunner о том, что этап в активном состоянии.  
[SkipProcessResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_SkipProcessResult.htm)|
Сообщение для ProcessRunner о том, что необходимо пропустить весь процесс.  
[SkipResult](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_SkipResult.htm)|
Сообщение для ProcessRunner о том, что этап следует пропустить.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
