# RouteDiff.ModifyStage - метод
Инициализирует новый экземпляр класса
[RouteDiff](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)
данными изменённого этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static RouteDiff ModifyStage(
    	Guid rowID,
    	string actualName,
    	string oldName,
    	bool hiddenStage,
    	bool hasPlainChanges = true
    )
VB __Копировать
     Public Shared Function ModifyStage ( 
    	rowID As Guid,
    	actualName As String,
    	oldName As String,
    	hiddenStage As Boolean,
    	Optional hasPlainChanges As Boolean = true
    ) As RouteDiff
C++ __Копировать
     public:
    static RouteDiff^ ModifyStage(
    	Guid rowID, 
    	String^ actualName, 
    	String^ oldName, 
    	bool hiddenStage, 
    	bool hasPlainChanges = true
    )
F# __Копировать
     static member ModifyStage : 
            rowID : Guid * 
            actualName : string * 
            oldName : string * 
            hiddenStage : bool * 
            ?hasPlainChanges : bool 
    (* Defaults:
            let _hasPlainChanges = defaultArg hasPlainChanges true
    *)
    -> RouteDiff 
#### Параметры
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор строки этапа.
actualName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Актуальное название этапа.
oldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Предыдущее название этапа.
hiddenStage [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если этап является скрытым, иначе - false.
hasPlainChanges
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Значение true, если были изменены поля этапа, иначе - false.
#### Возвращаемое значение
[RouteDiff](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)  
Инициализированный объект.
##  __См. также
#### Ссылки
[RouteDiff -
](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
