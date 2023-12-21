# Chronos.Platform.Processes - пространство имён
Инструменты для создания хоста Chronos и дочерних процессов.
##  __Классы
[CommandLineProcessHost](T_Chronos_Platform_Processes_CommandLineProcessHost.htm)|
Хост, передающий данные дочерним процессам через аргументы командной строки.  
---|---  
[JobProcessManager](T_Chronos_Platform_Processes_JobProcessManager.htm)|
Менеджер процессов, использующий
[ProcessJob](T_Chronos_Platform_Processes_ProcessJob.htm) для объединения
процессов в группу. Позволяет запускать дочерние процессы и управлять их
временем жизни. Используйте класс
[WindowsProcessManagerFactory](T_Chronos_Platform_Processes_WindowsProcessManagerFactory.htm),
чтобы создать экземпляр класса.  
[LazyProcessManager](T_Chronos_Platform_Processes_LazyProcessManager.htm)|
Менеджер процессов, делегирующий все свои действия другому менеджеру
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm), который
создаётся при первом обращении к методам.  
[ProcessJob](T_Chronos_Platform_Processes_ProcessJob.htm)|  Обёртка для
использования объекта WinAPI Job.  
[ProcessManager](T_Chronos_Platform_Processes_ProcessManager.htm)|  Менеджер
процессов по умолчанию. Позволяет запускать дочерние процессы и управлять их
временем жизни.  
[ProcessRefContainer](T_Chronos_Platform_Processes_ProcessRefContainer.htm)|
Контейнер, осуществляющий хранение объектов
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm) в изолированном
хранилище.  
[WindowsProcessManagerFactory](T_Chronos_Platform_Processes_WindowsProcessManagerFactory.htm)|
Вспомогательные методы для создания объектов
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm).  
## __Структуры
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)|  Информация,
идентифицирующая запущенный процесс.  
---|---  
## __Интерфейсы
[IProcessHost](T_Chronos_Platform_Processes_IProcessHost.htm)|  Позволяет
запускать дочерние процессы.  
---|---  
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm)|  Менеджер
процессов. Позволяет запускать дочерние процессы и управлять их временем
жизни.
