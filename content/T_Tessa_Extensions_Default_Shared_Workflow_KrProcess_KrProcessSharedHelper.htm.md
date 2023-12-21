# KrProcessSharedHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrProcessSharedHelper
VB __Копировать
     Public NotInheritable Class KrProcessSharedHelper
C++ __Копировать
     public ref class KrProcessSharedHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrProcessSharedHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessSharedHelper
##  __Методы
[CanBeHidden](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_CanBeHidden.htm)|
Возвращает значение, показывающее, разрешено ли скрытие этапа в дескрипторе
типа этапа или нет.  
---|---  
[CanBeSkipped](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_CanBeSkipped.htm)|
Возвращает значение, показывающее, возможен ли пропуск указанного этапа.  
[ComputeStageOrder](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_ComputeStageOrder.htm)|
Определяет порядок добавленного вручную этапа при вставке в маршрут.  
[DesignTimeCard](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_DesignTimeCard.htm)|
Возвращает значение, показывающее, может ли указанный тип карточки содержать
шаблоны этапов.  
[GetDocTypeID](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetDocTypeID.htm)|
Возвращает идентификатор типа документа для заданной карточки.  
[GetDocTypeIDAsync(Card, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetDocTypeIDAsync_1.htm)|
Асинхронно возвращает идентификатор типа документа для карточки с указанным
идентификатором. Метод кэширует тип документа в Card.Info, если он не был
найден в объекте карточки.  
[GetDocTypeIDAsync(Guid, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetDocTypeIDAsync.htm)|
Асинхронно возвращает идентификатор типа документа для карточки с указанным
идентификатором.  
[GetKrStateAsync(Card, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetKrStateAsync_1.htm)|
Асинхронно возвращает состояние карточки из возможных источников:
Секция KrApprovalCommonInfoVirtual;
Сателлит из Info карточки;
БД (опционально).  
[GetKrStateAsync(Guid, IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetKrStateAsync.htm)|
Асинхронно возвращает из базы данных состояние согласования для карточки с
указанным идентификатором.  
[RepairStorageRowsOrders(IList,
String)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_RepairStorageRowsOrders.htm)|
Восстанавливает порядок сортировки для списка строк.  
[RepairStorageRowsOrders(IList, String,
String)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_RepairStorageRowsOrders_1.htm)|
Восстанавливает порядок сортировки для списка строк.  
[RuntimeCard](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_RuntimeCard.htm)|
Возвращает значение, показывающее, является ли указанный тип карточки типом
карточки в котором выполняется маршрут.  
[SkipStage](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_SkipStage.htm)|
Выполняет пропуск этапа.  
[TryGetKrTypeAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_TryGetKrTypeAsync.htm)|
Возвращает эффективные настройки для типа карточки или типа документа
[IKrType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrType.htm) по
карточке card, которая загружена со всеми секциями, или null, если настройки
нельзя получить.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
