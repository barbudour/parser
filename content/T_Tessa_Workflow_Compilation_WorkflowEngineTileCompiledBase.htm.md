# WorkflowEngineTileCompiledBase - класс
Базовый класс для объекта компиляции, выполняемого при выполнении кнопок
## __Definition
 **Пространство имён:**
[Tessa.Workflow.Compilation](N_Tessa_Workflow_Compilation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WorkflowEngineTileCompiledBase : IWorkflowEngineTileCompiled
VB __Копировать
     Public MustInherit Class WorkflowEngineTileCompiledBase
    	Implements IWorkflowEngineTileCompiled
C++ __Копировать
     public ref class WorkflowEngineTileCompiledBase abstract : IWorkflowEngineTileCompiled
F# __Копировать
     [<AbstractClassAttribute>]
    type WorkflowEngineTileCompiledBase = 
        class
            interface IWorkflowEngineTileCompiled
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineTileCompiledBase
Implements
    [IWorkflowEngineTileCompiled](T_Tessa_Workflow_Compilation_IWorkflowEngineTileCompiled.htm)
##  __Конструкторы
[WorkflowEngineTileCompiledBase](M_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineTileCompiledBase  
---|---  
##  __Свойства
[Card](P_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_Card.htm)|
dynamic-обёртка над строковыми секциями карточки или null, если условия
проверяются вне контекста карточки.  
---|---  
[CardObject](P_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_CardObject.htm)|
Карточка, для которой проверяется условие, или null, если условия проверяются
вне контекста карточки.  
[Container](P_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_Container.htm)|  
[DbScope](P_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_DbScope.htm)|
Объект для взаимодействия с базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
[Session](P_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_Session.htm)|
Сессия пользователя.  
[Tables](P_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_Tables.htm)|
dynamic-обёртка над коллекционными секциями карточки или null, если условия
проверяются вне контекста карточки.  
## __Методы
[ConditionAsync](M_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_ConditionAsync.htm)|
Скрипт условия.  
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
[SetDependencies](M_Tessa_Workflow_Compilation_WorkflowEngineTileCompiledBase_SetDependencies.htm)|
Метод для установки зависимостей скомпилированного объекта.  
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
[Tessa.Workflow.Compilation - пространство
имён](N_Tessa_Workflow_Compilation.htm)
