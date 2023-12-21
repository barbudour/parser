# ExtensionTraceListener.NotifyExecuted - метод
Уведомляет объект о том, что было завершено выполнение метода расширения,
информацию о котором можно получить из заданного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void NotifyExecuted(
    	IExtensionStrategyContext strategyContext
    )
VB __Копировать
     Public Overridable Sub NotifyExecuted ( 
    	strategyContext As IExtensionStrategyContext
    )
C++ __Копировать
     public:
    virtual void NotifyExecuted(
    	IExtensionStrategyContext^ strategyContext
    )
F# __Копировать
     abstract NotifyExecuted : 
            strategyContext : IExtensionStrategyContext -> unit 
    override NotifyExecuted : 
            strategyContext : IExtensionStrategyContext -> unit 
#### Параметры
strategyContext
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
     Контекст стратегии расширения, содержащий информацию о том, какой метод какого расширения был выполнен. 
#### Реализации
[IExtensionTraceListener.NotifyExecuted(IExtensionStrategyContext)](M_Tessa_Extensions_IExtensionTraceListener_NotifyExecuted.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
## __См. также
#### Ссылки
[ExtensionTraceListener - ](T_Tessa_Extensions_ExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
