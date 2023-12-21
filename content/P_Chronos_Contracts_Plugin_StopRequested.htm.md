# Plugin.StopRequested - свойство
Признак того, что запрошена остановка плагина. Значение свойства можно
изменить только на true. Свойство устанавливается равным true сразу при
запрошенной остановке плагина, тогда как
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
переданный в метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm),
отменяется за несколько секунд до таймаута плагина, в соответсвии с настройкой
AwaitCancellationDeltaSeconds в файле app.json.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     protected bool StopRequested { get; set; }
VB __Копировать
     Protected Property StopRequested As Boolean
    	Get
    	Set
C++ __Копировать
     protected:
    property bool StopRequested {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member StopRequested : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[Plugin - ](T_Chronos_Contracts_Plugin.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
