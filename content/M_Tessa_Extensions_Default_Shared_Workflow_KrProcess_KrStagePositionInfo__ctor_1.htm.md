# KrStagePositionInfo(CardRow, Int32, Nullable<Int32>, Boolean, Boolean,
Boolean) - конструктор
Инициализирует новый экземпляр класса
[KrStagePositionInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStagePositionInfo.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrStagePositionInfo(
    	CardRow stageRow,
    	int absoluteOrder,
    	int? shiftedOrder,
    	bool saveRow,
    	bool hidden,
    	bool skip
    )
VB __Копировать
     Public Sub New ( 
    	stageRow As CardRow,
    	absoluteOrder As Integer,
    	shiftedOrder As Integer?,
    	saveRow As Boolean,
    	hidden As Boolean,
    	skip As Boolean
    )
C++ __Копировать
     public:
    KrStagePositionInfo(
    	CardRow^ stageRow, 
    	int absoluteOrder, 
    	Nullable<int> shiftedOrder, 
    	bool saveRow, 
    	bool hidden, 
    	bool skip
    )
F# __Копировать
     new : 
            stageRow : CardRow * 
            absoluteOrder : int * 
            shiftedOrder : Nullable<int> * 
            saveRow : bool * 
            hidden : bool * 
            skip : bool -> KrStagePositionInfo
#### Параметры
stageRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка для которой формируется информация о позиции.
absoluteOrder [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Абсолютный порядок этапа в маршруте.
shiftedOrder
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
    Сдвинутый порядок с учетом скрытых этапов.
saveRow [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если необходимо сохранить информацию о строке этапа для которой формируется информация о позиции, иначе - false.
hidden [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если этап является скрытым, иначе - false.
skip [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если этап является пропущенным, иначе - false.
##  __См. также
#### Ссылки
[KrStagePositionInfo -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStagePositionInfo.htm)
[KrStagePositionInfo -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStagePositionInfo__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
