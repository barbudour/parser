# Plugin.StopRequestedToken - свойство
Токен отмены плагина, который запрашивается сразу при установке свойства
[StopRequested](P_Chronos_Contracts_Plugin_StopRequested.htm) равным true,
т.е. в момент запроса остановки плагина. Объект
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
переданный в метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm),
отменяется за несколько секунд до таймаута плагина, в соответсвии с настройкой
AwaitCancellationDeltaSeconds в файле app.json.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     protected CancellationToken StopRequestedToken { get; }
VB __Копировать
     Protected ReadOnly Property StopRequestedToken As CancellationToken
    	Get
C++ __Копировать
     protected:
    property CancellationToken StopRequestedToken {
    	CancellationToken get ();
    }
F# __Копировать
     member StopRequestedToken : CancellationToken with get
#### Значение свойства
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
##  __См. также
#### Ссылки
[Plugin - ](T_Chronos_Contracts_Plugin.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
