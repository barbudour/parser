# PluginShutdownMode - перечисление
Способ завершения процесса хоста или плагина.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public enum PluginShutdownMode
VB __Копировать
     Public Enumeration PluginShutdownMode
C++ __Копировать
     public enum class PluginShutdownMode
F# __Копировать
     type PluginShutdownMode
##  __Заметки
Используется в классах
[PluginFacade](T_Chronos_Platform_Scheduling_PluginFacade.htm) и
[PluginGracefulLauncher](T_Chronos_Platform_Scheduling_PluginGracefulLauncher.htm).
## __Члены
ImmediateStop| 0|  При завершении работы хоста плагины немедленно
останавливаются.  
---|---|---  
GracefulStop| 1|  При завершении работы хоста плагины имеют возможность
завершить свою работу посредством реализации интерфейса
[ISupportGracefulStop](T_Chronos_Contracts_ISupportGracefulStop.htm).  
## __См. также
#### Ссылки
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
