# ExtensionStrategyContext.Exception - свойство
Исключение, возникшее в процессе выполнения метода расширения, или null, если
метод ещё не был выполнен или расширение не выбросило исключение.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Exception Exception { get; set; }
VB __Копировать
     Public Property Exception As Exception
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Exception^ Exception {
    	Exception^ get () sealed;
    	void set (Exception^ value) sealed;
    }
F# __Копировать
     abstract Exception : Exception with get, set
    override Exception : Exception with get, set
#### Значение свойства
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
#### Реализации
[IExtensionStrategyContext.Exception](P_Tessa_Extensions_IExtensionStrategyContext_Exception.htm)  
##  __См. также
#### Ссылки
[ExtensionStrategyContext - ](T_Tessa_Extensions_ExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
