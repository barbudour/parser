# ExtensionContainer.ResolveStrategy - метод
Возвращает стратегию, зарегистрированную на заданном этапе, или
[EmptyExtensionStrategy](T_Tessa_Extensions_EmptyExtensionStrategy.htm), если
стратегия не была зарегистрирована.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IExtensionStrategy ResolveStrategy(
    	ExtensionStrategyStage stage
    )
VB __Копировать
     Public Function ResolveStrategy ( 
    	stage As ExtensionStrategyStage
    ) As IExtensionStrategy
C++ __Копировать
     public:
    virtual IExtensionStrategy^ ResolveStrategy(
    	ExtensionStrategyStage stage
    ) sealed
F# __Копировать
     abstract ResolveStrategy : 
            stage : ExtensionStrategyStage -> IExtensionStrategy 
    override ResolveStrategy : 
            stage : ExtensionStrategyStage -> IExtensionStrategy 
#### Параметры
stage [ExtensionStrategyStage](T_Tessa_Extensions_ExtensionStrategyStage.htm)
    Этап, на котором зарегистрирована требуемая стратегия.
#### Возвращаемое значение
[IExtensionStrategy](T_Tessa_Extensions_IExtensionStrategy.htm)  
Стратегия, зарегистрированная на заданном этапе.
#### Реализации
[IExtensionContainer.ResolveStrategy(ExtensionStrategyStage)](M_Tessa_Extensions_IExtensionContainer_ResolveStrategy.htm)  
##  __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
