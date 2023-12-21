# AggregateExtensionStrategy - конструктор
Создаёт экземпляр класса с указанием последовательно выполняемых стратегий.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AggregateExtensionStrategy(
    	params IExtensionStrategy[] strategies
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray strategies As IExtensionStrategy()
    )
C++ __Копировать
     public:
    AggregateExtensionStrategy(
    	... array<IExtensionStrategy^>^ strategies
    )
F# __Копировать
     new : 
            strategies : IExtensionStrategy[] -> AggregateExtensionStrategy
#### Параметры
strategies [IExtensionStrategy](T_Tessa_Extensions_IExtensionStrategy.htm)[]
     Стратегии, которые будут выполнены в заданной последовательности при выполнении текущей стратегии. Значения null не допустимы. 
## __См. также
#### Ссылки
[AggregateExtensionStrategy -
](T_Tessa_Extensions_AggregateExtensionStrategy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
