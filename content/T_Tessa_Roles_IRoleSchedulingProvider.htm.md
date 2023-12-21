# IRoleSchedulingProvider - интерфейс
Определяет расписание выполнения запланированных действий с ролевой моделью.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRoleSchedulingProvider
VB __Копировать
     Public Interface IRoleSchedulingProvider
C++ __Копировать
     public interface class IRoleSchedulingProvider
F# __Копировать
     type IRoleSchedulingProvider = interface end
##  __Свойства
[CronScheduling](P_Tessa_Roles_IRoleSchedulingProvider_CronScheduling.htm)|
Строка Cron, определяющая расписание, или null, если расписание определяется
не через Cron.  
---|---  
[PeriodScheduling](P_Tessa_Roles_IRoleSchedulingProvider_PeriodScheduling.htm)|
Интервал в секундах, определяющий период, или null, если расписание
определяется не через период.  
[ScheduleAtLaunch](P_Tessa_Roles_IRoleSchedulingProvider_ScheduleAtLaunch.htm)|
Запланировать пересчёт при запуске сервиса Chronos.  
[SchedulingType](P_Tessa_Roles_IRoleSchedulingProvider_SchedulingType.htm)|
Способ указания расписания.  
##  __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
