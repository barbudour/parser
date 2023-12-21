# WfUIHelper - класс
Вспомогательные поля и методы, которые используются для построения
пользовательского интерфейса для бизнес-процессов Workflow.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WfUIHelper
VB __Копировать
     Public NotInheritable Class WfUIHelper
C++ __Копировать
     public ref class WfUIHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WfUIHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WfUIHelper
##  __Методы
[HasControlsWithSuffix](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_HasControlsWithSuffix.htm)|
Возвращает признак того, что в заданном блоке block есть хотя бы один элемент
управления, имя которого заканчивается на суффикс suffix.  
---|---  
[SetControlVisibility](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_SetControlVisibility.htm)|
Устанавливает видимость элементов управления для текущего блока.  
[VisualizeResolutionsAsync(IWfResolutionVisualizationGenerator, INodeLayout,
INodeFactory, Card, CardTask, IExtensionContainer,
CancellationToken)](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_VisualizeResolutionsAsync.htm)|
Выполняет визуализацию резолюций, начиная от заданной резолюции
rootResolution.  
[VisualizeResolutionsAsync(IWfResolutionVisualizationGenerator, INodeLayout,
INodeFactory, Card, CardTaskHistoryItem, IExtensionContainer,
CancellationToken)](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_VisualizeResolutionsAsync_2.htm)|
Выполняет визуализацию резолюций, начиная от заданной записи в истории
резолюций rootHistoryItem.  
[VisualizeResolutionsAsync(IWfResolutionVisualizationGenerator, INodeLayout,
INodeFactory, Card, CardTaskHistoryItem, CardTask, IExtensionContainer,
CancellationToken)](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_VisualizeResolutionsAsync_1.htm)|
Выполняет визуализацию резолюций, начиная от заданных записи в истории
резолюций rootHistoryItem и резолюции rootResolution.  
## __Поля
[AdditionalSuffix](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_AdditionalSuffix.htm)|
Суффикс для имени такого элемента управления в блоке задания
[MainInfoBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_MainInfoBlockName.htm),
который должен быть доступен только при выделении галки "дополнительно".  
---|---  
[ChildResolutionsBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_ChildResolutionsBlockName.htm)|
Имя блока в задании для дочерних резолюций.  
[ChildResolutionsSuffix](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_ChildResolutionsSuffix.htm)|
Суффикс для имени такого элемента управления в блоке задания
[MainInfoBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_MainInfoBlockName.htm),
который должен быть доступен только при наличии хотя бы одной дочерней
резолюции.  
[MainInfoBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_MainInfoBlockName.htm)|
Имя блока в задании для основной информации.  
[MassCreationSuffix](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_MassCreationSuffix.htm)|
Суффикс для имени такого элемента управления в блоке задания
[PerformersBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_PerformersBlockName.htm),
который должен быть доступен только при наличии хотя бы двух ролей в списке
исполнителей резолюции, а также при установленном флажке "Отдельная задача
каждому исполнителю".  
[MultiplePerformersSuffix](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_MultiplePerformersSuffix.htm)|
Суффикс для имени такого элемента управления в блоке задания
[PerformersBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_PerformersBlockName.htm),
который должен быть доступен только при наличии хотя бы двух ролей в списке
исполнителей резолюции.  
[NavigateTaskCardResolutionProcessMenuAction](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_NavigateTaskCardResolutionProcessMenuAction.htm)|
Имя элемента меню для перехода к карточке с файлами, приложенными к заданию.  
[PerformersBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_PerformersBlockName.htm)|
Имя блока для списка исполнителей.  
[UseResolutionsBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_UseResolutionsBlockName.htm)|
Имя блока в настройках типа карточки и типа документа для настроек резолюций.  
[UseResolutionsSuffix](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_UseResolutionsSuffix.htm)|
Суффикс для имени такого элемента управления в блоке настроек
[UseResolutionsBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_UseResolutionsBlockName.htm),
который должен быть доступен только при установке флага "Использовать
резолюции".  
[VisualizeResolutionBranchMenuAction](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_VisualizeResolutionBranchMenuAction.htm)|
Имя элемента меню для визуализации ветки резолюций.  
[VisualizeResolutionProcessMenuAction](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_VisualizeResolutionProcessMenuAction.htm)|
Имя элемента меню для визуализации процесса резолюций.  
[VisualizeResolutionSeparatorMenuAction](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_VisualizeResolutionSeparatorMenuAction.htm)|
Имя сепаратора меню, отделяющего элементы меню, связанные с визуализацией, от
других элементов.  
[WithControlSuffix](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_WithControlSuffix.htm)|
Суффикс для имени такого элемента управления в блоке задания
[MainInfoBlockName](F_Tessa_Extensions_Default_Client_Workflow_Wf_WfUIHelper_MainInfoBlockName.htm),
который должен быть доступен только при выделении галки "с контролем".  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
