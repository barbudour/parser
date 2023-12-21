# RouteDiff.DeleteStage - метод
Инициализирует новый экземпляр класса
[RouteDiff](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)
данными удалённого этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static RouteDiff DeleteStage(
    	Guid rowID,
    	string name,
    	bool hiddenStage
    )
VB __Копировать
     Public Shared Function DeleteStage ( 
    	rowID As Guid,
    	name As String,
    	hiddenStage As Boolean
    ) As RouteDiff
C++ __Копировать
     public:
    static RouteDiff^ DeleteStage(
    	Guid rowID, 
    	String^ name, 
    	bool hiddenStage
    )
F# __Копировать
     static member DeleteStage : 
            rowID : Guid * 
            name : string * 
            hiddenStage : bool -> RouteDiff 
#### Параметры
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор строки этапа.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Название удалённого этапа.
hiddenStage [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если этап является скрытым, иначе - false.
#### Возвращаемое значение
[RouteDiff](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)  
Инициализированный объект.
##  __См. также
#### Ссылки
[RouteDiff -
](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_RouteDiff.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
