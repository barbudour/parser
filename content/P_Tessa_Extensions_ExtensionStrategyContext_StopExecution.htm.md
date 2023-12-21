# ExtensionStrategyContext.StopExecution - свойство
Признак того, что запрошена остановка выполнения цепочки расширений. Т.е.
текущее выполняемое расширение станет последним. При этом ошибок не
выбрасывается.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool StopExecution { get; set; }
VB __Копировать
     Public Property StopExecution As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool StopExecution {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract StopExecution : bool with get, set
    override StopExecution : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IExtensionStrategyContext.StopExecution](P_Tessa_Extensions_IExtensionStrategyContext_StopExecution.htm)  
##  __См. также
#### Ссылки
[ExtensionStrategyContext - ](T_Tessa_Extensions_ExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
