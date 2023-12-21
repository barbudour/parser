# KrComponentsHelper - класс
Предоставляет методы для работы с компонентами типового решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrComponentsHelper
VB __Копировать
     Public NotInheritable Class KrComponentsHelper
C++ __Копировать
     public ref class KrComponentsHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrComponentsHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrComponentsHelper
##  __Методы
[CheckKrComponentsAsync(Card, Nullable<Guid>, IDbScope, IKrTypesCache,
KrComponents,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_CheckKrComponentsAsync_1.htm)|
Проверяет наличие необходимых настроек у карточки типового решения.  
---|---  
[CheckKrComponentsAsync(Guid, Guid, Nullable<Guid>, IDbScope, IKrTypesCache,
KrComponents,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_CheckKrComponentsAsync.htm)|
Проверяет наличие необходимых настроек у карточки типового решения.  
[GetKrComponentsAsync(Card, IKrTypesCache,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync_5.htm)|
Возвращает включенные компоненты типового решения для указанной карточки.  
[GetKrComponentsAsync(Guid, ICardCache,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync_2.htm)|
Возвращает включенные компоненты типового решения для указанного типа карточки
с использованием [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm).
Использовать для избежания циклических вызовов.  
[GetKrComponentsAsync(Guid, IKrTypesCache,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync_3.htm)|
Возвращает включенные компоненты типового решения только для типа карточки без
учета типа документа.  
[GetKrComponentsAsync(Card, IKrTypesCache, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync_6.htm)|
Возвращает включенные компоненты типового решения для указанной карточки.  
[GetKrComponentsAsync(Guid, Nullable<Guid>, IKrTypesCache,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync_1.htm)|
Возвращает включенные компоненты типового решения только для типа карточки по
известному типу карточки и документа.  
[GetKrComponentsAsync(Guid, IKrTypesCache, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync_4.htm)|
Возвращает включенные компоненты типового решения для карточки с учетом типа
документа.  
[GetKrComponentsAsync(Guid, Guid, IKrTypesCache, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync.htm)|
Возвращает включенные компоненты типового решения для указанной карточки с
учетом типа документа. Тип документа получается из базы данных.  
[HasBaseAsync(Guid, ICardCache,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_HasBaseAsync.htm)|
Определяет включен ли тип в типовое решение.  
[HasBaseAsync(Guid, IKrTypesCache,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_HasBaseAsync_1.htm)|
Определяет включён ли тип в типовое решение.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
