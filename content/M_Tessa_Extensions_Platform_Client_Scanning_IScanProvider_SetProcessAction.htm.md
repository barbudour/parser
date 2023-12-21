# IScanProvider.SetProcessAction - метод
Устанавливает функцию, вызываемую для отсканированной страницы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     void SetProcessAction(
    	Func<MemoryStream, CancellationToken, ValueTask> actionAsync
    )
VB __Копировать
     Sub SetProcessAction ( 
    	actionAsync As Func(Of MemoryStream, CancellationToken, ValueTask)
    )
C++ __Копировать
     void SetProcessAction(
    	Func<MemoryStream^, CancellationToken, ValueTask>^ actionAsync
    )
F# __Копировать
     abstract SetProcessAction : 
            actionAsync : Func<MemoryStream, CancellationToken, ValueTask> -> unit 
#### Параметры
actionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
    Действие, выполняемое для отсканированной страницы, данные по которой передаются в параметре.
##  __См. также
#### Ссылки
[IScanProvider -
](T_Tessa_Extensions_Platform_Client_Scanning_IScanProvider.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
