# IKrTypesCache - интерфейс
Кэш по типам карточек и документов, содержащих информацию по типовому решению.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrTypesCache
VB __Копировать
     Public Interface IKrTypesCache
C++ __Копировать
     public interface class IKrTypesCache
F# __Копировать
     type IKrTypesCache = interface end
##  __Методы
[GetCardTypesAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_GetCardTypesAsync.htm)|
Типы карточек, указанные в настройках типового решения. Возвращаемое значение
не равно null.  
---|---  
[GetDocTypesAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_GetDocTypesAsync.htm)|
Типы документов, определенные и используемые в системе, т.е. типы документов
для типов карточек у которых в настройках типового процесса включено
использование типов документов. Возвращаемое значение не равно null.  
[GetTypesAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_GetTypesAsync.htm)|
Типы карточек и типы документов, определенные и используемые в типовом
решении. Возвращаемое значение не равно null.  
[InvalidateAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_InvalidateAsync.htm)|
Сбрасывает кэш типов. При следующем их запросе они будут перерасчитаны.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
