# WorkflowCheckRolesForExecutionTileManagerExtension - класс
Расширение прав доступа к тайлам процесса, которое проверяет доступ по ролям
на выполнение.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Workflow](N_Tessa_Extensions_Platform_Server_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowCheckRolesForExecutionTileManagerExtension : IWorkflowEngineTileManagerExtension, 
    	IRegistryItem<Guid>
VB __Копировать
     Public NotInheritable Class WorkflowCheckRolesForExecutionTileManagerExtension
    	Implements IWorkflowEngineTileManagerExtension, IRegistryItem(Of Guid)
C++ __Копировать
     public ref class WorkflowCheckRolesForExecutionTileManagerExtension sealed : IWorkflowEngineTileManagerExtension, 
    	IRegistryItem<Guid>
F# __Копировать
     [<SealedAttribute>]
    type WorkflowCheckRolesForExecutionTileManagerExtension = 
        class
            interface IWorkflowEngineTileManagerExtension
            interface IRegistryItem<Guid>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowCheckRolesForExecutionTileManagerExtension
Implements
    [IRegistryItem](T_Tessa_Platform_IRegistryItem_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>, [IWorkflowEngineTileManagerExtension](T_Tessa_Workflow_IWorkflowEngineTileManagerExtension.htm)
##  __Конструкторы
[WorkflowCheckRolesForExecutionTileManagerExtension](M_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension__ctor.htm)|
Инициализирует новый экземпляр класса
WorkflowCheckRolesForExecutionTileManagerExtension  
---|---  
##  __Свойства
[ExtensionTypeID](P_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_ExtensionTypeID.htm)|
ID расширения.  
---|---  
[ID](P_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_ID.htm)|
Идентификатор объекта, по которому выполняется регистрация в реестре.  
[Name](P_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_Name.htm)|
Имя расширения.  
[Order](P_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_Order.htm)|
Порядок расширения. Влияет порядок отображения контролов в окне настройки
кнопки.  
## __Методы
[CheckTileAccessForExecuteAsync](M_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_CheckTileAccessForExecuteAsync.htm)|
Метод для проверки доступа списка тайлов на выполнение.  
---|---  
[CheckTileAccessForVisibilityAsync](M_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_CheckTileAccessForVisibilityAsync.htm)|
Метод для проверки доступа списка тайлов на просмотр.  
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
##  __Поля
[ExtensionID](F_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_ExtensionID.htm)|  
---|---  
[WorkflowCheckRolesForExecutionTileManagerExtensionTypeID](F_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_WorkflowCheckRolesForExecutionTileManagerExtensionTypeID.htm)|
Card type identifier for "WorkflowCheckRolesForExecutionTileManagerExtension":
{0295BFB2-ACF1-415B-AA6D-B272D8EBC3FE}.  
[WorkflowCheckRolesForExecutionTileManagerExtensionTypeName](F_Tessa_Extensions_Platform_Server_Workflow_WorkflowCheckRolesForExecutionTileManagerExtension_WorkflowCheckRolesForExecutionTileManagerExtensionTypeName.htm)|
Card type name for "WorkflowCheckRolesForExecutionTileManagerExtension".  
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
[Tessa.Extensions.Platform.Server.Workflow - пространство
имён](N_Tessa_Extensions_Platform_Server_Workflow.htm)
