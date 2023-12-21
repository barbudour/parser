# IWorkflowEngineTileManagerExtension - интерфейс
Расширение прав доступа к тайлам WorkflowEngine, проверяемым в
[IWorkflowEngineTileManager](T_Tessa_Workflow_IWorkflowEngineTileManager.htm).
Регистрируются через
[IWorkflowEngineTileManagerExtensionRegistry](T_Tessa_Workflow_IWorkflowEngineTileManagerExtensionRegistry.htm).
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineTileManagerExtension : IRegistryItem<Guid>
VB __Копировать
     Public Interface IWorkflowEngineTileManagerExtension
    	Inherits IRegistryItem(Of Guid)
C++ __Копировать
     public interface class IWorkflowEngineTileManagerExtension : IRegistryItem<Guid>
F# __Копировать
     type IWorkflowEngineTileManagerExtension = 
        interface
            interface IRegistryItem<Guid>
        end
Implements
    [IRegistryItem](T_Tessa_Platform_IRegistryItem_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Свойства
[ExtensionTypeID](P_Tessa_Workflow_IWorkflowEngineTileManagerExtension_ExtensionTypeID.htm)|
ID расширения.  
---|---  
[ID](P_Tessa_Platform_IRegistryItem_1_ID.htm)| Идентификатор объекта, по
которому выполняется регистрация в реестре.  
(Унаследован от
[IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm))  
[Name](P_Tessa_Workflow_IWorkflowEngineTileManagerExtension_Name.htm)|  Имя
расширения.  
[Order](P_Tessa_Workflow_IWorkflowEngineTileManagerExtension_Order.htm)|
Порядок расширения. Влияет порядок отображения контролов в окне настройки
кнопки.  
## __Методы
[CheckTileAccessForExecuteAsync](M_Tessa_Workflow_IWorkflowEngineTileManagerExtension_CheckTileAccessForExecuteAsync.htm)|
Метод для проверки доступа списка тайлов на выполнение.  
---|---  
[CheckTileAccessForVisibilityAsync](M_Tessa_Workflow_IWorkflowEngineTileManagerExtension_CheckTileAccessForVisibilityAsync.htm)|
Метод для проверки доступа списка тайлов на просмотр.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
