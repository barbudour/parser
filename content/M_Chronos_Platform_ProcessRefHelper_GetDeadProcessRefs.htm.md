# ProcessRefHelper.GetDeadProcessRefs - метод
Возвращает список процессов, на которые есть ссылки, но которые уже были
завершены.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<ProcessRef> GetDeadProcessRefs(
    	IEnumerable<ProcessRef> processesRef
    )
VB __Копировать
     Public Shared Function GetDeadProcessRefs ( 
    	processesRef As IEnumerable(Of ProcessRef)
    ) As IList(Of ProcessRef)
C++ __Копировать
     public:
    static IList<ProcessRef>^ GetDeadProcessRefs(
    	IEnumerable<ProcessRef>^ processesRef
    )
F# __Копировать
     static member GetDeadProcessRefs : 
            processesRef : IEnumerable<ProcessRef> -> IList<ProcessRef> 
#### Параметры
processesRef
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)>
    Перечисление ссылок на процессы, для которых требуется вернуть список объектов, ссылающихся на завершённые процессы.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)>  
Список процессов, на которые есть ссылки, но которые уже были завершены.
##  __См. также
#### Ссылки
[ProcessRefHelper - ](T_Chronos_Platform_ProcessRefHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
