# ExtensionTraceListener.NotifyException - метод
Уведомляет объект о том, что возникло исключение в процессе выполнения метода
расширения, информацию о котором можно получить из заданного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void NotifyException(
    	IExtensionStrategyContext strategyContext
    )
VB __Копировать
     Public Overridable Sub NotifyException ( 
    	strategyContext As IExtensionStrategyContext
    )
C++ __Копировать
     public:
    virtual void NotifyException(
    	IExtensionStrategyContext^ strategyContext
    )
F# __Копировать
     abstract NotifyException : 
            strategyContext : IExtensionStrategyContext -> unit 
    override NotifyException : 
            strategyContext : IExtensionStrategyContext -> unit 
#### Параметры
strategyContext
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
     Контекст стратегии расширения, содержащий информацию о том, какой метод какого расширения был выполнен. В свойстве [Tessa.Extensions.IExtensionStrategyContext.Exception] будет содержаться объект возникшего исключения. Указав свойство [Tessa.Extensions.IExtensionStrategyContext.ExceptionHandlingMode] можно установить способ обработки исключения после того, как этот метод будет выполнен. 
#### Реализации
[IExtensionTraceListener.NotifyException(IExtensionStrategyContext)](M_Tessa_Extensions_IExtensionTraceListener_NotifyException.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
## __См. также
#### Ссылки
[ExtensionTraceListener - ](T_Tessa_Extensions_ExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
