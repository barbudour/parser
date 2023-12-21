# ExtensionStrategyContext.ExceptionHandlingMode - свойство
Режим обработки исключений, возникающий в методах расширений. Может быть
изменён в т.ч. в методе
[Tessa.Extensions.IExtensionTraceListener.NotifyException].
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ExceptionHandlingMode ExceptionHandlingMode { get; set; }
VB __Копировать
     Public Property ExceptionHandlingMode As ExceptionHandlingMode
    	Get
    	Set
C++ __Копировать
     public:
    virtual property ExceptionHandlingMode ExceptionHandlingMode {
    	ExceptionHandlingMode get () sealed;
    	void set (ExceptionHandlingMode value) sealed;
    }
F# __Копировать
     abstract ExceptionHandlingMode : ExceptionHandlingMode with get, set
    override ExceptionHandlingMode : ExceptionHandlingMode with get, set
#### Значение свойства
[ExceptionHandlingMode](T_Tessa_Extensions_ExceptionHandlingMode.htm)
#### Реализации
[IExtensionStrategyContext.ExceptionHandlingMode](P_Tessa_Extensions_IExtensionStrategyContext_ExceptionHandlingMode.htm)  
##  __См. также
#### Ссылки
[ExtensionStrategyContext - ](T_Tessa_Extensions_ExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
