# ProcessRefHelper.KillMany - метод
Принудительно завершает все процессы, ссылки на которое приведены в указанном
перечислении.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void KillMany(
    	IEnumerable<ProcessRef> processesRef,
    	out List<ProcessRef> notKilledProcesses
    )
VB __Копировать
     Public Shared Sub KillMany ( 
    	processesRef As IEnumerable(Of ProcessRef),
    	<OutAttribute> ByRef notKilledProcesses As List(Of ProcessRef)
    )
C++ __Копировать
     public:
    static void KillMany(
    	IEnumerable<ProcessRef>^ processesRef, 
    	[OutAttribute] List<ProcessRef>^% notKilledProcesses
    )
F# __Копировать
     static member KillMany : 
            processesRef : IEnumerable<ProcessRef> * 
            notKilledProcesses : List<ProcessRef> byref -> unit 
#### Параметры
processesRef
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)>
    Перечисление ссылок на процессы, которые требуется завершить.
notKilledProcesses
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)>
    Список ссылок на процессы, которые завершить не удалось.
##  __См. также
#### Ссылки
[ProcessRefHelper - ](T_Chronos_Platform_ProcessRefHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
