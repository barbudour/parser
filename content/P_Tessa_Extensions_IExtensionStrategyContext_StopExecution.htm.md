# IExtensionStrategyContext.StopExecution - свойство
Признак того, что запрошена остановка выполнения цепочки расширений. Т.е.
текущее выполняемое расширение станет последним. При этом ошибок не
выбрасывается.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool StopExecution { get; set; }
VB __Копировать
     Property StopExecution As Boolean
    	Get
    	Set
C++ __Копировать
    property bool StopExecution {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     abstract StopExecution : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[IExtensionStrategyContext -
](T_Tessa_Extensions_IExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
