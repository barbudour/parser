# ExtensionStrategyContext.ConcreteContexts - свойство
Список контекстов для экземпляров расширений, доступных на этапе
упорядочивания цепочки типов расширений, или null на прочих этапах.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IExtensionStrategyContext[] ConcreteContexts { get; set; }
VB __Копировать
     Public Property ConcreteContexts As IExtensionStrategyContext()
    	Get
    	Set
C++ __Копировать
     public:
    virtual property array<IExtensionStrategyContext^>^ ConcreteContexts {
    	array<IExtensionStrategyContext^>^ get () sealed;
    	void set (array<IExtensionStrategyContext^>^ value) sealed;
    }
F# __Копировать
     abstract ConcreteContexts : IExtensionStrategyContext[] with get, set
    override ConcreteContexts : IExtensionStrategyContext[] with get, set
#### Значение свойства
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)[]
#### Реализации
[IExtensionStrategyContext.ConcreteContexts](P_Tessa_Extensions_IExtensionStrategyContext_ConcreteContexts.htm)  
##  __См. также
#### Ссылки
[ExtensionStrategyContext - ](T_Tessa_Extensions_ExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
