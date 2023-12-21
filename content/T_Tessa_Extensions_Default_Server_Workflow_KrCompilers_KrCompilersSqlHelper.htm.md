# KrCompilersSqlHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrCompilersSqlHelper
VB __Копировать
     Public NotInheritable Class KrCompilersSqlHelper
C++ __Копировать
     public ref class KrCompilersSqlHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrCompilersSqlHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrCompilersSqlHelper
##  __Методы
[GetFilteredStageTemplates](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_GetFilteredStageTemplates.htm)|
Возвращает список идентификаторов шаблонов для указанных: типа
карточки/документа, пользователя и группы этапов.  
---|---  
[SelectCommonMethodsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectCommonMethodsAsync.htm)|
Возвращает список базовых методов.  
[SelectFilteredStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectFilteredStageGroupsAsync.htm)|
Возвращает список идентификаторов групп этапов удовлетворяющих условиям: типа
карточки/документа, идентификатора пользователя, порядковый номер лежит в
интервале [orderFrom; orderTo] и связанного со вторичным процессом имеющим
указанный идентификатор.  
[SelectKrSecondaryProcessesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectKrSecondaryProcessesAsync.htm)|
Возвращает информацию по вторичному процессу из БД.  
[SelectRuntimeStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectRuntimeStagesAsync.htm)|
Возвращает список с информацией по рантайм скриптам этапов полученный из БД.  
[SelectSecondaryProcessRuntimeStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectSecondaryProcessRuntimeStagesAsync.htm)|
Возвращает список с информацией по рантайм скриптам этапов вторичных процессов
полученный из БД.  
[SelectStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectStageGroupsAsync.htm)|
Возвращает список содержащий информацию по группам этапов.  
[SelectStageTemplatesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectStageTemplatesAsync.htm)|
Загружает из БД шаблоны этапов.  
[SelectVirtualStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectVirtualStageGroupsAsync.htm)|
Возвращает список виртуальных групп по вторичным процессам.  
[SelectVirtualStageTemplatesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersSqlHelper_SelectVirtualStageTemplatesAsync.htm)|
Возвращает список содержащий информацию по виртуальным шаблонам вторичных
процессов.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
