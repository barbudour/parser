# SchedulingType - перечисление
Способ указания расписания для выполнения действий с ролевой моделью.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    public enum SchedulingType
VB __Копировать
    <DataContractAttribute>
    Public Enumeration SchedulingType
C++ __Копировать
    [DataContractAttribute]
    public enum class SchedulingType
F# __Копировать
     [<DataContractAttribute>]
    type SchedulingType
##  __Члены
Period| 0|  Выполнение действий с ролевой моделью осуществляется с заданным в
[PeriodScheduling](P_Tessa_Roles_DynamicRole_PeriodScheduling.htm) интервалом
в секундах.  
---|---|---  
Cron| 1|  Выполнение действий с ролевой моделью осуществляется по расписанию,
заданному в строке Cron
[CronScheduling](P_Tessa_Roles_DynamicRole_CronScheduling.htm).  
## __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
