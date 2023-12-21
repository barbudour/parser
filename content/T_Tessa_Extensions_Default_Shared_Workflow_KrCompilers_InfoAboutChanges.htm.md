# InfoAboutChanges - перечисление
Перечисление режимов вывода информации об изменениях в маршруте после
пересчёта.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum InfoAboutChanges
VB __Копировать
    <FlagsAttribute>
    Public Enumeration InfoAboutChanges
C++ __Копировать
    [FlagsAttribute]
    public enum class InfoAboutChanges
F# __Копировать
     [<FlagsAttribute>]
    type InfoAboutChanges
##  __Члены
None| 0|  В response.Info не будет информации об изменениях маршрута после
пересчета.  
---|---|---  
HasChangesToInfo| 1|  Булевое значение о наличии изменений будет помещено в
response.Info[KrCompilersInfo.HasChangesInRoute].  
ChangesListToInfo| 2|  Список изменений RouteDiff будет помещен в
response.Info[KrCompilersInfo.RouteChanges].  
ToInfo| 3|  Логическое значение о наличии изменений будет помещено в
response.Info[KrCompilersInfo.HasChangesInRoute]. Список изменений RouteDiff
будет помещен в response.Info[KrCompilersInfo.RouteChanges].  
HasChangesToValidationResult| 4|  Информация о наличии изменений в маршруте
будет помещена в response.ValidationResult в читаемом виде.  
ChangesListToValidationResult| 8|  Список изменений будет помещен в
response.ValidationResult в читаемом виде.  
ToValidationResult| 12|  Информация о наличии изменений в маршруте будет
помещена в response.ValidationResult в читаемом виде.  
ChangesInHiddenStages| 22|  В список изменений будут включены изменения в
скрытых этапах.  
ToInfoIncludingHiddenStages| 23|  Аналогично ToInfo с учетом скрытых этапов.  
ToValidationResultIncludingHiddenStages| 30|  Аналогично ToValidationResult с
учетом скрытых этапов.  
Full| 31|  Список изменений RouteDiff будет помещен в
response.Info[KrCompilersInfo.RouteChanges].
Список изменений будет помещен в response.ValidationResult в читаемом виде.
Во все списки изменений будут включены скрытые этапы.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
