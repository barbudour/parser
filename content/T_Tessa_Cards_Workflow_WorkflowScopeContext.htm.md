# WorkflowScopeContext - класс
Контекст бизнес-процессов на Workflow API. Позволяет в процессе сохранения
получить информацию по родительскому контексту сохранения
[StoreContext](P_Tessa_Cards_Workflow_WorkflowScopeContext_StoreContext.htm),
а также по контексту Workflow API.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowScopeContext : IWorkflowScopeContext
VB __Копировать
     Public NotInheritable Class WorkflowScopeContext
    	Implements IWorkflowScopeContext
C++ __Копировать
     public ref class WorkflowScopeContext sealed : IWorkflowScopeContext
F# __Копировать
     [<SealedAttribute>]
    type WorkflowScopeContext = 
        class
            interface IWorkflowScopeContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowScopeContext
Implements
    [IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm)
##  __Конструкторы
[WorkflowScopeContext](M_Tessa_Cards_Workflow_WorkflowScopeContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Current](P_Tessa_Cards_Workflow_WorkflowScopeContext_Current.htm)|  Текущий
контекст
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm).  
---|---  
[HasCurrent](P_Tessa_Cards_Workflow_WorkflowScopeContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm), а
свойство [Current](P_Tessa_Cards_Workflow_WorkflowScopeContext_Current.htm)
ссылается на действительный контекст.  
[Parent](P_Tessa_Cards_Workflow_WorkflowScopeContext_Parent.htm)|
Родительский контекст Workflow (для нескольких вложенных сохранений,
регулируемых через Workflow). Значение может быть равно null в том случае,
если родительский или текущий объект контекста пустой.  
[StoreContext](P_Tessa_Cards_Workflow_WorkflowScopeContext_StoreContext.htm)|
Контекст по сохранению карточки, в котором было инициировано вложенное
сохранение через Workflow API. Например, в контексте содержится информация по
завершению задания, а в расширении на создание задания, отправленного через
Workflow API, возможно получить информацию по завершённому заданию. Значение
может быть равно null только в том случае, если текущий объект контекста
пустой, т.е. операция выполняется вне пределов Workflow.  
[Unknown](P_Tessa_Cards_Workflow_WorkflowScopeContext_Unknown.htm)|
Неизвестный контекст
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm).  
[WorkflowContext](P_Tessa_Cards_Workflow_WorkflowScopeContext_WorkflowContext.htm)|
Контекст бизнес-процесса, содержащий информацию по сохраняемой карточке.
Значение может быть равно null только в том случае, если текущий объект
контекста пустой, т.е. операция выполняется вне пределов Workflow.  
[WorkflowManager](P_Tessa_Cards_Workflow_WorkflowScopeContext_WorkflowManager.htm)|
Объект, предоставляющий возможности для управления бизнес-процессом. Значение
может быть равно null только в том случае, если текущий объект контекста
пустой, т.е. операция выполняется вне пределов Workflow.  
[WorkflowWorker](P_Tessa_Cards_Workflow_WorkflowScopeContext_WorkflowWorker.htm)|
Объект, реализующий логику подпроцессов и переходов в бизнес-процессе.
Значение может быть равно null только в том случае, если текущий объект
контекста пустой, т.е. операция выполняется вне пределов Workflow.  
## __Методы
[Create](M_Tessa_Cards_Workflow_WorkflowScopeContext_Create.htm)|  Создаёт
область операции, в которой заданный контекст будет являться текущим.  
---|---  
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
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
