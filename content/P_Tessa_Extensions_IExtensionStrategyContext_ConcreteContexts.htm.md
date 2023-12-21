# IExtensionStrategyContext.ConcreteContexts - свойство
Список контекстов для экземпляров расширений, доступных на этапе
упорядочивания цепочки типов расширений, или null на прочих этапах.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    IExtensionStrategyContext[] ConcreteContexts { get; set; }
VB __Копировать
     Property ConcreteContexts As IExtensionStrategyContext()
    	Get
    	Set
C++ __Копировать
    property array<IExtensionStrategyContext^>^ ConcreteContexts {
    	array<IExtensionStrategyContext^>^ get ();
    	void set (array<IExtensionStrategyContext^>^ value);
    }
F# __Копировать
     abstract ConcreteContexts : IExtensionStrategyContext[] with get, set
#### Значение свойства
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)[]
##  __См. также
#### Ссылки
[IExtensionStrategyContext -
](T_Tessa_Extensions_IExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
