# ExtensionTraceListener.NotifyExecuting - метод
Уведомляет объект о том, что следующим шагом будет выполнение метода
расширения, информацию о котором можно получить из заданного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void NotifyExecuting(
    	IExtensionStrategyContext strategyContext
    )
VB __Копировать
     Public Overridable Sub NotifyExecuting ( 
    	strategyContext As IExtensionStrategyContext
    )
C++ __Копировать
     public:
    virtual void NotifyExecuting(
    	IExtensionStrategyContext^ strategyContext
    )
F# __Копировать
     abstract NotifyExecuting : 
            strategyContext : IExtensionStrategyContext -> unit 
    override NotifyExecuting : 
            strategyContext : IExtensionStrategyContext -> unit 
#### Параметры
strategyContext
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
     Контекст стратегии расширения, содержащий информацию о том, какой метод какого расширения будет выполнен. 
#### Реализации
[IExtensionTraceListener.NotifyExecuting(IExtensionStrategyContext)](M_Tessa_Extensions_IExtensionTraceListener_NotifyExecuting.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
## __См. также
#### Ссылки
[ExtensionTraceListener - ](T_Tessa_Extensions_ExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
