# KrProcessSharedHelper.ComputeStageOrder - метод
Определяет порядок добавленного вручную этапа при вставке в маршрут.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static int ComputeStageOrder(
    	Guid groupID,
    	int groupOrder,
    	IReadOnlyList<CardRow> rows
    )
VB __Копировать
     Public Shared Function ComputeStageOrder ( 
    	groupID As Guid,
    	groupOrder As Integer,
    	rows As IReadOnlyList(Of CardRow)
    ) As Integer
C++ __Копировать
     public:
    static int ComputeStageOrder(
    	Guid groupID, 
    	int groupOrder, 
    	IReadOnlyList<CardRow^>^ rows
    )
F# __Копировать
     static member ComputeStageOrder : 
            groupID : Guid * 
            groupOrder : int * 
            rows : IReadOnlyList<CardRow> -> int 
#### Параметры
groupID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор группы этапов.
groupOrder [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Порядок группы этапов.
rows
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[CardRow](T_Tessa_Cards_CardRow.htm)>
    Список строк, в который выполняется вставка нового этапа.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Порядок добавленного вручную этапа при вставке в маршрут.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
