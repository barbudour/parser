# KrConstants.GetRouteStageNamesWithDefaultStages(String[]) - метод
Возвращает перечисление названий этапов маршрута включающее названия типовых
этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static IEnumerable<string> GetRouteStageNamesWithDefaultStages(
    	params string[] customStageNames
    )
VB __Копировать
     Public Shared Function GetRouteStageNamesWithDefaultStages ( 
    	ParamArray customStageNames As String()
    ) As IEnumerable(Of String)
C++ __Копировать
     public:
    static IEnumerable<String^>^ GetRouteStageNamesWithDefaultStages(
    	... array<String^>^ customStageNames
    )
F# __Копировать
     static member GetRouteStageNamesWithDefaultStages : 
            customStageNames : string[] -> IEnumerable<string> 
#### Параметры
customStageNames
[String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Перечисление названий этапов из кастомного процесса.
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Перечисление названий этапов маршрута.
##  __Заметки
Число типовых этапов содержится в константе
[DefaultStagesCount](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_DefaultStagesCount.htm).
##  __См. также
#### Ссылки
[KrConstants -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants.htm)
[GetRouteStageNamesWithDefaultStages -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_GetRouteStageNamesWithDefaultStages.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
