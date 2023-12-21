# LazyProcessManager - конструктор
Создаёт экземпляр класса с указанием функции, создающей объект
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm).
Гарантируется, что функция не будет вызвана более одного раза.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public LazyProcessManager(
    	Func<IProcessManager> createProcessManagerFunc
    )
VB __Копировать
     Public Sub New ( 
    	createProcessManagerFunc As Func(Of IProcessManager)
    )
C++ __Копировать
     public:
    LazyProcessManager(
    	Func<IProcessManager^>^ createProcessManagerFunc
    )
F# __Копировать
     new : 
            createProcessManagerFunc : Func<IProcessManager> -> LazyProcessManager
#### Параметры
createProcessManagerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm)>
     Функция, создающая объект [IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm). Не должна быть равна null. 
## __См. также
#### Ссылки
[LazyProcessManager - ](T_Chronos_Platform_Processes_LazyProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
